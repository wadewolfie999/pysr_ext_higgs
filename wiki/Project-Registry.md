# Project Registry

**Wiki revision v0.5.0 · Updated 2026-10-26.** This page contains the current expression record.

## L2HL_1_050

| Record | Value |
|---|---|
| Parent run | L2HL_1 |
| Saved objective | L2HingeLoss() |
| Complexity | 50 |
| Recorded objective value | 0.3425168330019069 |
| Recorded test AUC | 0.9615986120334543; original selection score |
| Original export label | 5.3.1 |

### Current fixed-expression reproduction

| Split | ROC-AUC | Interpretation |
|---|---:|---|
| Training | 0.9573333839771221 | Current reproduction |
| Validation | 0.9726962005193153 | Current reproduction on reconstructed validation rows |
| Test | 0.9615986120334543 | Matches the recorded test selection score |
| All rows | 0.9601292032444535 | Descriptive |

The reproduction uses the current dataset (12,280 rows; SHA-256 c8c8063c84a10143b6369f444a037ef5695ff13f5eef6f9bf00dc86880c3937a) and a stratified 60%/10%/30% split with seed 42. That gives 7,368 training, 1,228 validation, and 3,684 test rows. The original training and validation membership is not recoverable from the saved evidence. The validation value is therefore a current reproduction, not an authenticated historical result or an independent estimate.

The original workflow used test AUC to select expressions. The recorded test AUC remains a selection score and must not be presented as an untouched final-test result.

### Expression files

- [SymPy expression](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression_sympy.txt)
- [NumPy expression module](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression_lambda.py)
- [TeX source](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression.tex)
- [Expression PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression.pdf)
- [Candidate table](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/hall_of_fame.csv)
- [Manifest and checksums](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/manifest.json)

### Saved diagnostics

![Preserved L2HL_1_050 ROC curve.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.png)

[ROC PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.pdf) · [Mass-plane PNG](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_plane.png) · [Mass scan PNG](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_scan_1d.png) · [Validation subset variability PNG](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/subset_variability.png)

The subset-variability plot keeps this expression fixed across six validation subsets. It describes variation among those subsets; it is not refitted cross-validation or a confidence interval.

[Method and limitations](Method-and-Limitations) · [Home](Home)

<sub>Page v0.5.0 · Previous v0.4.1 · Expression record v0.1.0.</sub>
