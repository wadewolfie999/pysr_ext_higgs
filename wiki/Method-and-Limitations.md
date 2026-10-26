# Methods and limitations

How the project trains symbolic classifiers and interprets their results. For commands, use the **[README](https://github.com/wadewolfie999/pysr_ext_higgs#how-to-run-this-on-your-machine)**; for scores and figures, use **[Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry)**.

[Inputs and objective](#inputs-and-objective) · [Evaluation and selection](#evaluation-and-selection) · [Diagnostic plots](#diagnostic-plots) · [Reproducibility](#reproducibility)

## Inputs and objective

| Component | Current workflow |
|---|---|
| Input features | `mchi1` and `mchipm1`, in GeV |
| Reference target | Binary `exclusion` labels, 0 and 1 |
| Training objective | `L2HingeLoss()` |
| Training targets | Signed labels, `2*y - 1`, giving -1 and +1 |
| Sample weights | Balanced by class, using training rows only |
| Evaluation | ROC-AUC from continuous scores, with label 1 positive |

Squared hinge loss is `max(0, 1 - y*s)**2`, for signed target `y` and score `s`.

**The expression returns a raw score.** Negative values are valid, and the score is not a calibrated probability. No additional physical meaning is assigned here to the reference labels.

*`L2HingeLoss()` is the chosen objective; the selected result alone does not establish that it is statistically superior to other losses.* See the [PySR loss documentation](https://github.com/astroautomata/PySR/blob/master/docs/src/options.md#loss) and [LossFunctions.jl margin definitions](https://juliaml.github.io/LossFunctions.jl/stable/losses/margin/).

## Evaluation and selection

The current reproduction uses **12,280 rows**, split by `do_split()` with stratification and **seed 42**:

| Partition | Share | Rows |
|---|---:|---:|
| Training | 60% | 7,368 |
| Validation | 10% | 1,228 |
| Test | 30% | 3,684 |

### What the reported validation means

The validation score in Project Registry evaluates the **fixed saved expression** on the reconstructed validation partition. Original split membership is unknown, so this is a current reproduction rather than an authenticated historical validation result.

### How the expression was selected

`top_three_sort()` ranks candidate expressions by **test AUC**. That score participates in expression selection and **is not an untouched final-test estimate**. Reproducing the recorded value does not make the test partition independent of selection. The all-row AUC is descriptive.

An independent final assessment would require data held out from expression selection.

## Diagnostic plots

These plots answer different questions:

| Plot | What it shows |
|---|---|
| **ROC curve** | Ranking of the binary reference labels by continuous expression scores |
| **Mass plane** | Scores beside reference labels at observed mass pairs |
| **One-dimensional mass scan** | Raw expression behaviour as `mchi1` varies with `mchipm1` fixed at 2000 GeV |
| **Validation subset variability** | One fixed expression evaluated across six validation subsets; no refitting |
| **Fitted validation curve** | Fresh child models at different configured complexity limits |
| **Fitted learning curve** | Fresh child models using different training-set sizes |

**Subset variability is descriptive.** Its standard-deviation band is not a confidence interval, and the procedure is not refitted cross-validation.

**Fitted curves run new searches.** They use PySR's `model_selection='best'` for child-model predictions, separately from the parent expression selected by test AUC. One fit per point gives no repeated-fit uncertainty estimate; multithreaded searches are not guaranteed to repeat identically.

In `plot.ipynb`, set **`RUN_CURVE_FITS = False`** for saved-result inspection. Enabling it requires the original local checkpoint and saves fresh diagnostics under `output/curve_diagnostics/`. The preserved curve image's historical numerical result tables are unavailable.

## Reproducibility

- **Saved expression:** The committed manifest records the current reproduction and artifact checksums. It does not recover missing historical split membership or generating-commit provenance.
- **New runs:** Before fitting, `main.py` records row IDs, labels, weights, model parameters, dataset hash, package versions, and source hashes in `run_metadata.json`. These records apply to that new run.
- **Published files:** Binary artifacts are served from versioned paths at `logs.reshub.lol`. Explicit downloads are checked against the committed manifest; raw logs, checkpoints, environment files, and backups remain local.
- **Environment:** The inspected Mac environment uses Python **3.13.7** and PySR **2.7.0**. The restored installation instructions have not been tested on a fresh machine in this revision.

The dataset fingerprint, exact scores, export label, and saved files are collected in [Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry#expression-downloads).

---

[Wiki Home](https://github.com/wadewolfie999/pysr_ext_higgs/wiki) · [Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry) · [README](https://github.com/wadewolfie999/pysr_ext_higgs#readme)

<sub>Page v0.4.0 · Code release v5.7.0 · Updated 2026-10-26.</sub>
