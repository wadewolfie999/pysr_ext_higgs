# Version v5.7.0
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.utils.class_weight import compute_sample_weight
from sr import (run_id_ledger, do_split, expr_indexer, auc_recorder, top_three_sort,
                expr_expander, expr_pdf_compiler, run_finalizer, plot_roc_curve,
                plot_1d_mass, plot_mass_plane, plot_expr_folds_variability, save_plot,
                write_run_metadata, SEED)

PROJECT_DIR = Path(__file__).resolve().parent
SAVE_PLOTS, SHOW_PLOTS = True, False


def main() -> None:
    # The unchanged run counter intentionally operates in the repository root.
    if Path.cwd().resolve() != PROJECT_DIR:
        raise RuntimeError(f"Run main.py from {PROJECT_DIR}")
    from pysr import PySRRegressor


    # Choose ONE:
    # loss_ZOL  = "ZeroOneLoss()"
    loss_L2HL = "L2HingeLoss()"
    # loss_L2ML = "L2MarginLoss()"
    # loss_MHL  = "ModifiedHuberLoss()"
    # loss_SL   = "SigmoidLoss()"

    RUN_ID = f"L2HL_{next(run_id_ledger())}"

    RUN_DIR = PROJECT_DIR / "output" / RUN_ID
    RUN_DIR.mkdir(parents=True, exist_ok=False)

    total_ME1 = "data/masses_exclusions.csv"
    df = pd.read_csv(total_ME1)

    features = ["mchi1","mchipm1"]
    target = "exclusion"

    df = df.dropna(subset=features + [target])

    X = df[features].astype(float)
    y = df[target].astype(int)

    X_train, y_train, X_val, y_val, X_test, y_test, X_total, y_total= do_split(X,y, seed=SEED)
    # Save a copy for later use
    cp_path = Path("data/auc")
    cp_path.mkdir(parents=True, exist_ok=True)
    test_ME1 = X_test.copy()
    test_ME1["exclusion"] = np.asarray(y_test)
    test_ME1.to_csv(cp_path / "test_ME1.csv", index=False)

    val_ME1 = X_val.copy()
    val_ME1["exclusion"] = np.asarray(y_val)
    val_ME1.to_csv(cp_path / "val_ME1.csv", index=False)


    sample_weights = compute_sample_weight(class_weight="balanced", y=y_train)

    y_train_signed = 2 * y_train.astype(int) - 1

    # NEW Regressor -> based on https://pysr.ai/v2.7.2/#detailed-example
    model = PySRRegressor(
    elementwise_loss=loss_L2HL,
    parallelism="multithreading",
    # procs=4,
    populations=8,
    # ^ Assuming we have 4 cores, this means 2 populations per core, so one is always running.
    population_size=100,
    # ^ Slightly larger populations, for greater diversity.
    ncycles_per_iteration=100,
    # ^ Generations between migrations.   ???
    output_directory="output/",
    run_id=RUN_ID,
    niterations=100,
    early_stop_condition=(
        "stop_if(loss, complexity) = loss < 1e-6 && complexity < 500"
        # Stop early if we find a good and simple equation
    ),
    timeout_in_seconds=60 * 60 * 1,
    # ^ Alternatively, stop after (HP) 4 hours have passed.

    maxsize=280,
    # ^ Allow greater complexity.
    #maxdepth=40,
    # ^ But, avoid deep nesting.
    binary_operators=["*", "+", "-", "/"],
    unary_operators=["square", "cube", "exp", "cos"],
    # constraints={
    #     "/": (-1, 4),
    #     "square": 5,
    #     "cube": 2,
    #     "exp": 6,
    # },
    # ^ Limit the complexity within each argument.
    # "inv": (-1, 9) states that the numerator has no constraint,
    # but the denominator has a max complexity of 9.
    # "exp": 9 simply states that `exp` can only have
    # an expression of complexity 9 as input.
    # nested_constraints={
    #      "square": {"square": 1, "cube": 1, "exp": 0},
    #      "cube": {"square": 1, "cube": 1, "exp": 0},
    #      "exp": {"square": 1, "cube": 1, "exp": 0},
    # },
    # ^ Nesting constraints on operators. For example,
    # "square(exp(x))" is not allowed, since "square": {"exp": 0}.
    #complexity_of_operators={"/": 2, "exp": 3},
    # ^ Custom complexity of particular operators.
    #complexity_of_constants=2,
    # ^ Punish constants more than variables
    #select_k_features=2,
    # ^ Train on only the 4 most important features -> Here -> 2
    progress=True,
    # ^ Can set to false if printing to a file.
    #weight_randomize=0.1,
    # ^ Randomize the tree much more frequently
    # cluster_manager=None,
    # ^ Can be set to, e.g., "slurm", to run a slurm
    # cluster. Just launch one script from the head node.
    precision=64,
    # ^ Higher precision calculations.
    warm_start=True,
    # ^ Start from where left off.
    # turbo=True,
    # ^ Faster evaluation (experimental)
    # extra_sympy_mappings={"cos2": lambda x: sp.cos(x)**2},
    # extra_torch_mappings={sympy.cos: torch.cos},
    # ^ Not needed as cos already defined, but this
    # is how you define custom torch operators.
    # extra_jax_mappings={sympy.cos: "jnp.cos"},
    # ^ For JAX, one passes a string
    parsimony=1e-3,
    #adaptive_parsimony_scaling=40
)

    datasets = {"train": (X_train, y_train), "validation": (X_val, y_val),
                "test": (X_test, y_test), "total": (X_total, y_total)}
    write_run_metadata(RUN_DIR, project_dir=PROJECT_DIR, data_csv=PROJECT_DIR / total_ME1,
                       datasets=datasets, model_parameters=model.get_params(),
                       training_labels=y_train_signed, sample_weights=sample_weights,
                       split_seed=SEED, weight_policy="balanced classes computed on training rows only")
    model.fit(X_train, y_train_signed, weights=sample_weights)

    HOF = model.equations_
    HOF_01 = expr_indexer(HOF, RUN_ID, features)
    HOF_02, evaluations = auc_recorder(HOF_01, datasets)
    HOF_03, _rank_one_id = top_three_sort(HOF_02)
    HOF_4_pt1 = expr_expander(HOF_03, RUN_DIR, features)
    HOF_4_pt2 = expr_pdf_compiler(HOF_03, _rank_one_id, RUN_DIR)
    HOF_FINAL = run_finalizer(HOF_4_pt1, HOF_4_pt2, RUN_ID, PROJECT_DIR / ".run_num1_logger.csv")
    print(HOF_FINAL.to_string(index=False))

    equation = HOF_03.set_index("Expression_ID").loc[_rank_one_id, "Lambda_Equation"]
    X_slice = pd.DataFrame({"mchi1": np.linspace(1, 2001, 2000), "mchipm1": 2000.0})
    fold_fig, fold_ax, fold_table, summary, _ = plot_expr_folds_variability(_rank_one_id, datasets, evaluations)
    figures = {"roc_curve.pdf": plot_roc_curve(_rank_one_id, evaluations, magnified=True),
               "mass_scan_1d.pdf": plot_1d_mass(equation, X_slice, Expression_ID=_rank_one_id),
               "mass_plane.pdf": plot_mass_plane(_rank_one_id, datasets, evaluations),
               "subset_variability.pdf": (fold_fig, fold_ax)}
    print(fold_table.to_string(), summary, sep="\n")
    for filename, (fig, _) in figures.items():
        if SAVE_PLOTS:
            save_plot(fig, filename, RUN_DIR / "plots")
    if SHOW_PLOTS:
        plt.show()
    else:
        for fig, _ in figures.values():
            plt.close(fig)


if __name__ == "__main__":
    main()
