# Method and limitations

**Page v0.2.1 · Code release v5.7.0 · Updated 2026-10-26.**

## Why earlier results were withdrawn

**Earlier results withdrawn.** The owner has withdrawn every result outside the four retained expression IDs. Earlier published artifacts remain in Git history: [17-expression HP catalogue](https://github.com/wadewolfie999/pysr_ext_higgs/tree/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results) and [historical TEMP_6_038 snapshot](https://github.com/wadewolfie999/pysr_ext_higgs/tree/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038).

The owner reports that an omitted `elementwise_loss` left earlier work using PySR's default squared-error objective, rather than the intended margin-classification objective. This is the owner's reason for withdrawal; the cause has not been authenticated separately for every historical run. Negative raw scores alone do not falsify a classifier's ranking. `L2HingeLoss()` is the owner's preferred loss for current work, not a demonstrated statistically superior objective.

The active list contains the four selected expressions in [Project Registry](Project-Registry). The withdrawal is an owner decision about the research protocol. Historical values and files remain records of those earlier outputs; this revision does not replace them with invented results or authenticate a cause for each historical run.

## Loss, labels, and raw scores

PySR's default elementwise objective is `L2DistLoss()`, squared error. A classification experiment can explicitly choose a margin loss. The current training entry point selects `L2HingeLoss()` and maps reference labels `0, 1` to signed training targets `-1, +1` using `2*y-1`.

For signed target `y` and raw score `s`, squared hinge loss is `max(0, 1-y*s)**2`. `LogitMarginLoss()` uses `log(1+exp(-y*s))`. Agreement depends on the sign and magnitude of the margin. Negative scores are therefore valid; neither margin score is automatically a calibrated probability. Squared-error training alone does not prove a binary ranking is invalid. [PySR loss documentation](https://github.com/astroautomata/PySR/blob/master/docs/src/options.md#loss), [LossFunctions.jl margin definitions](https://juliaml.github.io/LossFunctions.jl/stable/losses/margin/).

Weights are balanced using the training rows only. ROC evaluation retains labels 0 and 1, with label 1 positive, and uses continuous scores without thresholding. No physical interpretation of those reference labels is added by this cleanup.

The saved checkpoint settings identify `LogitMarginLoss()` for `EXP_6` and `ELEM_7`, and `L2HingeLoss()` for the two L2HL parents. The checkpoints were inspected for simple configuration literals without executing their pickle contents. Their full historical generating source and original split membership remain unverified.

## Selection and interpretation

The owner explicitly retains **test-AUC expression selection**. `top_three_sort()` selects by `test_auc`, and no retained winner is reranked during cleanup. Test AUC is therefore a selection score, not an independent final-test estimate. Total AUC is descriptive. A newly reconstructed split does not restore untouched-test status.

`L2HingeLoss()` is the owner's preferred objective. The current table, differing search settings, and two diagnostic images do not establish statistical superiority of that loss. Objective values from different loss functions should not be compared directly.

## Three diagnostics with different meanings

| Diagnostic | What changes | What it supports |
|---|---|---|
| Fixed-expression subset variability | Validation rows are partitioned into six subsets; the expression stays fixed | Descriptive variability across these subsets; no fitting, refitted cross-validation, or confidence interval |
| Fitted validation curve | Fresh models use maxsize 10, 15, 20, 25 on the training split | Dependence on complexity limit for these single diagnostic fits |
| Fitted learning curve | Fresh models use 25%, 50%, 75%, 100% of training rows, with maxsize 280 | Dependence on training-set size for these single diagnostic fits |

The fitted child models use PySR's own `model_selection='best'` and default `predict()` choice. That is separate from the parent expression chosen by test AUC. The subset seed controls stratified sampling; the saved configurations use multithreading without a deterministic search seed. Repeating the search need not reproduce the same curve. Neither fitted curve is a direct evaluation of the frozen parent winner, and there are no repeated-fit uncertainty estimates.

The two preserved curve images have eight recovered child IDs each. Their numerical result arrays were not serialized. The manifests retain this gap explicitly; no points have been estimated from pixels. New explicitly enabled curve runs save tables, child settings, selected expressions, row IDs, signed labels, weights, and status in a fresh ignored directory.

## Provenance boundaries

The current fingerprinted dataset has 12,280 rows. The shared `do_split()` is unchanged: stratified 60%/10%/30% train/validation/test, seed 42. Current reproduction matches all four recorded test AUCs and the exported NumPy predictions exactly. Reconstructed row IDs are stored separately from historical provenance.

For future training, `run_metadata.json` is written before fitting with the actual row IDs, label mapping, weights, complete available model parameters, dataset hash, package versions, and source hashes. This does not backfill metadata for the four retained runs.

Curated `files[].path` values resolve relative to their containing manifest. Original `source_path` values and the logger's `output/...` strings resolve from the repository root and may name ignored files absent from a fresh clone. Portable inspection uses curated mappings and checks the candidate-table and dataset fingerprints. It never loads a checkpoint.

## Publication

The repository's `wiki/` files are the canonical editable sources for these public pages. The public curated package is hosted under immutable `https://logs.reshub.lol/pysr-ext-higgs/0.1.0/` URLs. Arvancloud owns public HTTPS and automatic renewal; the dedicated Caddy origin serves public files over HTTP to the edge. Raw logs, checkpoints, environment files, and backups remain private/local. Synchronize the separate Wiki checkout before publishing source revisions, then verify the public pages and their downloads.

PNG/PDF binaries are optional ignored local cache. Git retains small candidate tables, source exports, and checksums. `fetch_artifacts.py --expression L2HL_1_050` explicitly downloads that expression's binary files, checks their committed size and SHA-256, then atomically installs them; no automatic download occurs during ordinary inspection. With no cached curve image, the notebook offers its hosted URL instead. Failed downloads never replace existing cache bytes.

The hosted 0.1.0 snapshot preserves its original curation metadata, including prepublication status labels; current endpoint publication is established by the separate deployment/acceptance record. Original generating commits and split membership are not inferred from hosting or successful downloads.

[Home](Home) · [Retained results](Project-Registry)
