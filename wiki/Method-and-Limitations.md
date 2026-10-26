# Method and limitations

**Page v0.3.0 · Code release v5.7.0 · Updated 2026-10-26.**

## Current scope

The [Project Registry](Project-Registry) presents L2HL_1_050 as the current expression. Previous catalogue revisions remain historical records; they are not the active result on these pages.

The model uses mchi1 and mchipm1 in GeV and predicts a continuous raw score for the binary reference labels in exclusion. The score is not a calibrated probability, and this cleanup assigns no new physical meaning to the labels.

## Objective, labels, and scores

The saved expression uses L2HingeLoss(). The current training entry point maps labels 0 and 1 to signed targets -1 and +1 with 2*y-1 and balances sample weights using training rows. ROC-AUC uses the continuous scores with label 1 as positive.

Negative raw scores are valid classifier scores. A margin score is not automatically a probability. The current expression’s loss identifies its training objective; it does not show that this loss is statistically superior to alternatives. See the [PySR loss documentation](https://github.com/astroautomata/PySR/blob/master/docs/src/options.md#loss) and [LossFunctions.jl margin definitions](https://juliaml.github.io/LossFunctions.jl/stable/losses/margin/).

## Validation and selection

The fixed-expression validation AUC reported in the registry, 0.9726962005193153, comes from evaluating the saved expression on the validation portion of the current reconstructed split. The dataset has 12,280 rows; the stratified split is 60%/10%/30% with seed 42. Original split membership is unknown, so this reproduction does not authenticate the historical validation rows or establish independent performance.

The saved record’s test AUC is 0.9615986120334543. The original workflow used test AUC for expression selection, so that value is a selection score, not an untouched final-test estimate. The current reproduction matching it does not restore untouched-test status.

## Diagnostics

| Diagnostic | What changes | What it supports |
|---|---|---|
| Fixed-expression subset variability | Validation rows are divided into six subsets; L2HL_1_050 stays fixed | Descriptive variation across those subsets; no refitting or confidence interval |
| Fitted validation curve | Fresh child models use configured complexity limits on the training split | Effect of those limits for the individual diagnostic fits |
| Fitted learning curve | Fresh child models use configured fractions of the training rows | Effect of training-set size for the individual diagnostic fits |

The fitted curves are diagnostic searches, not evaluations of the frozen L2HL_1_050 expression. They use fresh child models and PySR’s model selection rule. A single fit per point provides no repeated-fit uncertainty estimate. The notebook writes new diagnostics under ignored output/curve_diagnostics/ directories when curve fitting is enabled.

## Provenance

The current dataset fingerprint is SHA-256 c8c8063c84a10143b6369f444a037ef5695ff13f5eef6f9bf00dc86880c3937a. Current split sizes are 7,368 training, 1,228 validation, and 3,684 test rows. The saved expression manifest records the reproduction and explicitly leaves original split membership unknown.

Future training runs write actual row identities, label mapping, weights, available model parameters, dataset hash, package versions, and source hashes before fitting. This does not backfill historical training provenance.

## Publication

The repository’s wiki/ files are the canonical editable sources for these Wiki pages. The L2HL_1_050 expression assets are served from immutable versioned paths at [logs.reshub.lol](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/). Raw logs, checkpoints, environment files, and backups remain local. Downloads are explicit; saved-result inspection does not fetch files automatically.

[Home](Home) · [Project Registry](Project-Registry)

<sub>Page v0.3.0 · Previous v0.2.1 · Code release v5.7.0.</sub>
