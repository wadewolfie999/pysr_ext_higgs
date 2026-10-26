# Version v5.7.0
import hashlib
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sr import (do_split, load_saved_expression, auc_recorder, plot_roc_curve, plot_1d_mass,
                plot_mass_plane, plot_expr_folds_variability, save_plot)

PROJECT_DIR = Path(__file__).resolve().parent
RUN_SOURCE = PROJECT_DIR / "results/L2HL_1_050/manifest.json"
DATA_CSV = PROJECT_DIR / "data/masses_exclusions.csv"
EXPRESSION_ID = "L2HL_1_050"
FEATURES = ["mchi1", "mchipm1"]
SAVE_PLOTS, SHOW_PLOTS = False, True
INSPECTION_DIR = PROJECT_DIR / ".temp/inspection"


def main(source=RUN_SOURCE, expression_id=EXPRESSION_ID, data_csv=DATA_CSV, *,
         save_plots=SAVE_PLOTS, show_plots=SHOW_PLOTS, plot_dir=None):
    """Inspect a fixed expression; regenerated figures never replace source evidence."""
    source, data_csv = Path(source).resolve(), Path(data_csv).resolve()
    selected = load_saved_expression(source, expression_id, FEATURES)
    expected_hash = selected.attrs["dataset_sha256"]
    if expected_hash and hashlib.sha256(data_csv.read_bytes()).hexdigest() != expected_hash:
        raise ValueError("Dataset differs from the curated current-reproduction fingerprint.")
    destination = Path(plot_dir or INSPECTION_DIR / expression_id).resolve()
    evidence_dir = source.parent if source.is_file() else source
    if save_plots and (destination.is_relative_to(evidence_dir)
                       or destination.is_relative_to(PROJECT_DIR / "results")):
        raise ValueError("Save regenerated figures outside the source evidence and curated results.")
    df = pd.read_csv(data_csv).dropna(subset=FEATURES + ["exclusion"])
    X, y = df[FEATURES].astype(float), pd.to_numeric(df["exclusion"], errors="raise")
    X_train, y_train, X_val, y_val, X_test, y_test, X_total, y_total = do_split(X, y)
    datasets = {"train": (X_train, y_train), "validation": (X_val, y_val),
                "test": (X_test, y_test), "total": (X_total, y_total)}
    HOF_02, evaluations = auc_recorder(selected, datasets)
    equation = HOF_02.iloc[0]["Lambda_Equation"]
    X_slice = pd.DataFrame({"mchi1": np.linspace(1, 2001, 2000), "mchipm1": 2000.0})
    fold_fig, fold_ax, fold_table, summary, _ = plot_expr_folds_variability(expression_id, datasets, evaluations)
    figures = {"roc_curve.pdf": plot_roc_curve(expression_id, evaluations, magnified=True),
               "mass_scan_1d.pdf": plot_1d_mass(equation, X_slice, Expression_ID=expression_id),
               "mass_plane.pdf": plot_mass_plane(expression_id, datasets, evaluations),
               "subset_variability.pdf": (fold_fig, fold_ax)}
    print(HOF_02[["Expression_ID", "train_auc", "val_auc", "test_auc", "total_auc"]].to_string(index=False))
    print(fold_table.to_string(), summary, sep="\n")
    for filename, (fig, _) in figures.items():
        if save_plots:
            save_plot(fig, filename, destination)
    if show_plots:
        plt.show()
    else:
        for fig, _ in figures.values():
            plt.close(fig)
    return datasets, HOF_02, evaluations


if __name__ == "__main__":
    main()
