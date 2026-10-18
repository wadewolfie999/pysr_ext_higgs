# Version 3.5.0 — Version history at the end
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, ConnectionPatch
from pathlib import Path
from pysr import PySRRegressor#, TensorBoardLoggerSpec
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.metrics import roc_auc_score, roc_curve, auc, RocCurveDisplay
from sympy import true




SEED = 42



def run_id_ledger():
    counter_file = Path(".run_id_counter")

    while True:
        i = int(counter_file.read_text()) + 1 if counter_file.exists() else 1

        counter_file.write_text(str(i))

        yield i


def set_df(dataset_path: str) -> pd.DataFrame:
    df = pd.read_csv(dataset_path)
    return df


# splitting made easy #1111 needs function return definition
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

    return X_train, y_train, X_val, y_val, X_test, y_test

def do_auc_split():

    csv_test = "data/auc/test_ME1.csv"
    csv_train = "data/auc/train_ME1.csv"
    csv_total = "data/masses_exclusions.csv"
    df_test, df_train , df_total = set_df(csv_test), set_df(csv_train), set_df(csv_total)
    y_test = df_test.pop("exclusion")
    X_test = df_test

    y_train = df_train.pop("exclusion")
    X_train = df_train

    y_total = df_total.pop("exclusion")
    X_total = df_total

    return X_test, y_test, X_train, y_train, X_total, y_total



def save_plot(
    fig: plt.Figure,
    filename: str,
    output_dir: str = "output",
    dpi: int = 300
) -> Path:

    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    filepath = path / filename

    fig.savefig(
        filepath,
        dpi=dpi,
        bbox_inches="tight"
    )

    return filepath

def plot_expression(expr_lambda, X, y, key, *, output_dir="output"):
    with np.errstate(all="ignore"):
        prediction = np.broadcast_to(
            np.asarray(expr_lambda(X), dtype=float), (len(X),)
        )
    prediction = np.where(np.isfinite(prediction), prediction, np.nan)

    fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)

    ax.scatter(
        X["mchi1"], prediction,
        s=12, color="#2563EB", alpha=0.45,
        edgecolors="none", label="PySR prediction", zorder=2,
    )
    ax.scatter(
        X["mchi1"], y,
        s=24, facecolors="none", edgecolors="#D97706",
        linewidths=0.8, alpha=0.6, label="Reference label", zorder=3,
    )

    ax.set(
        xlabel=r"$m_{\chi_1}$ [GeV]",
        ylabel="Reference label / PySR score",
        title=f"PySR prediction and reference — {key.capitalize()}",
    )
    ax.title.set_fontsize(14)
    ax.xaxis.label.set_fontsize(12)
    ax.yaxis.label.set_fontsize(12)
    ax.tick_params(labelsize=11)
    ax.set_axisbelow(True)
    ax.grid(color="0.9", linewidth=0.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.margins(x=0.02, y=0.08)
    ax.legend(
        loc="best", frameon=True, facecolor="white",
        edgecolor="0.85", framealpha=0.95, markerscale=1.5,
    )
    save_plot(fig, f"expression_{key}.pdf", output_dir=output_dir)
    #plt.show()
    return fig, ax


def plot_roc(
    expr_lambda, X_train, y_train, X_test, y_test, X_total, y_total,
    *, output_dir="output",
):
    fig, ax = plt.subplots(figsize=(6, 6), constrained_layout=True)

    for name, X, y, color, style in [
        ("Training", X_train, y_train, "#2563EB", "-"),
        ("Test", X_test, y_test, "#D97706", "--"),
        ("Total", X_total, y_total, "#059669", ":"),
    ]:
        display = RocCurveDisplay.from_predictions(
            y, expr_lambda(X),
            pos_label=1, name=name, ax=ax,
        )
        display.line_.set_label(f"{name} (AUC = {display.roc_auc:.4f})")

    ax.plot(
        [0, 1], [0, 1],
        color="0.5", linestyle="--", linewidth=1.2,
        label="Chance (AUC = 0.5000)",
    )
    ax.set(
        title="Selected expression: ROC comparison",
        xlabel="False positive rate",
        ylabel="True positive rate",
        xlim=(0, 1),
        ylim=(0, 1.02),
    )
    ax.set_aspect("equal")
    ax.set_axisbelow(True)
    ax.grid(color="0.9", linewidth=0.7)
    ax.tick_params(labelsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="lower right", framealpha=0.95)
    save_plot(fig, "roc_comparison.pdf", output_dir=output_dir)
    #plt.show()
    return fig, ax



def plot_roc_full(
    expr_lambda,
    X_train, y_train,
    X_test, y_test,
    X_total, y_total,
    *,
    zoom=(0.15, 0.25),
    output_dir="output"
):
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5))
    fig.subplots_adjust(
        left=0.07, right=0.98,
        bottom=0.23, top=0.82, wspace=0.38,
    )

    datasets = [
        ("Training", X_train, y_train, "#0072B2", "-",  "o"),
        ("Test",     X_test,  y_test,  "#D55E00", "--", "s"),
        ("Total",    X_total, y_total, "#009E73", ":",  "^"),
    ]

    curves = []
    for i, (name, X, y, color, style, marker) in enumerate(datasets):
        fpr, tpr, _ = roc_curve(y, expr_lambda(X), pos_label=1)
        curves.append((fpr, tpr))

        for ax in axes:
            ax.plot(
                fpr, tpr,
                label=f"{name} (AUC = {auc(fpr, tpr):.6f})",
                color=color, linestyle=style, linewidth=1.6,
                marker=marker, markersize=5,
                markerfacecolor="white", markeredgewidth=1.1,
                markevery=(0.025 * i, 0.12),
            )

    # Fit the vertical zoom limits to all curves in the chosen FPR interval.
    xmin, xmax = zoom
    visible = np.concatenate([
        np.r_[
            tpr[(fpr >= xmin) & (fpr <= xmax)],
            np.interp([xmin, xmax], fpr, tpr),
        ]
        for fpr, tpr in curves
    ])
    padding = max(0.15 * np.ptp(visible), 0.002)
    ymin = max(0, visible.min() - padding)
    ymax = min(1, visible.max() + padding)

    axes[0].plot(
        [0, 1], [0, 1],
        color="0.6", linestyle="--", linewidth=1, label="Chance",
    )
    axes[0].set(title="Full ROC", xlim=(0, 1), ylim=(0, 1))
    axes[1].set(
        title="A · Magnified region",
        xlim=(xmin, xmax), ylim=(ymin, ymax),
    )

    for ax in axes:
        ax.set(
            xlabel="False positive rate",
            ylabel="True positive rate",
        )
        ax.set_box_aspect(1)
        ax.set_axisbelow(True)
        ax.grid(color="0.91", linewidth=0.7)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=10)

    highlight = "#7C3AED"
    axes[0].add_patch(Rectangle(
        (xmin, ymin), xmax - xmin, ymax - ymin,
        facecolor=(0.49, 0.23, 0.93, 0.07),
        edgecolor=highlight, linewidth=1.3, zorder=5,
    ))
    axes[0].annotate(
        "A", (xmax, ymax),
        xytext=(5, 5), textcoords="offset points",
        color=highlight, fontsize=11, fontweight="bold",
    )

    # Keep the directional arrow in the gap, away from both curves.
    arrow = ConnectionPatch(
        xyA=(1.15, 0.65), coordsA=axes[0].transAxes,
        xyB=(-0.28, 0.65), coordsB=axes[1].transAxes,
        arrowstyle="-|>", color=highlight,
        linewidth=1.3, mutation_scale=14, clip_on=False,
    )
    arrow.set_in_layout(False)
    fig.add_artist(arrow)

    fig.suptitle(
        "PySR Classification: ROC Performance",
        fontsize=15, y=0.96,
    )
    fig.legend(
        *axes[0].get_legend_handles_labels(),
        loc="lower center", bbox_to_anchor=(0.5, 0.035),
        ncol=2, frameon=False, fontsize=10,
    )
    save_plot(fig, "roc_comparison_zoom.pdf", output_dir=output_dir)
    #plt.show()
    return fig, axes


def main() -> None:

    run_id = run_id_ledger()
    value = next(run_id)
    RUN_ID = f"RUN_{value}"
    plot_dir = Path("output") / RUN_ID / "plots"
    plot_dir.mkdir(parents=True, exist_ok=True)

    total_ME1 = "data/masses_exclusions.csv"
    df = set_df(total_ME1)
    
    features = ["mchi1","mchipm1"]
    target = "exclusion"
    
    df = df.dropna(subset=features + [target])
    
    X = df[features].astype(float)
    y = df[target].astype(int)
    X_train, y_train, X_val, y_val, X_test, y_test = do_split(X,y)
    X_total, y_total = X, y
    # Save a copy for later use
    cp_path = Path("data/auc")
    cp_path.mkdir(parents=True, exist_ok=True)
    test_ME1 = X_test.copy()
    test_ME1["exclusion"] = np.asarray(y_test)
    test_ME1.to_csv(cp_path / "test_ME1.csv", index=False)

    train_ME1 = X_train.copy()
    train_ME1["exclusion"] = np.asarray(y_train)
    train_ME1.to_csv(cp_path / "train_ME1.csv", index=False)

    
    sample_weights = compute_sample_weight(class_weight="balanced", y=y_train)

    model = PySRRegressor(
        niterations=600,
        parallelism="multithreading",
        populations=36,         # Increase populations to 3*num_cores
        maxsize=40,
        binary_operators=["+", "-", "*", "/"],
        unary_operators=["square", "cube", "sqrt", "exp", "log", "sin", "cosh", "inv"],
        output_directory="output/",
        run_id=RUN_ID,
        #use_tracing=True,
        #tracing_file=f"{TEMP_DIR}/trace-03.jsonl",
        #parsimony=1e-4,
        #adaptive_parsimony_scaling=700,
        #logger_spec=logger_spec,
        #precision=64,
        #warm_start=True               # to continue where left off 
    )
    model.fit(X_train, y_train, weights=sample_weights)

    # auc analysis
    model_df = model.equations_

    test_auc_results = []
    train_auc_results = []
    total_auc_results = []

    
    for eq_index in model_df.index:
        pred_y_test = model.predict(X_test, index=eq_index)
        pred_y_train = model.predict(X_train, index=eq_index)
        pred_y_total = model.predict(X_total, index=eq_index)
        test_auc = roc_auc_score(y_test, pred_y_test)
        train_auc = roc_auc_score(y_train, pred_y_train)
        total_auc = roc_auc_score(y_total, pred_y_total)
        test_auc_results.append({
            "test_AUC"  : test_auc
        })
        train_auc_results.append({
            "train_AUC"  : train_auc
        })
        total_auc_results.append({
            "total_AUC"  : total_auc
        })
    

    test_auc_df = pd.DataFrame(test_auc_results, index=model_df.index)
    train_auc_df = pd.DataFrame(train_auc_results, index=model_df.index)
    total_auc_df = pd.DataFrame(total_auc_results, index=model_df.index)

    
    sorted_test_auc_df = test_auc_df.sort_values("test_AUC",ascending=False)
    sorted_train_auc_df = train_auc_df.sort_values("train_AUC",ascending=False)
    sorted_total_auc_df = total_auc_df.sort_values("total_AUC",ascending=False)
    print(sorted_test_auc_df.head())
    print(sorted_train_auc_df.head())
    print(sorted_total_auc_df.head())
    # Winner Expression of each auc
    _w_index_test  = sorted_test_auc_df.index[0]
    _w_index_train = sorted_train_auc_df.index[0]
    _w_index_total = sorted_total_auc_df.index[0]
    # print(model.equations_.iloc[_h_index])
    # sympy_eq_ = model.sympy(index=_h_index) # sympy expr
    # latex_eq_ = model.latex(index=_h_index) # latex expr
    expr_lambda_test = model_df.loc[_w_index_test, "lambda_format"]
    expr_lambda_train = model_df.loc[_w_index_train, "lambda_format"]
    expr_lambda_total = model_df.loc[_w_index_total, "lambda_format"]

    # Printing winner expression - Lambda format
    for key in ["test", "train", "total"]:
        if key=="test":
            print(f"based on {key} data, \nthe winner lambda_expr is: {expr_lambda_test}")
        elif key=="train":
            print(f"based on {key} data, \nthe winner lambda_expr is: {expr_lambda_train}")
        else:
            print(f"based on {key} data, \nthe winner lambda_expr is: {expr_lambda_total}")
            

    # expression Plots
    plot_expression(
        expr_lambda_total, X_total, y_total,
        key="total", output_dir=plot_dir,
    )
    plot_expression(
        expr_lambda_test, X_test, y_test,
        key="test", output_dir=plot_dir,
    )
    plot_expression(
        expr_lambda_train, X_train, y_train,
        key="train", output_dir=plot_dir,
    )

    fig, ax = plot_roc(
        expr_lambda_total,
        X_train, y_train,
        X_test, y_test,
        X_total, y_total,
        output_dir=plot_dir,
    )

    fig, axes = plot_roc_full(
        expr_lambda_total,
        X_train, y_train,
        X_test, y_test,
        X_total, y_total,
        zoom=(0.63, 0.83),
        output_dir=plot_dir,
    )

    

if __name__ == "__main__":
    main()

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
#        - fixed model.fit(X_train, y_train) -> model.fit(X_train, y_train, weights=sample_weights)
#        - fixed csv_train = "data/auc/test_ME1.csv" -> csv_train = "data/auc/train_ME1.csv"
#        - fixed copy_path either existing or creating it
#        - fixed duplication calling of Xs and ys
#        - fixed plot_roc_full() maginification and made it better
#   v3.5.0:
#        - Save all expression and ROC figures under output/<run_id>/.
