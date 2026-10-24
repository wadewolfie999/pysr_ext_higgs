# Version v5.2.0
import pandas as pd
import numpy as np
from pysr import PySRRegressor
from pathlib import Path
from sklearn.utils.class_weight import compute_sample_weight
from sr import run_id_ledger, do_split, report_auc


def main() -> None:

    run_id = run_id_ledger()
    value = next(run_id)
    RUN_ID = Path(".tmp") / f"TEMP_{value}"
    expr_dir = RUN_ID / "expressions"
    plot_dir =  RUN_ID / "plots"
    plot_dir.mkdir(parents=True, exist_ok=True)
    expr_dir.mkdir(parents=True, exist_ok=True)

    total_ME1 = "data/masses_exclusions.csv"
    df = pd.read_csv(total_ME1)
    
    features = ["mchi1","mchipm1"]
    target = "exclusion"
    
    df = df.dropna(subset=features + [target])
    
    X = df[features].astype(float)
    y = df[target].astype(int)
    X_train, y_train, X_val, y_val, X_test, y_test, X_total, y_total= do_split(X,y)
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
    
    # NEW Regressor -> based on https://pysr.ai/v2.7.2/#detailed-example
    model = PySRRegressor(
        # parallelism="multiprocessing",
        # procs=6,
        populations=16,
        # ^ Assuming we have 4 cores, this means 2 populations per core, so one is always running.
        population_size=50,
        # ^ Slightly larger populations, for greater diversity.
        #ncycles_per_iteration=500,
        # ^ Generations between migrations.   ???
        output_directory="./",
        run_id=str(RUN_ID),
        #niterations=100,  
        early_stop_condition=(
            "stop_if(loss, complexity) = loss < 1e-6 && complexity < 100"
            # Stop early if we find a good and simple equation
        ),
        timeout_in_seconds=60 * 60 * 5,
        # ^ Alternatively, stop after  hours have passed.
        maxsize=300,
        # ^ Allow greater complexity.
        maxdepth=40,
        # ^ But, avoid deep nesting.
        
        binary_operators=["*", "+", "-", "/"],
    
        unary_operators=["square", "sqrt", "sin", "sinh", "cosh", "exp", "cos"],
        constraints={
             "/": (-1, 6),
             "square": 6,
             "cos": 6,
             "exp": 6,
             "sin": 6,
             "sinh": 6,
             "cosh": 6
        },
        # ^ Limit the complexity within each argument.
        # "inv": (-1, 9) states that the numerator has no constraint,
        # but the denominator has a max complexity of 9.
        # "exp": 9 simply states that `exp` can only have
        # an expression of complexity 9 as input.
        nested_constraints={
            "square": {"square": 2, "cos": 4, "cosh": 4, "sin": 4,"sinh": 4, "exp": 2},
            "cos" : {"square": 2, "cos": 1, "cosh": 2, "sin": 1,"sinh": 2, "exp": 2},
            "exp": {"square": 2, "cos": 2, "cosh": 2, "sin": 2,"sinh": 2, "exp": 0},
            "sin": {"square": 2, "cos": 1, "cosh": 2, "sin": 1,"sinh": 2, "exp": 2},
            "cosh": {"square": 2, "cos": 2, "cosh": 0, "sin": 2,"sinh": 0, "exp": 2},
            "sinh": {"square": 2, "cos": 2, "cosh": 0, "sin": 2,"sinh": 0, "exp": 2}
        },


        # ^ Nesting constraints on operators. For example,
        # "square(exp(x))" is not allowed, since "square": {"exp": 0}.
        complexity_of_operators={"/": 2, "exp": 3},
        # ^ Custom complexity of particular operators.
        complexity_of_constants=2,
        # ^ Punish constants more than variables
        select_k_features=2,
        #^ Train on only the 4 most important features -> Here -> 2
        progress=True,
        # ^ Can set to false if printing to a file.
        weight_randomize=0.1,
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
        # ^ For JAX, one passes a string.
)
    model.fit(X_train, y_train, weights=sample_weights)


    # <CAN-BE-CHANGED>
# Revision v5.1.0: select/report by validation AUC in one pass.


    datasets = {"train": (X_train, y_train), "validation": (X_val, y_val),
                "test": (X_test, y_test), "total": (X_total, y_total)}
    result = report_auc(model, datasets, directory=expr_dir, top_n=5)
# </CAN-BE-CHANGED>
    

if __name__ == "__main__":
    main()
