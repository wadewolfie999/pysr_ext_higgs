# Version v5.3.0-ATTEMPT1 — Version history at the end
import pandas as pd
import numpy as np
import shutil
import subprocess
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.patches import Rectangle, ConnectionPatch
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve, auc, RocCurveDisplay


SEED = 42
VERSION = "5.3.0"

def run_id_ledger():
    counter_file = Path(".run_id_counter")

    while True:
        i = int(counter_file.read_text()) + 1 if counter_file.exists() else 1

        counter_file.write_text(str(i))

        yield i


# splitting made easy
def do_split(X, y, train_p=60, val_p=10, test_p=30, seed=SEED):
    if (train_p + val_p + test_p)!=100:
        raise ValueError 
    # Calculate splitting ratios
    test_size_1 = (val_p + test_p) / 100
    test_size_2 = test_p / (val_p + test_p)

    # Stage 1: Training + Remaining
    X_train, X_rest, y_train, y_rest = train_test_split(
        X, y,
        test_size=test_size_1,
        stratify=y,
        random_state=seed,
    )
    # Stage 2: Validation + Testing
    X_val, X_test, y_val, y_test = train_test_split(
        X_rest, y_rest,
        test_size=test_size_2,
        stratify=y_rest,
        random_state=seed,
    )
    X_total, y_total = X, y
    return X_train, y_train, X_val, y_val, X_test, y_test, X_total, y_total

# <CAN-BE-CHANGED>

"""
building on -> model.equations_ or hall_of_fame.csv returned by the pysr model training
    - Calling it: HOF
        contains:
            | Complexity | Loss | Equation |
        I assume the equation is already Lambda format.
    - in the main.py; i'll write for now, HOF = model.equations_
    - and as HOF passes down the functions below, it gets counter!
"""

def expr_indexer(HOF):
    """
    uniquely indexes: every expression in HOF
    
    calls this index -> "Expression_ID" 
        Expression_ID = RUN_ID_0{complexity_of_expression}
    
    returns: pd.DataFrame 
        HOF_01 containing:
            | Expression_ID | Complexity | Loss | Equation |
    """
    pass


def auc_recorder(HOF_01, do_sort=True):
    """
    records the four auc corresponding to:
        datasets = {"train": (X_train, y_train), "validation": (X_val, y_val),
                    "test": (X_test, y_test), "total": (X_total, y_total)}
    
        i.e.: for every expression available
            train_auc = (y_train, y_pred(X_train), 
            val_auc = (y_val, y_pred(X_val)), 
            test_auc = (y_test, y_pred(X_test)) 
            total_auc = (y_total, y_pred(X_total))
                
    outputs: pd.DataFrame 
        HOF_02 containing:
            Expression_ID | Complexity | Loss | Lambda_Equation  | train_auc | val_auc | test_auc | total_auc |

    """
    pass


def top_three_sort(HOF_2,primary_metric="test_auc"):
    """
        outputs: HOF_3

            Sort by Highest test_auc, 
            and show the top 3 entry. 
            containing:
            Expression_ID | Complexity | Loss | Lambda_Equation  | test_auc | val_auc | train_auc | total_auc |
            but trimmed to top 3 entry.

    Expression_ID of NUMBER ONE -> call it "_rank_one_id"
    """
    pass

def expr_expander(HOF_3, _rank_one_id):
    """
;
    saves the 2 version (sympy, lambda) in 2 designated files:
        - in directory: RUN_DIR / Expression_ID /
            - RUN_DIR  <----- from `main.py`: RUN_DIR = Path("output") / RUN_ID
        - and stores the path to 2 versions
    outputs: HOF_4_pt1
        containing:
            Expression_ID | Complexity | Loss | test_auc | SymPy: {file_url_in_repo} | Lambda: {file_url_in_repo} | 
    """
    pass


def expr_pdf_compiler(_rank_one_id):
    """
    for the Expression_ID of NUMBER ONE expression in HOF_03;
    creates/compiles/saves the (TeX, PDF) version of expression in 2 designated files:
        - in directory: RUN_DIR / Expression_ID /
            - RUN_DIR  <----- from `main.py`: RUN_DIR = Path("output") / RUN_ID
        - and stores the path to 2 versions
    outputs: HOF_4_pt2
        containing:
        Expression_ID | TeX: {file_url_in_repo} | PDF: {file_url_in_repo} |
    """
    pass



def run_finalizer(HOF_4_pt1, HOF_4_pt2):
    """
    merges: HOF_4_pt1 and HOF_4_pt2
    outputs: HOF_FINAL -> there's a file at root of repo -> .run_num1_logger.csv
     - containing:
        Expression_ID | Complexity | Loss | test_auc | SymPy: {file_url_in_repo} | Lambda: {file_url_in_repo} | TeX: {file_url_in_repo} | PDF: {file_url_in_repo} 
    and can write this array to anywhere i want
    """
    pass



def plot_roc_curve(Expression_ID:str=_rank_one_id, magnified=False):
    # This function should plot per expression_id as usual
    # in main.py, its entry point should set to _rank_one_id
    # plot its magnified performance if magnified=True
    pass


def plot_1d_mass(Expression_ID:str=_rank_one_id):
    # This function should plot per expression_id as usual
    # in main.py, its entry point should set to _rank_one_id
    pass



def plot_mass_plane(metrics=["test_auc", "val_auc", "train_auc"], Expression_ID:str=_rank_one_id):
    # This function should plot per expression_id as usual
    # in main.py, its entry point should set to _rank_one_id
    pass

# fixed-expression subset variability, without refitting
def plot_expr_folds_variability():
    """
    same as below, but translated to function coding and algorithm
    """
    # fold_fig, fold_ax, fold_scores, fold_summary, fold_positions = plot_saved_expression_folds(
    #     datasets, equation, dataset_name=FOLD_DATASET, n_splits=N_SPLITS,
    #     random_state=FOLD_SEED, run_label=RUN_DIR.name, output_dir=PLOT_DIR)


# <CAN-BE-CHANGED>