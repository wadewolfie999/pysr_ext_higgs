
# <CAN-BE-CHANGED>
# Version v5.2.0
from pathlib import Path
import matplotlib.pyplot as plt
from sr import VERSION, plot_saved_run, plot_saved_expression_folds

PROJECT_DIR = Path(__file__).resolve().parent
RUN_DIR = PROJECT_DIR / "output/TEMP_4"
DATA_CSV = PROJECT_DIR / "data/masses_exclusions.csv"
EQUATION_INDEX = 56
PLOT_DIR = RUN_DIR / "plots" / f"v{VERSION}"
SLICE_SCAN_FEATURE = "mchi1"
SLICE_FIXED_INPUTS = {"mchipm1": 2000.0}
FOLD_DATASET, N_SPLITS, FOLD_SEED = "validation", 6, 42
SHOW_PLOTS = True

if __name__ == "__main__":
    model, datasets, equation = plot_saved_run(
        RUN_DIR, DATA_CSV, equation_index=EQUATION_INDEX, output_dir=PLOT_DIR,
        scan_feature=SLICE_SCAN_FEATURE, fixed_inputs=SLICE_FIXED_INPUTS)
    fold_fig, fold_ax, fold_scores, fold_summary, fold_positions = plot_saved_expression_folds(
        datasets, equation, dataset_name=FOLD_DATASET, n_splits=N_SPLITS,
        random_state=FOLD_SEED, run_label=RUN_DIR.name, output_dir=PLOT_DIR)
    print(fold_scores.round({"auc": 6}).to_string())
    print(fold_summary)
    if SHOW_PLOTS:
        plt.show()
# </CAN-BE-CHANGED>