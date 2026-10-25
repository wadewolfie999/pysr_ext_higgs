# Version v5.3.0
from pathlib import Path
from tempfile import NamedTemporaryFile
import keyword
import re
import shutil
import subprocess

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import pandas as pd
import sympy as sp
from sympy.printing.numpy import NumPyPrinter
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import roc_curve, auc

SEED = 42
VERSION = "5.3.0"
SPLITS = {"train": "train_auc", "validation": "val_auc", "test": "test_auc", "total": "total_auc"}
MASS_LABELS = {"mchi1": r"$m_{\chi_1}$ [GeV]", "mchipm1": r"$m_{\chi^\pm_1}$ [GeV]"}


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


def expr_indexer(HOF, RUN_ID, features):
    """Normalize model/CSV equations and assign RUN_ID_0{complexity} IDs."""
    features = tuple(features)
    if not re.fullmatch(r"[A-Za-z0-9_-]+", RUN_ID):
        raise ValueError("RUN_ID must contain only letters, digits, underscores, or hyphens.")
    if not features or len(set(features)) != len(features) or any(
        not name.isidentifier() or keyword.iskeyword(name) or name in {"numpy", "X"} for name in features
    ):
        raise ValueError("Provide unique Python feature names other than 'numpy' and 'X'.")
    HOF_01 = HOF.rename(columns={"complexity": "Complexity", "loss": "Loss", "equation": "Equation",
                                "sympy_format": "SymPy_Equation", "lambda_format": "Lambda_Equation"}).copy()
    if HOF_01.empty or not {"Complexity", "Loss", "Equation"}.issubset(HOF_01.columns):
        raise ValueError("Provide a nonempty HOF with Complexity, Loss, and Equation columns.")
    complexity = pd.to_numeric(HOF_01["Complexity"], errors="raise")
    if not np.isfinite(complexity).all() or (complexity < 1).any() or (complexity % 1 != 0).any():
        raise ValueError("Complexities must be positive integers.")
    if complexity.duplicated().any():
        raise ValueError("Each expression must have a unique complexity within its run.")
    HOF_01["Complexity"] = complexity.astype(int)
    HOF_01["Loss"] = pd.to_numeric(HOF_01["Loss"], errors="raise")
    HOF_01.insert(0, "Expression_ID", [f"{RUN_ID}_0{c}" for c in HOF_01["Complexity"]])
    symbols = dict(zip(features, map(sp.Symbol, features)))
    expressions, functions = [], []
    for _, row in HOF_01.iterrows():
        expr = sp.sympify(row.get("SymPy_Equation", row["Equation"]),
                          locals={**symbols, "square": lambda value: value**2}, evaluate=False)
        if {str(symbol) for symbol in expr.free_symbols} - set(features):
            raise ValueError("Expression contains symbols outside the supplied features.")
        fn = row.get("Lambda_Equation")
        if not callable(fn):
            numeric = sp.lambdify(list(symbols.values()), expr, modules="numpy")
            fn = lambda X, numeric=numeric: numeric(*(X[name].to_numpy(dtype=float) for name in features))
        expressions.append(expr)
        functions.append(fn)
    HOF_01["SymPy_Equation"], HOF_01["Lambda_Equation"] = expressions, functions
    return HOF_01


def _scores(expr_lambda, X):
    """Evaluate once and normalize constant expressions to one float per row."""
    with np.errstate(all="ignore"):
        scores = np.asarray(expr_lambda(X))
    if np.iscomplexobj(scores):
        raise ValueError("Expression must return real scores.")
    scores = scores.astype(float)
    if scores.ndim == 0:
        scores = np.full(len(X), scores.item())
    if scores.shape != (len(X),):
        raise ValueError("Expression must return a scalar or one score per row.")
    return scores


def auc_recorder(HOF_01, datasets):
    """Return HOF_02 and evaluations[Expression_ID][split]: scores, fpr, tpr, auc."""
    if set(datasets) != set(SPLITS):
        raise ValueError("Provide train, validation, test, and total datasets.")
    for name, (X, y) in datasets.items():
        labels = np.asarray(y)
        if isinstance(y, pd.Series) and not X.index.equals(y.index):
            raise ValueError(f"{name}: feature and label indices must match.")
        if (len(X) == 0 or labels.shape != (len(X),) or not np.isin(labels, [0, 1]).all()
                or np.unique(labels).size != 2 or not np.isfinite(X.to_numpy(dtype=float)).all()):
            raise ValueError(f"{name}: provide finite features and both binary labels, one per row.")
    HOF_02, evaluations = HOF_01.copy(), {}
    for _, row in HOF_01.iterrows():
        evaluated = {}
        for name, (X, y) in datasets.items():
            scores = _scores(row["Lambda_Equation"], X)
            fpr, tpr, area = None, None, np.nan
            if np.isfinite(scores).all():
                fpr, tpr, _ = roc_curve(y, scores, pos_label=1)
                area = float(auc(fpr, tpr))
            evaluated[name] = {"scores": scores, "fpr": fpr, "tpr": tpr, "auc": area}
        evaluations[row["Expression_ID"]] = evaluated
    for name, metric in SPLITS.items():
        HOF_02[metric] = [evaluations[expression_id][name]["auc"] for expression_id in HOF_02["Expression_ID"]]
    return HOF_02, evaluations


def top_three_sort(HOF_02, primary_metric="test_auc"):
    """Return up to three fully finite candidates and the winning Expression_ID."""
    if primary_metric not in SPLITS.values():
        raise ValueError(f"Unknown ranking metric: {primary_metric}")
    valid = np.isfinite(HOF_02[list(SPLITS.values())].to_numpy(dtype=float)).all(axis=1)
    HOF_03 = HOF_02.loc[valid].sort_values(primary_metric, ascending=False, kind="stable").head(3).copy()
    if HOF_03.empty:
        raise ValueError("No expression has four finite AUCs.")
    return HOF_03, HOF_03.iloc[0]["Expression_ID"]


def expr_expander(HOF_03, RUN_DIR, features):
    """Export the selected expressions as SymPy text and standalone NumPy modules."""
    rows = []
    for _, row in HOF_03.iterrows():
        folder = Path(RUN_DIR).resolve() / row["Expression_ID"]
        folder.mkdir(parents=True, exist_ok=True)
        sympy_path, lambda_path = folder / "expression_sympy.txt", folder / "expression_lambda.py"
        sympy_path.write_text(f"# Version v{VERSION}\n{row['SymPy_Equation']}\n")
        source = f"# Version v{VERSION}\nimport numpy\n\nFEATURES = {tuple(features)!r}\n\ndef predict(X):\n"
        for name in features:
            source += f"    {name} = numpy.asarray(X[{name!r}], dtype=float)\n"
        expression = NumPyPrinter().doprint(row["SymPy_Equation"])
        source += f"    return numpy.broadcast_to(numpy.asarray({expression}, dtype=float), (len(X),)).copy()\n"
        lambda_path.write_text(source)
        rows.append({**row[["Expression_ID", "Complexity", "Loss", "test_auc"]].to_dict(),
                     "SymPy": sympy_path, "Lambda": lambda_path})
    return pd.DataFrame(rows)


def expr_pdf_compiler(HOF_03, _rank_one_id, RUN_DIR):
    """Compile only the winning expression; retain TeX and compiler diagnostics on failure."""
    row = HOF_03.set_index("Expression_ID").loc[_rank_one_id]
    folder = Path(RUN_DIR).resolve() / _rank_one_id
    folder.mkdir(parents=True, exist_ok=True)
    tex, pdf = folder / "expression.tex", folder / "expression.pdf"
    expression = row["SymPy_Equation"]
    substitutions, equations = {}, []
    # Give long nested parts names so the PDF remains readable at normal size.
    for node in sp.postorder_traversal(expression):
        if node.is_Atom or node == expression or node in substitutions:
            continue
        with sp.evaluate(False):
            value = node.xreplace(substitutions)
        if len(sp.latex(value, full_prec=True)) > 100:
            symbol = sp.Symbol(f"a_{len(equations)}")
            substitutions[node] = symbol
            equations.append((symbol, value))
    with sp.evaluate(False):
        equations.append((sp.Symbol("s"), expression.xreplace(substitutions)))
    body = "\n".join(r"\exprline{" + sp.latex(left) + " = " + sp.latex(right, full_prec=True) + "}"
                     for left, right in equations)
    document = (r"\documentclass{article}" "\n"
                r"\usepackage[a4paper,landscape,margin=15mm]{geometry}" "\n"
                r"\usepackage{amsmath,graphicx}" "\n"
                r"\newcommand{\exprline}[1]{\par\noindent\begingroup\setbox0=\hbox{$\displaystyle #1$}"
                r"\ifdim\wd0>\linewidth\resizebox{\linewidth}{!}{\box0}\else\box0\fi\endgroup\par\medskip}" "\n"
                r"\begin{document}" "\n"
                + r"\noindent\texttt{" + _rank_one_id.replace("_", r"\_") + "}\\\\\n"
                + f"Version {VERSION}\\\\\n"
                + body + "\n"
                + r"\end{document}" + "\n")
    tex.write_text(document)
    compiler = shutil.which("pdflatex")
    if compiler is None:
        raise RuntimeError(f"pdflatex is required; TeX retained at {tex}")
    try:
        subprocess.run([compiler, "-interaction=nonstopmode", "-halt-on-error", tex.name],
                       cwd=folder, capture_output=True, text=True, check=True, timeout=60)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        raise RuntimeError(f"PDF compilation failed; inspect {folder / 'expression.log'}") from error
    if not pdf.is_file():
        raise RuntimeError(f"Compiler did not produce {pdf}")
    return pd.DataFrame([{"Expression_ID": _rank_one_id, "TeX": tex, "PDF": pdf}])


def run_finalizer(HOF_4_pt1, HOF_4_pt2, RUN_ID, logger_path):
    """Merge the winner and atomically update its run's repository-root CSV record."""
    logger_path = Path(logger_path).resolve()
    HOF_FINAL = HOF_4_pt1.merge(HOF_4_pt2, on="Expression_ID", validate="one_to_one")
    columns = ["Expression_ID", "Complexity", "Loss", "test_auc", "SymPy", "Lambda", "TeX", "PDF"]
    if len(HOF_FINAL) != 1 or not HOF_FINAL.iloc[0]["Expression_ID"].startswith(f"{RUN_ID}_0"):
        raise ValueError("Finalization requires exactly one winner belonging to this run.")
    for name in ["SymPy", "Lambda", "TeX", "PDF"]:
        path = Path(HOF_FINAL.iloc[0][name]).resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        HOF_FINAL[name] = path.relative_to(logger_path.parent).as_posix()
    history = pd.DataFrame(columns=columns)
    if logger_path.exists() and logger_path.stat().st_size:
        history = pd.read_csv(logger_path, float_precision="round_trip")
        if list(history.columns) != columns:
            raise ValueError("Existing logger columns do not match the winner-record format.")
        history = history.loc[~history["Expression_ID"].str.startswith(f"{RUN_ID}_0", na=False)]
    records = pd.concat([history, HOF_FINAL[columns]], ignore_index=True) if len(history) else HOF_FINAL[columns]
    temporary = None
    try:
        with NamedTemporaryFile(mode="w", dir=logger_path.parent, suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            records.to_csv(stream, index=False)
        temporary.replace(logger_path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return HOF_FINAL[columns]


def plot_roc_curve(Expression_ID, evaluations, magnified=False, *, zoom=(0.15, 0.25)):
    """Draw cached split ROC curves; optionally add a magnified panel."""
    curves = evaluations[Expression_ID]
    if not curves or any(not np.isfinite(curve["auc"]) for curve in curves.values()):
        raise ValueError("ROC plotting requires finite AUCs for every supplied split.")
    xmin, xmax = zoom
    if magnified and not (np.isfinite(zoom).all() and 0 <= xmin < xmax <= 1):
        raise ValueError("zoom must satisfy 0 <= xmin < xmax <= 1.")
    fig, axes = plt.subplots(1, 2 if magnified else 1, figsize=(12, 6) if magnified else (7, 7),
                             squeeze=False, layout="constrained")
    axes = axes[0]
    for ax in axes:
        for (name, curve), color, style in zip(curves.items(), ["#0072B2", "#CC79A7", "#D55E00", "#009E73"],
                                              ["-", "-.", "--", ":"]):
            ax.plot(curve["fpr"], curve["tpr"], color=color, linestyle=style,
                    label=f"{name}: AUC={curve['auc']:.4f}, n={len(curve['scores']):,}")
        ax.set(xlabel="False positive rate (label 1 positive)", ylabel="True positive rate",
               xlim=(0, 1), ylim=(0, 1.02), title="Full ROC")
        ax.set_box_aspect(1)
        ax.grid(alpha=0.2)
    axes[0].plot([0, 1], [0, 1], "--", color="0.6", label="Chance: AUC=0.5000")
    axes[0].legend(loc="lower right", fontsize=8)
    if magnified:
        visible = np.concatenate([np.r_[c["tpr"][(c["fpr"] >= xmin) & (c["fpr"] <= xmax)],
                                         np.interp([xmin, xmax], c["fpr"], c["tpr"])] for c in curves.values()])
        padding = max(0.15 * np.ptp(visible), 0.002)
        ymin, ymax = max(0, visible.min() - padding), min(1, visible.max() + padding)
        axes[1].set(xlim=(xmin, xmax), ylim=(ymin, ymax), title="Magnified ROC")
        axes[0].add_patch(Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, fill=False, color="#7C3AED"))
    fig.suptitle(Expression_ID)
    return fig, axes if magnified else axes[0]


def plot_1d_mass(expr_lambda, X_slice, *, scan_feature="mchi1", Expression_ID=None):
    """Evaluate an explicit fixed-input scan once, retaining undefined regions as gaps."""
    if scan_feature not in X_slice or len(X_slice) < 2 or not np.isfinite(X_slice.to_numpy(dtype=float)).all():
        raise ValueError("Provide a finite scan with at least two rows and the named scan feature.")
    scan = X_slice[scan_feature].to_numpy(dtype=float)
    fixed = X_slice.drop(columns=scan_feature)
    if not (np.diff(scan) > 0).all() or (fixed.nunique(dropna=False) != 1).any():
        raise ValueError("Scan values must increase; every other input must remain fixed.")
    scores = _scores(expr_lambda, X_slice)
    if not np.isfinite(scores).any():
        raise ValueError("No finite scores on this scan.")
    fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
    ax.plot(scan, np.where(np.isfinite(scores), scores, np.nan), color="#0072B2")
    context = ", ".join(f"{name}={fixed[name].iloc[0]:g}" for name in fixed)
    ax.set(xlabel=MASS_LABELS.get(scan_feature, scan_feature), ylabel="Raw score (uncalibrated)",
           title=f"{Expression_ID or 'Expression'} | fixed inputs: {context}")
    ax.grid(alpha=0.2)
    return fig, ax


def plot_mass_plane(Expression_ID, datasets, evaluations, metrics=("test_auc", "val_auc", "train_auc")):
    """Draw cached scores and reference labels, one row per requested split."""
    names = dict(zip(SPLITS.values(), SPLITS))
    if not metrics or any(metric not in names for metric in metrics):
        raise ValueError("Choose nonempty split metrics from train_auc, val_auc, test_auc, total_auc.")
    splits = [names[metric] for metric in metrics]
    scores = [evaluations[Expression_ID][name]["scores"] for name in splits]
    if any(not np.isfinite(values).all() or len(values) != len(datasets[name][0]) for name, values in zip(splits, scores)):
        raise ValueError("Provide finite cached scores matching every dataset row.")
    masses = [datasets[name][0].loc[:, ["mchi1", "mchipm1"]].to_numpy(dtype=float) for name in splits]
    low, high = np.concatenate(scores).min(), np.concatenate(scores).max()
    fig, axes = plt.subplots(len(splits), 2, figsize=(11, 4.5 * len(splits)), squeeze=False, layout="constrained")
    for i, (name, values, xy) in enumerate(zip(splits, scores, masses)):
        score_map = axes[i, 0].scatter(*xy.T, c=values, vmin=low, vmax=high, cmap="viridis", s=8)
        labels = np.asarray(datasets[name][1])
        for label, color, marker in [(0, "#D55E00", "o"), (1, "#0072B2", "^")]:
            axes[i, 1].scatter(*xy[labels == label].T, color=color, marker=marker, s=8, label=f"Label {label}")
        axes[i, 0].set_title(f"{name}: raw scores (n={len(xy):,})")
        axes[i, 1].set_title(f"{name}: reference labels")
        axes[i, 1].legend(fontsize=8)
        for ax in axes[i]:
            ax.set(xlabel=MASS_LABELS["mchi1"], ylabel=MASS_LABELS["mchipm1"])
            ax.set_aspect("equal", adjustable="box")
            ax.grid(alpha=0.15)
    fig.colorbar(score_map, ax=axes[:, 0].tolist(), label="Raw score (uncalibrated)", shrink=0.8)
    fig.suptitle(Expression_ID + " | observed mass pairs")
    return fig, axes


def plot_expr_folds_variability(Expression_ID, datasets, evaluations, *, dataset_name="validation", n_splits=6, seed=SEED):
    """Partition cached fixed-expression scores; no fitting or repeated evaluation."""
    X, y = datasets[dataset_name]
    labels, scores = np.asarray(y), evaluations[Expression_ID][dataset_name]["scores"]
    if (labels.shape != (len(X),) or len(scores) != len(X) or not np.isin(labels, [0, 1]).all()
            or not np.isfinite(scores).all()):
        raise ValueError("Provide matching binary labels and finite cached scores.")
    if isinstance(n_splits, bool) or not isinstance(n_splits, (int, np.integer)) or n_splits < 2:
        raise ValueError("n_splits must be an integer of at least two.")
    if np.bincount(labels.astype(int), minlength=2).min() < n_splits:
        raise ValueError("Each class must contain at least n_splits observations.")
    splitter = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    grid = np.linspace(0, 1, 1001)
    rows, curves, interpolated, positions = [], [], [], []
    for fold, (_, selected) in enumerate(splitter.split(X, labels), 1):
        fpr, tpr, _ = roc_curve(labels[selected], scores[selected], pos_label=1)
        tpr_grid = np.interp(grid, fpr, tpr)
        tpr_grid[0], tpr_grid[-1] = 0, 1
        rows.append({"subset": fold, "rows": len(selected), "auc": float(auc(fpr, tpr))})
        curves.append((fpr, tpr))
        interpolated.append(tpr_grid)
        positions.append(selected)
    fold_table = pd.DataFrame(rows).set_index("subset")
    mean, spread = np.mean(interpolated, axis=0), np.std(interpolated, axis=0, ddof=1)
    summary = {"dataset": dataset_name, "rows": len(X), "n_splits": int(n_splits), "seed": seed,
               "mean_subset_auc": float(fold_table["auc"].mean()), "sd_subset_auc": float(fold_table["auc"].std(ddof=1)),
               "area_under_mean_roc": float(auc(grid, mean))}
    fig, ax = plt.subplots(figsize=(8, 8), layout="constrained")
    for row, (fpr, tpr) in zip(rows, curves):
        ax.plot(fpr, tpr, alpha=0.6, lw=1, label=f"Subset {row['subset']}: AUC={row['auc']:.4f}, n={row['rows']}")
    ax.plot(grid, mean, color="#152f56", lw=2, label=f"Mean ROC: area={summary['area_under_mean_roc']:.4f}")
    ax.fill_between(grid, np.clip(mean-spread, 0, 1), np.clip(mean+spread, 0, 1), alpha=0.15, label="±1 SD of subset TPRs")
    ax.plot([0, 1], [0, 1], "--", color="0.5", label="Chance")
    ax.set(xlim=(0, 1), ylim=(0, 1.02), xlabel="False positive rate", ylabel="True positive rate",
           title=f"{Expression_ID} | {dataset_name} subset variability\nFixed expression; no refitting; SD is not a confidence interval")
    ax.set_box_aspect(1)
    ax.grid(alpha=0.15)
    ax.legend(loc="lower right", fontsize=8)
    return fig, ax, fold_table, summary, positions


def save_plot(fig, filename, output_dir, *, dpi=600):
    """Explicitly save a figure and a PNG companion when its filename is PDF."""
    path = Path(output_dir) / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with plt.rc_context({"pdf.fonttype": 42}):
        fig.savefig(path, dpi=dpi, bbox_inches="tight")
        if path.suffix.lower() == ".pdf":
            fig.savefig(path.with_suffix(".png"), dpi=dpi, bbox_inches="tight")
    return path
