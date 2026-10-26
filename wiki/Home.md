# PySR classification research

**Wiki revision v0.4.1 · Code release v5.7.0 · Updated 2026-10-26.** This catalogue contains the four retained expressions and supersedes the earlier results catalogue.

Symbolic regression learns an explicit raw score from the mass features `mchi1` and `mchipm1`, in GeV, for the dataset's binary reference labels in `exclusion`.

**Earlier results withdrawn.** The owner has withdrawn every result outside the four retained expression IDs. Earlier published artifacts remain in Git history: [17-expression HP catalogue](https://github.com/wadewolfie999/pysr_ext_higgs/tree/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results) and [historical TEMP_6_038 snapshot](https://github.com/wadewolfie999/pysr_ext_higgs/tree/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038).

The owner reports that an omitted `elementwise_loss` left earlier work using PySR's default squared-error objective, rather than the intended margin-classification objective. This is the owner's reason for withdrawal; the cause has not been authenticated separately for every historical run. Negative raw scores alone do not falsify a classifier's ranking. `L2HingeLoss()` is the owner's preferred loss for current work, not a demonstrated statistically superior objective.

## Start here

- [Retained results and downloads](Project-Registry).
- [Method, withdrawal rationale, and limitations](Method-and-Limitations).
- [Repository setup and saved-result inspection](https://github.com/wadewolfie999/pysr_ext_higgs/blob/main/README.md).

Exactly four selected expressions remain in the active catalogue: `EXP_6_072`, `ELEM_7_0198`, `L2HL_1_050`, and `L2HL_2_0235`. The default saved-result view is `L2HL_1_050`; both L2HL entries include their preserved validation/learning curve image.

Test AUC remains a selection score. The six fixed-expression validation subsets involve no refitting. The separate fitted curves use new diagnostic models and PySR's own expression-selection rule. The current results do not establish statistical superiority of one loss or independent predictive performance.

## Workflow

1. Inspect tracked saved evidence using `plot_sr.py` or the notebook; no local checkpoints are required for this default path.
2. Use `main.py` only when deliberately starting a new search. Future-run metadata captures the actual configuration and split identities before fitting.
3. Keep the notebook's `RUN_CURVE_FITS = False` for ordinary inspection. Enabling it deliberately launches new searches into fresh ignored directories.
4. Curate selected artifacts into the versioned results package; keep raw runs and checkpoints local.

The editable publication sources live in the repository's `wiki/` directory. Curated files are published at [logs.reshub.lol](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/), using immutable versioned paths. Binary files are ignored local cache; source revisions remain in Git. Ordinary offline inspection uses the retained candidate tables and dataset, without automatic downloads.

<sub>Page v0.4.1 · Previous v0.4.0 · Code release v5.7.0 · Retained batch v0.1.0.</sub>
