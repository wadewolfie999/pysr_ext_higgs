# Version v5.2.0 — Version history at the end
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

import hashlib
import json
from sklearn.model_selection import StratifiedKFold

VERSION = "5.1.0"
SPLIT_NOTE = "Reconstructed split (seed 42)"


def _scores(expr_lambda, X):
    
    # if not isinstance(X, pd.DataFrame) or X.empty:
    #     raise ValueError("Provide a nonempty feature DataFrame.")
    # if not np.isfinite(X.to_numpy(dtype=float)).all():
    #     raise ValueError("Input features must be finite.")
    # with np.errstate(all="ignore"):
    scores = np.asarray(expr_lambda(X), dtype=float)
    if scores.ndim == 0:
        scores = np.full(len(X), scores.item())
    # if scores.shape != (len(X),):
    #     raise ValueError("Expression must return a scalar or one score per row.")
    return scores


def _plot_scores(expr_lambda, X, y):
    if isinstance(y, pd.Series) and not X.index.equals(y.index):
        raise ValueError("X and y must have matching row indices in the same order.")
    labels = np.asarray(y)
    if labels.shape != (len(X),) or not np.isin(labels, [0, 1]).all():
        raise ValueError("Provide one binary reference label per row.")
    return labels, _scores(expr_lambda, X)


def _roc_values(expr_lambda, X, y):
    labels, scores = _plot_scores(expr_lambda, X, y)
    if not np.isfinite(scores).all():
        raise ValueError("ROC requires finite scores for every row; no observations were dropped.")
    if np.unique(labels).size != 2:
        raise ValueError("ROC requires both reference labels 0 and 1.")
    fpr, tpr, _ = roc_curve(labels, scores, pos_label=1)
    return fpr, tpr, auc(fpr, tpr)



def save_plot(
    fig: Figure,
    filename: str,
    output_dir: str = "output",
    dpi: int = 600,
    *,
    save_png: bool = True,
) -> Path:
    """Save the requested figure and a high-resolution PNG companion for PDFs."""
    if isinstance(dpi, bool) or not isinstance(dpi, (int, float)) or not np.isfinite(dpi) or dpi <= 0:
        raise ValueError("dpi must be a positive finite number.")

    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    filepath = path / filename

    with plt.rc_context({"pdf.fonttype": 42}):
        fig.savefig(filepath, dpi=dpi, bbox_inches="tight")
        if save_png and filepath.suffix.lower() == ".pdf":
            fig.savefig(
                filepath.with_suffix(".png"), dpi=dpi,
                bbox_inches="tight", facecolor="white",
            )

    return filepath


def plot_expression(
    expr_lambda, X, y, key, *, output_dir: str | Path, equation_label=None,
    score_limits=None,
):
    """Compare scores and labels at observed mass pairs; return fig and score axes."""
    required = ["mchi1", "mchipm1"]
    missing = sorted(set(required) - set(X.columns))
    if missing:
        raise ValueError(f"Missing mass columns: {missing}")
    masses = X.loc[:, required].to_numpy(dtype=float)
    if not np.isfinite(masses).all():
        raise ValueError("Mass coordinates must be finite.")
    labels, scores = _plot_scores(expr_lambda, X, y)
    finite = np.isfinite(scores)
    if not finite.any():
        raise ValueError("No finite predictions are available to plot.")

    if score_limits is not None:
        low, high = score_limits
        if not (np.isfinite([low, high]).all() and low <= scores[finite].min()
                and high >= scores[finite].max()):
            raise ValueError("score_limits must be finite and cover every finite score.")
    else:
        low, high = scores[finite].min(), scores[finite].max()

    fig, axes = plt.subplots(
        1, 2, figsize=(11.8, 5.9), sharex=True, sharey=True,
        constrained_layout=True,
    )
    fig.suptitle(
        f"PySR score and reference in the mass plane - {key.capitalize()}"
        + (f"\n{equation_label}" if equation_label else ""),
        fontsize=14,
    )
    score_map = axes[0].scatter(
        masses[finite, 0], masses[finite, 1], c=scores[finite],
        cmap="viridis", vmin=low, vmax=high, s=9, linewidths=0, rasterized=False,
    )
    if not finite.all():
        axes[0].scatter(
            masses[~finite, 0], masses[~finite, 1], marker="x", s=22,
            color="#D55E00", label=f"Non-finite score: {(~finite).sum():,}",
        )
        axes[0].legend(loc="upper left", fontsize=9)
    axes[0].set_title(f"Raw score | finite: {finite.sum():,}/{len(X):,}", fontsize=11)
    colorbar = fig.colorbar(score_map, ax=axes[0], shrink=0.82, pad=0.025)
    # Keep the colour scale scalable alongside the scatter points in PDF output.
    colorbar.solids.set_rasterized(False)
    # Matching edges suppress hairline seams between vector colour cells in PDF viewers.
    colorbar.solids.set_edgecolor("face")
    colorbar.set_label("PySR score (uncalibrated)")
    colorbar.ax.tick_params(labelsize=9)

    for value, color, marker in [(0, "#D55E00", "o"), (1, "#0072B2", "^")]:
        selected = labels == value
        axes[1].scatter(
            masses[selected, 0], masses[selected, 1], color=color,
            marker=marker, s=9, linewidths=0, rasterized=False,
            label=f"Label {value} (n={selected.sum():,})",
        )
    axes[1].set_title(f"Reference labels | n={len(X):,}", fontsize=11)
    axes[1].legend(loc="lower right", framealpha=0.95, fontsize=9, markerscale=2)
    for ax in axes:
        ax.set(xlabel=r"$m_{\chi_1}$ [GeV]", ylabel=r"$m_{\chi^\pm_1}$ [GeV]")
        ax.set_aspect("equal", adjustable="box")
        ax.set_axisbelow(True)
        ax.grid(color="0.91", linewidth=0.6)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=10)
        ax.margins(0.03)
    fig.supxlabel(
        "Observed mass pairs only | "
        + ("Shared full score range" if score_limits is not None else "Full score colour range")
        + " | Scores are not probabilities",
        fontsize=10,
    )
    save_plot(fig, f"expression_{key}.pdf", output_dir=output_dir)
    return fig, axes[0]


def plot_expression_slice(
    expr_lambda, X_slice, *, output_dir: str | Path,
    scan_feature="mchi1", equation_label=None,
):
    """Plot one expression on an explicit grid with all other inputs held fixed."""
    if scan_feature not in X_slice.columns:
        raise ValueError(f"Missing scan feature: {scan_feature}")
    if len(X_slice) < 2 or not np.isfinite(X_slice.to_numpy(dtype=float)).all():
        raise ValueError("Provide at least two rows with finite input values.")
    scan = X_slice[scan_feature].to_numpy(dtype=float)
    if not (np.diff(scan) > 0).all():
        raise ValueError("Scan values must be strictly increasing.")
    fixed = X_slice.drop(columns=scan_feature)
    if (fixed.nunique(dropna=False) != 1).any():
        raise ValueError("Every input other than the scanned feature must be constant.")
    scores = _scores(expr_lambda, X_slice)
    finite = np.isfinite(scores)
    if not finite.any():
        raise ValueError("The expression has no finite values on this slice.")
    # NaN gaps preserve undefined regions instead of connecting across them.
    scores = np.where(finite, scores, np.nan)
    symbols = {"mchi1": r"m_{\chi_1}", "mchipm1": r"m_{\chi^\pm_1}",
               "mhiggs": r"m_h"}
    fixed_labels = []
    for name in fixed.columns:
        value = float(fixed[name].iloc[0])
        fixed_labels.append(
            rf"${symbols[name]} = {value:g}$ GeV" if name in symbols
            else f"{name} = {value:g}"
        )
    fig, ax = plt.subplots(figsize=(10, 5.6), constrained_layout=True)
    ax.plot(scan, scores, color="#0072B2", linewidth=1.7, label="PySR expression")
    if not finite.all():
        ax.scatter(
            scan[~finite], np.zeros((~finite).sum()),
            transform=ax.get_xaxis_transform(), color="#D55E00", marker="x",
            s=35, clip_on=False, label=f"Undefined grid scores: {(~finite).sum():,}",
        )
    xlabel = rf"${symbols[scan_feature]}$ [GeV]" if scan_feature in symbols else scan_feature
    ax.set(xlabel=xlabel, ylabel="PySR score (uncalibrated)",
           title="Fixed-input 1D slice" + (": " + "; ".join(fixed_labels) if fixed_labels else ""))
    if equation_label:
        fig.suptitle(equation_label, fontsize=12)
    ax.set_axisbelow(True)
    ax.grid(color="0.9", linewidth=0.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.margins(x=0.02, y=0.08)
    ax.legend(loc="best", fontsize=9)
    fig.supxlabel(
        f"Finite scores: {finite.sum():,}/{len(scan):,} | "
        "Fixed-input grid; no reference labels or AUC",
        fontsize=10,
    )
    save_plot(fig, "expression_slice_1d.pdf", output_dir=output_dir)
    return fig, ax


def _roc_curves(expr_lambda, X_train, y_train, X_test, y_test, X_total, y_total, validation):
    datasets = [("Training", X_train, y_train, "#0072B2", "-", "o"),
                ("Test", X_test, y_test, "#D55E00", "--", "s"),
                ("Total (descriptive)", X_total, y_total, "#009E73", ":", "^")]
    if validation is not None:
        datasets.insert(1, ("Validation", *validation, "#CC79A7", "-.", "D"))
    return [(name, len(X), *_roc_values(expr_lambda, X, y), color, style, marker)
            for name, X, y, color, style, marker in datasets]


def _draw_roc(ax, curves):
    for i, (name, size, fpr, tpr, area, color, style, marker) in enumerate(curves):
        ax.plot(fpr, tpr, label=f"{name}: AUC={area:.4f}, n={size:,}",
                color=color, linestyle=style, linewidth=1.6, marker=marker,
                markersize=4, markerfacecolor="white", markeredgewidth=1,
                markevery=(0.025 * i, 0.12))
    ax.set(xlabel="False positive rate", ylabel="True positive rate")
    ax.set_box_aspect(1)
    ax.set_axisbelow(True)
    ax.grid(color="0.91", linewidth=0.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=10)



def plot_roc(
    expr_lambda,
    X_train, y_train,
    X_test, y_test,
    X_total, y_total,
    *, output_dir: str | Path,
    validation=None, equation_label=None, split_note=None,
) -> tuple[Figure, Axes]:
    curves = _roc_curves(expr_lambda, X_train, y_train, X_test, y_test,
                         X_total, y_total, validation)
    fig, ax = plt.subplots(figsize=(7, 7), constrained_layout=True)
    _draw_roc(ax, curves)
    ax.plot([0, 1], [0, 1], color="0.6", linestyle="--", linewidth=1,
            label="Chance: AUC=0.5000")
    ax.set(title="Selected expression: ROC comparison", xlim=(0, 1), ylim=(0, 1.02),
           xlabel="False positive rate (label 1 positive)", ylabel="True positive rate")
    ax.legend(loc="lower right", fontsize=9)
    if equation_label:
        fig.suptitle(equation_label, fontsize=11)
    if split_note:
        fig.supxlabel(split_note, fontsize=9)
    save_plot(fig, "roc_comparison.pdf", output_dir=output_dir)
    return fig, ax


def plot_roc_full(
    expr_lambda,
    X_train, y_train,
    X_test, y_test,
    X_total, y_total,
    *, zoom=(0.15, 0.25), output_dir: str | Path,
    validation=None, equation_label=None, split_note=None,
):
    xmin, xmax = zoom
    if not (np.isfinite([xmin, xmax]).all() and 0 <= xmin < xmax <= 1):
        raise ValueError("zoom must satisfy 0 <= xmin < xmax <= 1.")
    curves = _roc_curves(expr_lambda, X_train, y_train, X_test, y_test,
                         X_total, y_total, validation)
    visible = np.concatenate([
        np.r_[tpr[(fpr >= xmin) & (fpr <= xmax)], np.interp([xmin, xmax], fpr, tpr)]
        for _, _, fpr, tpr, _, _, _, _ in curves
    ])
    padding = max(0.15 * np.ptp(visible), 0.002)
    ymin, ymax = max(0, visible.min() - padding), min(1, visible.max() + padding)

    fig, axes = plt.subplots(1, 2, figsize=(11.8, 6.7))
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.31, top=0.79, wspace=0.36)
    for ax in axes:
        _draw_roc(ax, curves)
    axes[0].plot([0, 1], [0, 1], color="0.6", linestyle="--", linewidth=1,
                 label="Chance: AUC=0.5000")
    axes[0].set(title="Full ROC", xlim=(0, 1), ylim=(0, 1))
    axes[1].set(title="A | Magnified region", xlim=(xmin, xmax), ylim=(ymin, ymax))
    highlight = "#7C3AED"
    axes[0].add_patch(Rectangle(
        (xmin, ymin), xmax - xmin, ymax - ymin,
        facecolor=(0.49, 0.23, 0.93, 0.07), edgecolor=highlight, linewidth=1.3,
    ))
    axes[0].annotate("A", (xmax, ymax), xytext=(5, 5), textcoords="offset points",
                     color=highlight, fontsize=11, fontweight="bold")
    arrow = ConnectionPatch(
        xyA=(1.12, 0.65), coordsA=axes[0].transAxes,
        xyB=(-0.25, 0.65), coordsB=axes[1].transAxes,
        arrowstyle="-|>", color=highlight, linewidth=1.3,
        mutation_scale=14, clip_on=False,
    )
    arrow.set_in_layout(False)
    fig.add_artist(arrow)
    fig.suptitle(
        "PySR classification: ROC performance"
        + (f"\n{equation_label}" if equation_label else ""),
        fontsize=14, y=0.96,
    )
    fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center",
               bbox_to_anchor=(0.5, 0.085), ncol=2, frameon=False, fontsize=10)
    fig.text(0.5, 0.058, "Positive class: label 1 | Same equation on every split",
             ha="center", fontsize=9)
    if split_note:
        fig.text(0.5, 0.025, split_note, ha="center", fontsize=9)
    save_plot(fig, "roc_comparison_zoom.pdf", output_dir=output_dir)
    return fig, axes


def analyze_auc(model, datasets: dict) -> pd.DataFrame:
    """Evaluate each candidate/dataset pair once, preserving saved equation indices."""
    if not datasets or model.equations_.empty:
        raise ValueError("Provide datasets and a model with saved equations.")
    rows = []
    for idx in model.equations_.index:
        row = {"eq_index": idx, "tex_expr": model.latex(index=idx),
               "sympy_expr": model.sympy(index=idx),
               "lambda_expr": model.equations_.loc[idx, "lambda_format"]}
        for name, (X, y) in datasets.items():
            _, _, row[f"{name}_AUC"] = _roc_values(
                lambda values: model.predict(values, index=idx), X, y)
        rows.append(row)
    return pd.DataFrame(rows).set_index("eq_index")


def _rank_auc(model, datasets, rank_by, top_n):
    if rank_by not in datasets:
        raise ValueError(f"Missing ranking dataset: {rank_by!r}")
    if isinstance(top_n, bool) or not isinstance(top_n, int) or top_n < 1:
        raise ValueError("top_n must be a positive integer.")
    scores = analyze_auc(model, datasets)
    ranking = scores.sort_values(f"{rank_by}_AUC", ascending=False, kind="stable")
    return {"scores": scores, "ranking": ranking, "top": ranking.head(top_n), "paths": {}}


def _write_auc_csv(result, directory):
    folder = Path(directory)
    folder.mkdir(parents=True, exist_ok=True)
    for key, filename in [("scores", "auc_scores.csv"), ("top", "top_equations.csv")]:
        result["paths"][key] = folder / filename
        result[key].to_csv(folder / filename, index_label="eq_index")
    return folder


def _report_equations(expression):
    """Introduce exact intermediate quantities instead of shrinking a long expression."""
    from sympy import Symbol, latex, postorder_traversal
    substitutions, equations = {}, []
    for node in postorder_traversal(expression):
        if node.is_Atom or node in substitutions or node == expression:
            continue
        value = node.xreplace(substitutions)
        if len(latex(value)) > 100:
            symbol = Symbol(f"a_{len(equations)}")
            equations.append((symbol, value))
            substitutions[node] = symbol
    return equations + [(Symbol("s"), expression.xreplace(substitutions))]


def _equation_report(rows, datasets, rank_by, *, exact=False):
    """Render only the supplied rows; the new reporting API supplies the winner."""
    sections = []
    for rank, (idx, row) in enumerate(rows.iterrows(), 1):
        metrics = "; ".join("{}: {:.6f}".format(name.replace("_", r"\_"), row[f"{name}_AUC"])
                            for name in datasets)
        expr = row["tex_expr"]
        if exact:
            from sympy import latex
            equations = [(latex(symbol), latex(value))
                         for symbol, value in _report_equations(row["sympy_expr"])]
        else:
            equations = [("s", expr)]
        body = "\n".join(r"\reporteq{" + left + " = " + right + "}" for left, right in equations)
        sections.append(rf"\subsection*{{Rank {rank}, equation index {idx}}}" + "\n"
                        + r"\noindent " + metrics + r"\par\medskip" + "\n" + body)
    ranking_label = rank_by.replace("_", r"\_")
    return (r"\documentclass{article}" "\n"
            r"\usepackage[a4paper,landscape,margin=20mm]{geometry}" "\n"
            r"\usepackage{amsmath,graphicx}" "\n"
            r"\newcommand{\reporteq}[1]{\par\noindent\begingroup\setbox0=\hbox{$\displaystyle #1$}" "\n"
            r"\ifdim\wd0>\linewidth\resizebox{0.98\linewidth}{!}{\box0}\else\box0\fi\endgroup\par\medskip}" "\n"
            r"\begin{document}" "\n"
            + rf"\noindent Report v{VERSION}. Selection: {ranking_label} AUC.\par" "\n"
            + r"\noindent Total AUC is descriptive. Test metrics inspected across candidates are diagnostic; "
              r"historical holdout independence is unverified.\par" "\n"
            + "\n".join(sections) + "\n" + r"\end{document}" + "\n")


def report_auc(model, datasets, *, directory, top_n=5):
    """Export all scores, validation-ranked candidates, and only the winning equation."""
    result = _rank_auc(model, datasets, "validation", top_n)
    document = _equation_report(result["top"].head(1), datasets, "validation", exact=True)
    folder = _write_auc_csv(result, directory)
    result["paths"]["report"] = folder / "equation_report.tex"
    result["paths"]["report"].write_text(document, encoding="utf-8")
    return result


def save_auc_results(model, datasets: dict, directory="output", rank_by="total", top_n=5):
    """Legacy export adapter; new callers use report_auc and validation selection."""
    result = _rank_auc(model, datasets, rank_by, top_n)
    folder = _write_auc_csv(result, directory)
    result["paths"]["table"] = folder / "equations.tex"
    result["paths"]["table"].write_text(
        model.latex_table(indices=result["top"].index.tolist()), encoding="utf-8")
    return result


def render_auc_report(model, datasets: dict, directory="output", rank_by="total",
                      top_n=5, compile_pdf=True) -> dict:
    """Legacy adapter retaining top-N rendering and optional PDF compilation."""
    compiler = shutil.which("pdflatex") if compile_pdf else None
    if compile_pdf and compiler is None:
        raise RuntimeError("PDF compilation requires pdflatex.")
    result = save_auc_results(model, datasets, directory, rank_by, top_n)
    path = Path(directory).resolve() / "equation_report.tex"
    path.write_text(_equation_report(result["top"], datasets, rank_by), encoding="utf-8")
    result["paths"]["report"] = path
    if compile_pdf:
        subprocess.run([compiler, "-interaction=nonstopmode", "-halt-on-error", path.name],
                       cwd=path.parent, check=True)
        result["paths"]["pdf"] = path.with_suffix(".pdf")
    return result



def plot_saved_expression_folds(datasets, equation, *, dataset_name="validation",
                                n_splits=6, random_state=42, run_label="Saved PySR",
                                output_dir=None):
    """Partition a named dataset and score the same fixed expression on each subset.

    This measures subset variability, not cross-validation of model fitting.
    Raw expression scores rank label 1; they need not be probabilities.
    """
    if dataset_name not in datasets:
        raise ValueError(f"Missing dataset {dataset_name!r}; available: {list(datasets)}")
    X_part, y_part = datasets[dataset_name]
    labels, scores = _plot_scores(equation["lambda_format"], X_part, y_part)
    if np.unique(labels).size != 2 or not np.isfinite(scores).all():
        raise ValueError("Subset ROC requires both binary classes and finite scores.")
    if isinstance(n_splits, bool) or not isinstance(n_splits, (int, np.integer)) or n_splits < 2:
        raise ValueError("n_splits must be an integer of at least 2.")
    counts = np.bincount(labels.astype(int), minlength=2)
    if counts.min() < n_splits:
        raise ValueError(f"Each class needs at least {n_splits} rows; counts: {counts.tolist()}")

    splitter = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    mean_fpr = np.linspace(0.0, 1.0, 1001)
    fold_positions, curves, interp_tprs, rows = [], [], [], []
    for fold, (_, positions) in enumerate(splitter.split(X_part, labels), start=1):
        fold_y, fold_scores = labels[positions], scores[positions]
        fpr, tpr, _ = roc_curve(fold_y, fold_scores, pos_label=1)
        interpolated = np.interp(mean_fpr, fpr, tpr)
        interpolated[0], interpolated[-1] = 0.0, 1.0
        fold_positions.append(positions)
        curves.append((fpr, tpr))
        interp_tprs.append(interpolated)
        rows.append({"subset": fold, "rows": len(positions),
                     "class_0": int(np.sum(fold_y == 0)), "class_1": int(np.sum(fold_y == 1)),
                     "auc": float(roc_auc_score(fold_y, fold_scores))})

    fold_table = pd.DataFrame(rows).set_index("subset")
    mean_tpr = np.mean(interp_tprs, axis=0)
    std_tpr = np.std(interp_tprs, axis=0, ddof=1)
    summary = {"dataset": dataset_name, "rows": len(labels), "seed": random_state, "n_splits": int(n_splits),
               "mean_subset_auc": float(fold_table["auc"].mean()),
               "sd_subset_auc": float(fold_table["auc"].std(ddof=1)),
               "area_under_mean_roc": float(auc(mean_fpr, mean_tpr))}

    fig, ax = plt.subplots(figsize=(8.5, 7.5))
    for row, (fpr, tpr) in zip(rows, curves):
        ax.plot(fpr, tpr, lw=1.2, alpha=0.65,
                label=f"Subset {row['subset']} (n={row['rows']}, AUC={row['auc']:.4f})")
    ax.plot([0, 1], [0, 1], linestyle="--", color="0.5", lw=1, label="Chance")
    ax.plot(mean_fpr, mean_tpr, color="#152f56", lw=2.6,
            label=f"Mean ROC (area={summary['area_under_mean_roc']:.4f})")
    ax.fill_between(mean_fpr, np.clip(mean_tpr - std_tpr, 0, 1),
                    np.clip(mean_tpr + std_tpr, 0, 1), color="#64748b", alpha=0.2,
                    label="±1 SD of subset TPRs")
    ax.set(xlim=(0, 1), ylim=(0, 1.02), xlabel="False positive rate (label 0)",
           ylabel="True positive rate (label 1)",
           title=f"{dataset_name.capitalize()} subset ROC variability — fixed expression\n"
                 f"{run_label} | equation row {equation.name} | {n_splits} subsets | seed {random_state}")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(alpha=0.15)
    ax.legend(loc="lower right", fontsize=8.5, framealpha=0.95)
    fig.text(0.5, 0.065,
             f"Subset AUC mean ± sample SD: {summary['mean_subset_auc']:.4f} ± {summary['sd_subset_auc']:.4f}",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025,
             "Fixed equation; no refitting. SD band is not a confidence interval.\n"
             "Reconstructed notebook split; original fit/holdout membership unverified.",
             ha="center", fontsize=9, color="0.35")
    fig.tight_layout(rect=(0, 0.10, 1, 1))
    if output_dir is not None:
        folder = Path(output_dir)
        save_plot(fig, "roc_subset_variability.pdf", output_dir=folder)
        fold_table.to_csv(folder / "subset_auc.csv")
        path = folder / "plot_manifest.json"
        manifest = json.loads(path.read_text()) if path.exists() else {"version": VERSION, "files": []}
        manifest["subset_variability"] = dict(summary, meaning="Fixed equation; no refitting; SD is not a confidence interval")
        manifest["files"] = list(dict.fromkeys([*manifest["files"], "roc_subset_variability.pdf",
                                              "roc_subset_variability.png", "subset_auc.csv"]))
        path.write_text(json.dumps(manifest, indent=2) + "\n")
    return fig, ax, fold_table, summary, fold_positions


def plot_saved_run(run_dir, data_csv, *, equation_index=56, output_dir=None,
                   scan_feature="mchi1", scan_values=None, fixed_inputs=None, show=False):
    """Plot one saved equation; never fit or silently choose a different candidate."""
    run_dir, data_csv = Path(run_dir), Path(data_csv)
    checkpoint = run_dir / "checkpoint.pkl"
    if not checkpoint.is_file():
        raise FileNotFoundError(f"Missing saved checkpoint: {checkpoint}")
    from pysr import PySRRegressor
    model = PySRRegressor.from_file(run_directory=run_dir)
    features = list(model.feature_names_in_)
    df = pd.read_csv(data_csv)
    missing = sorted(set(features + ["exclusion"]) - set(df.columns))
    if missing:
        raise ValueError(f"Missing CSV columns: {missing}")
    df = df.dropna(subset=features + ["exclusion"])
    X, y = df.loc[:, features].astype(float), pd.to_numeric(df["exclusion"], errors="raise")
    equation = model.get_best(index=equation_index)
    labels, scores = _plot_scores(equation["lambda_format"], X, y)
    if np.unique(labels).size != 2 or not np.isfinite(scores).all():
        raise ValueError("Saved-run ROC requires both binary classes and finite scores.")
    y = y.astype(int)
    X_train, y_train, X_val, y_val, X_test, y_test = do_split(X, y)
    datasets = {"train": (X_train, y_train), "validation": (X_val, y_val),
                "test": (X_test, y_test), "total": (X, y)}
    values = np.linspace(1, 2001, 2000) if scan_values is None else np.asarray(scan_values)
    fixed = {"mchipm1": 2000.0} if fixed_inputs is None else fixed_inputs
    if scan_feature not in features or set(features) - {scan_feature} - set(fixed):
        raise ValueError("Provide a valid scan feature and fixed values for every other model input.")
    if any(np.ndim(fixed[name]) != 0 for name in features if name != scan_feature):
        raise ValueError("Fixed model inputs must be scalar values.")
    X_slice = pd.DataFrame({name: values if name == scan_feature else fixed[name] for name in features})
    # Validate the slice before writing the observed-data figures.
    if (len(X_slice) < 2 or not np.isfinite(X_slice.to_numpy(dtype=float)).all()
            or not (np.diff(X_slice[scan_feature]) > 0).all()
            or not np.isfinite(_scores(equation["lambda_format"], X_slice)).any()):
        raise ValueError("Provide an increasing finite slice with at least one finite score.")
    folder = Path(output_dir) if output_dir is not None else run_dir / "plots" / f"v{VERSION}"
    context = f"{run_dir.name} | Equation row {equation.name} | Complexity {equation['complexity']}"
    limits = (float(scores.min()), float(scores.max()))
    for name, (inputs, target) in datasets.items():
        plot_expression(equation["lambda_format"], inputs, target, name, output_dir=folder,
                        equation_label=context, score_limits=limits)
    plot_roc_full(equation["lambda_format"], X_train, y_train, X_test, y_test, X, y,
                  validation=(X_val, y_val), output_dir=folder, equation_label=context, split_note=SPLIT_NOTE)
    _, slice_ax = plot_expression_slice(equation["lambda_format"], X_slice, output_dir=folder,
                                        scan_feature=scan_feature, equation_label=context)
    areas = {name: float(_roc_values(equation["lambda_format"], inputs, target)[2])
             for name, (inputs, target) in datasets.items()}
    manifest = {"version": VERSION, "plot_functions_version": VERSION, "run": run_dir.name,
                "equation_row": int(equation.name),
                "selection": "checkpoint model_selection" if equation_index is None else "explicit row",
                "data_csv": str(data_csv.resolve()),
                "data_sha256": hashlib.sha256(data_csv.read_bytes()).hexdigest(),
                "checkpoint_sha256": hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
                "split": {"seed": SEED, "percentages": [60, 10, 30], "status": SPLIT_NOTE},
                "sizes": {name: len(pair[0]) for name, pair in datasets.items()}, "auc": areas,
                "shared_score_limits": limits,
                "slice_1d": {"scan_feature": scan_feature, "scan_start": float(values[0]),
                             "scan_end": float(values[-1]), "grid_points": len(values),
                             "fixed_inputs": {name: float(X_slice[name].iloc[0]) for name in features if name != scan_feature},
                             "finite_scores": int(np.isfinite(slice_ax.lines[0].get_ydata()).sum()),
                             "meaning": "Constructed fixed-input slice; no labels or AUC"},
                "auc_roles": {"train": "fit diagnostic", "validation": "selection diagnostic",
                              "test": "independent only if original holdout is verified and unused for selection",
                              "total": "descriptive"},
                "export": {"png_dpi": 600, "pdf_graphics": "vector", "pdf_fonttype": 42},
                "files": [f"{stem}.{ext}" for stem in [*[f"expression_{name}" for name in datasets],
                          "roc_comparison_zoom", "expression_slice_1d"] for ext in ["pdf", "png"]]}
    (folder / "plot_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{context}\nAUC (reconstructed splits): {areas}\nSaved plots: {folder}")
    if show:
        plt.show()
    return model, datasets, equation
# </CAN-BE-CHANGED>

# --------------------------------
# Version history:
#   v0.0.1: Initialized the working script
#   v0.0.2: Revised the script, so it saves a copy of (X,y) for AUC 
#   v0.1.2: Polished Paths, more informative code                    <jumped a few versions>
#   v1.2.0: retrieved and integrated eval_auc.ipynb here
#   v1.8.0: multiplicated the code for masses_exclusions2.csv
#   v2.2.0: single py script developping...
#   v2.9.0: restructured the whole thing
#   
#   v3.0.0-t1: fixed do_split - roc-auc work was done
#   v3.0.0-t2: fixed auc analysis
#   
#   v3.0.0: almost fixed remainders - some #1111 remains - !this is before first official run!
#   v3.1.0: fixed run_id_ledger() 
#   v3.2.0: fixed plot_expression()
#   v3.3.0: fixed plot_roc() and  
#   v3.4.0: plot_roc()  massively extended it to plot_roc_full()
#   v3.4.1:
#       - fixed model.fit(X_train, y_train) -> model.fit(X_train, y_train, weights=sample_weights)
#       - fixed csv_train = "data/auc/test_ME1.csv" -> csv_train = "data/auc/train_ME1.csv"
#       - fixed copy_path either existing or creating it
#       - fixed duplication calling of Xs and ys
#       - fixed plot_roc_full() maginification and made it better
#   v3.5.0:
#       - Save all expression and ROC figures under output/<run_id>/.
#   v3.6.0:
#       - from parallelism(multithreading) -> parallelism(multiprocessing)
#   v3.6.1:
#       - rewrote PySR Regressor based on -> https://pysr.ai/v2.7.2/#detailed-example
#   V4.0.0:
#       - wrote some functions to work better, more precise, and monitorable!
#   v4.1.0:
#       - Compare scores/reference labels in the two-mass plane at observed points.
#       - Add optional validation ROC, equation context and split-provenance notes.
#       - Validate score/label alignment, constant expressions and finite ROC scores.
#   v4.2.0:
#       - Add an explicit fixed-input 1D slice alongside the observed-point mass-plane plots.
#       - Preserve undefined grid scores as gaps and label the fixed inputs and finite count.
#   v4.3.0:
#       - Export scalable PDF scatter/colourbar graphics with embedded TrueType fonts.
#       - Save 600 DPI PNG companions through save_plot(), retaining its Path return.
#
#   START OF V5
#  - Codex or any other AI/LLM must NOTE that throughout all repo, in scripts or notebooks, ONLY the codeblock enapsulated with `# <CAN-BE-CHANGED>` and `# </CAN-BE-CHANGED>`
#
#   v5.0.0-t1: sr.py -> broken down to three files
#                   1. sr.py           ----------------------------> only holding all functions for this codebase
#                   2. main.py         ----------------------------> only holding the main function, 
#                   1. plot_sr.py      ----------------------------> responsible for generating plots
#                
#                   REMAINING TO DO:
#                       - rewrite the code in `plot.ipynb` into `post_sr.py`
#                       - sr.py - The codeblock  `# <CAN-BE-CHANGED>` and `# </CAN-BE-CHANGED>`:
#                           - needs to be seriously reduced and `post_sr.py` making correct function import calls to this
#                       - main.py - The codeblock  `# <CAN-BE-CHANGED>` and `# </CAN-BE-CHANGED>`:
#                           - I feel like the functions save_auc_results & render_auc_report & ... in sr.py can be compacted
#   # v5.1.0: shared plotting workflow and validation-ranked AUC reporting.
#   