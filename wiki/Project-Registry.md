# Recorded results

## HP batch: 17 recorded expressions

[Batch guide](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/hp-run-num1-v0.1.0/README.md) · [Exact logger snapshot](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/hp-run-num1-v0.1.0/logger.csv) · [Batch manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/hp-run-num1-v0.1.0/manifest.json)

`TEMP_4_0141` has the highest recorded test AUC in this batch. `TEMP_19_044` provides a simpler comparison (complexity 44 versus 141), with a recorded AUC difference of approximately 0.00004803. This numerical difference does not establish statistical equivalence or superiority.

| Expression | Complexity | Loss | Recorded test AUC |
|---|---:|---:|---:|
| [TEMP_4_0141](#user-content-temp_4_0141) | 141 | 0.0781385913308636 | 0.9635796010086283 |
| [TEMP_19_044](#user-content-temp_19_044) | 44 | 0.0825036511819801 | 0.9635315710928521 |
| [TEMP_5_059](#user-content-temp_5_059) | 59 | 0.0786298387687911 | 0.9631669358138987 |
| [TEMP_12_064](#user-content-temp_12_064) | 64 | 0.0857304931533565 | 0.962907672288944 |
| [TEMP_2_070](#user-content-temp_2_070) | 70 | 0.0792349968744776 | 0.9618010238213678 |
| [TEMP_17_052](#user-content-temp_17_052) | 52 | 0.0796802568232809 | 0.9613378782049553 |
| [TEMP_3_065](#user-content-temp_3_065) | 65 | 0.0821458387191495 | 0.9608727721838173 |
| [TEMP_11_071](#user-content-temp_11_071) | 71 | 0.0876339711619138 | 0.9604326613229301 |
| [TEMP_15_068](#user-content-temp_15_068) | 68 | 0.0824209249713451 | 0.9598210150485568 |
| [TEMP_16_079](#user-content-temp_16_079) | 79 | 0.0804398467206262 | 0.9596210537665502 |
| [TEMP_13_068](#user-content-temp_13_068) | 68 | 0.0832458771554274 | 0.957847867692285 |
| [TEMP_18_064](#user-content-temp_18_064) | 64 | 0.087507877929393 | 0.9555610555799245 |
| [TEMP_7_082](#user-content-temp_7_082) | 82 | 0.0883229018843609 | 0.9531149605836124 |
| [TEMP_1_0202](#user-content-temp_1_0202) | 202 | 0.0890910802704311 | 0.9526199583904097 |
| [TEMP_14_044](#user-content-temp_14_044) | 44 | 0.0903690572943183 | 0.9516814146280499 |
| [TEMP_10_0479](#user-content-temp_10_0479) | 479 | 0.1027698262892726 | 0.9354335802626452 |
| [TEMP_6_0138](#user-content-temp_6_0138) | 138 | 0.1359070364827088 | 0.8768483553429607 |

The inspected v5.3.0 pipeline ranks candidate expressions by `test_auc`; that score is part of selection and is not an untouched final-test estimate. Total AUC is descriptive. Saved validation-subset figures reuse one fixed expression across six subsets, with no refitting. The SD band is not a confidence interval. Figure labels remain as recorded; other full-precision split AUCs are not supplied by this logger.

These are preserved recorded outputs. No predictions, AUCs, or figures were recalculated and no model was retrained for this catalogue. The original generating commit, training-data fingerprint, split membership, run date, and run-specific selection invocation are not established by the winner CSV. Exported expressions return raw, uncalibrated scores.

`TEMP_8` and `TEMP_9` have no finalized rows in this logger and are excluded from this leaderboard. Plots are unavailable for `TEMP_1_0202` and `TEMP_2_070`; their expression downloads are available. The historical `TEMP_6_038` snapshot appears separately below.

## TEMP_4_0141

Recorded source: `HP_output/TEMP_4/`.

| Recorded field | Value |
|---|---|
| Complexity | 141 |
| Loss | 0.0781385913308636 |
| Test AUC | 0.9635796010086283 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_4_0141.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
0.9831143619017236 - exp(4*(-9473.746885051392*mchi1*(mchi1 + mchipm1)/mchipm1**2 - mchipm1**2/(mchi1 + 3.3277173633206085))/(3048.383200273093*mchipm1/((-0.03905646364146095*mchi1*(-381.32667087515931*mchi1**12/(-mchi1 + (1.4868466271092322 + (3.333641668254851 - 7015.862366316909/mchipm1)*(55.211646150405386*mchi1 - 55.257719520092348)*(mchipm1 - 18.787663910564365)/mchi1)**2)**3 + mchi1 - 2.3159940700174513*mchipm1 + cos(mchi1)**3 + 0.03905646364146095) + 5.7700305017944293e-8*mchipm1**2*(mchipm1 + 18.787663910564365)**2/(3.333641668254851 - 7015.862366316909/mchipm1)**2)*cos(3.8571244396442319*exp(6*mchi1 - 6*mchipm1))) + 7.2515758500794005)**2)
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_4_0141: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_4_0141: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_4_0141: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_19_044

Recorded source: `HP_output/TEMP_19/`.

| Recorded field | Value |
|---|---|
| Complexity | 44 |
| Loss | 0.0825036511819801 |
| Test AUC | 0.9635315710928521 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_19_044.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
1.0471682425656008*cos(-0.5399005817691068*cos(0.06243687511774902/(-mchi1 + mchipm1)**2)*cos(cos(0.0038649110353923895*mchipm1)) + cos(0.0006160326007406046*mchi1 + mchi1/mchipm1 + 0.001246679746186349*mchipm1) + 1.223996039565275)
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_19_044: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_19_044: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_19_044: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_5_059

Recorded source: `HP_output/TEMP_5/`.

| Recorded field | Value |
|---|---|
| Complexity | 59 |
| Loss | 0.0786298387687911 |
| Test AUC | 0.9631669358138987 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_5_059.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos(2601701849.6049196/(4.6519505259157803*mchi1**2/(0.9668685139528674*mchipm1 + (mchi1 + 1/(((mchi1 - mchipm1)**2 - 0.02200355064329114)**2*cos(1124.9483020019968/(4.6519505259157803*mchi1**2/(mchipm1 + 0.9668685139528674 + 1891639.3970876367/mchipm1**2) + mchipm1 + 1124.9483020019968))))**2/mchipm1**2) + mchipm1 + 1124.9483020019968)**3)**18
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_5_059: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_5_059: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_5_059: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_12_064

Recorded source: `HP_output/TEMP_12/`.

| Recorded field | Value |
|---|---|
| Complexity | 64 |
| Loss | 0.0857304931533565 |
| Test AUC | 0.962907672288944 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_12_064.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos((-mchi1 + mchipm1)*exp(mchi1 - mchipm1) + (cos(2.9071847628409433*(0.8698961291302949 - exp(mchi1 - mchipm1))/(mchi1 - mchipm1)) + cos((0.0023500341036272214*mchi1 + 0.8698961291302949)*cos(exp(mchi1 - mchipm1))))*cos(1.1842469812652451e-9*mchipm1**2/(mchi1 - mchipm1) - 0.0008099082877929833*mchipm1))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_12_064: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_12_064: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_12_064: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_2_070

Recorded source: `HP_output/TEMP_2/`.

| Recorded field | Value |
|---|---|
| Complexity | 70 |
| Loss | 0.0792349968744776 |
| Test AUC | 0.9618010238213678 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

**Plots unavailable:** no saved plot files were present in this run at curation time.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
(-0.3829787837384603*mchi1 - 3.0796562256598416)**2/(1.2800499244737693 - 3.4126094646469687*(mchi1 - 297.5807274153572/(-0.02802391250173666*mchi1**2/mchipm1 - 0.01401195625086833*mchipm1))*(0.1027355249283932*mchi1 + 5605807082.3072288/(-mchi1**2 + mchipm1**2 - 0.29045780755911328*mchipm1)**6 - 2.5947665530701878/(-9.541354176772265e-13*mchipm1**6/(mchi1 + 35652.67774409823/mchipm1)**3 - 0.4132520379183373))/mchi1)**2
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_17_052

Recorded source: `HP_output/TEMP_17/`.

| Recorded field | Value |
|---|---|
| Complexity | 52 |
| Loss | 0.0796802568232809 |
| Test AUC | 0.9613378782049553 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_17_052.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos((cos(0.006771653483997484*mchi1*cos(0.0010624337867578971*mchipm1)*cos(0.22086834599835395/(mchi1 - mchipm1))) + cos(0.0013335603759751385*mchi1 - cos(0.0010624337867578971*mchipm1)))*cos(0.0015533284844867915*mchi1)*cos(1.2526123639497352e-6*mchipm1**2*cos(0.0006219766309761784*mchipm1)))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_17_052: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_17_052: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_17_052: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_3_065

Recorded source: `HP_output/TEMP_3/`.

| Recorded field | Value |
|---|---|
| Complexity | 65 |
| Loss | 0.0821458387191495 |
| Test AUC | 0.9608727721838173 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_3_065.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
1.230457690662212*exp(-exp(3*exp(3*(6.923296036632556*exp(3*exp(-12550.28898243733*(-mchi1 + mchipm1)**6*exp(51.248126907349775*exp(-1807.7661046528661*(-mchi1 + mchipm1)**3)))) - 0.99999890201231244)/mchipm1))/(mchi1*cos(cos(1.3048615280737272e-7*(-mchi1 + mchipm1)**3*exp(-6*exp(-3.6824283549543966/mchi1)))**3)**3))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_3_065: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_3_065: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_3_065: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_11_071

Recorded source: `HP_output/TEMP_11/`.

| Recorded field | Value |
|---|---|
| Complexity | 71 |
| Loss | 0.0876339711619138 |
| Test AUC | 0.9604326613229301 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_11_071.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
0.0024014686028372913*mchi1 - 5.5619591698021137e-5*mchipm1*cos(1.9818570139556385e-6*mchipm1**2) - 3.0001136419956882e-7*(-mchi1 + mchipm1)**2 + 0.61074652692370113*(mchi1/mchipm1 - 0.3640153559561071)*(-2.3481549045374917e-6*mchipm1**2 + cos(-0.002950812503982865*mchipm1 + 0.16114244372418238 + (-mchi1 + mchipm1 - 0.44883882821779203)/(-mchi1 + mchipm1)) - 0.7586481852215448)
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_11_071: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_11_071: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_11_071: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_15_068

Recorded source: `HP_output/TEMP_15/`.

| Recorded field | Value |
|---|---|
| Complexity | 68 |
| Loss | 0.0824209249713451 |
| Test AUC | 0.9598210150485568 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_15_068.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos((cos(0.0040287826938821689*mchi1 - 0.00049729729813319252*mchi1/(-mchi1 + mchipm1)) + 0.5645274129759962)*cos(5.71690793620207e-7*mchipm1**2)*cos(-0.003611299686454646*mchi1 + 0.0005245936877285318*mchi1/(-mchi1 + mchipm1) + 8.6055580634205687e-10*mchipm1**2*(2*mchi1 + mchipm1)))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_15_068: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_15_068: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_15_068: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_16_079

Recorded source: `HP_output/TEMP_16/`.

| Recorded field | Value |
|---|---|
| Complexity | 79 |
| Loss | 0.0804398467206262 |
| Test AUC | 0.9596210537665502 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_16_079.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos((-0.0016464956341800338*mchi1*(exp(mchi1 - mchipm1) - 0.8712027804933787) - 0.8749126159685751)*(cos((exp(mchi1 - mchipm1) - 0.8594876517622306)*(0.061305330738716246*mchi1 + 0.0013968196536284425*mchipm1*(mchi1 - mchipm1) - cos(cos(mchipm1)))*exp(mchi1 - mchipm1)) + cos(2.7715166273604876e-6*mchipm1*(mchi1 - mchipm1) + 0.001984162107227708*mchipm1))*cos(cos(0.0017199045572864197*mchipm1) - 0.6698894944561484))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_16_079: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_16_079: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_16_079: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_13_068

Recorded source: `HP_output/TEMP_13/`.

| Recorded field | Value |
|---|---|
| Complexity | 68 |
| Loss | 0.0832458771554274 |
| Test AUC | 0.957847867692285 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_13_068.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos((cos(0.004514648803959916*mchi1 - 0.0005057636527631049*mchipm1 + 0.0005057636527631049*mchipm1/(mchi1 - mchipm1) + 0.1584875312709165) + 0.640463100841876)*cos(0.001231948657820141*mchipm1 - 0.32000430242982697)*cos(0.003132615676865654*mchi1 - 0.0005279310693999557*mchipm1 + 0.1654339757578514 + 0.0005279310693999557*(mchipm1 - 5.1087269571265446)/(mchi1 - mchipm1)))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_13_068: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_13_068: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_13_068: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_18_064

Recorded source: `HP_output/TEMP_18/`.

| Recorded field | Value |
|---|---|
| Complexity | 64 |
| Loss | 0.087507877929393 |
| Test AUC | 0.9555610555799245 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_18_064.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
0.0001563314903542978*mchi1 + cos(0.00042971526622973184*mchi1 + 0.10901053160131852*cos(0.010220335652266464*mchi1) + cos(0.00084221563880952839*mchi1 + 0.00064448579685492447*mchi1/(mchi1 - mchipm1) + 0.0012134516010386314*mchipm1 - 47.381992390600867 + (mchi1**2/(mchipm1 - 2.4824165868394656) + mchi1)/(mchipm1 + 187.9373802434672)) - 0.6799123723908508)
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_18_064: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_18_064: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_18_064: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_7_082

Recorded source: `HP_output/TEMP_7/`.

| Recorded field | Value |
|---|---|
| Complexity | 82 |
| Loss | 0.0883229018843609 |
| Test AUC | 0.9531149605836124 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_7_082.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
1.239945070371659*cos(285.0163090640031/(1.09530417787674*mchi1 + 162.4535037117941))**2*cos(1.586908423231659*cos(1.904573633324856*cos(cos(1.889080952963016*cos(cos(1.83184626582135*cos(142.50826222441612/mchipm1)**4*cos(cos(1.0822340599408649/(2*mchi1 - 2*mchipm1 + 0.6500800138018834))))/(mchi1 - mchipm1 - 0.39662441926791125)))/(mchi1 - mchipm1 - 0.43293892967454467))))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_7_082: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_7_082: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_7_082: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_1_0202

Recorded source: `HP_output/TEMP_1/`.

| Recorded field | Value |
|---|---|
| Complexity | 202 |
| Loss | 0.0890910802704311 |
| Test AUC | 0.9526199583904097 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

**Plots unavailable:** no saved plot files were present in this run at curation time.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
-6.9380592898841236e-7*mchi1**2 + 0.0009938862168577531*mchi1 + 0.33933793703051873*mchi1/mchipm1 + 0.00075749508220749224*mchipm1 - 0.00023639113465026086*(-0.41811692320723814 + 0.3029890451290253/(-mchi1 + mchipm1 + 0.37541633508686867))*(-0.0077412771575638166*mchi1*(-mchi1*(0.00094555464112512708*mchipm1 - 0.0017235067491824511) + mchi1 + mchipm1) - 9326.353576207914*(-0.07726193727764205*mchi1*(0.3976668140822962 - (-mchi1 + 22361.858310595206/mchi1)/mchi1)*sinh(sin(sqrt(mchi1)))/(-mchi1 + mchipm1 + 0.17964999106168295) - mchi1 - 0.07726193727764205*mchipm1 + 0.07726193727764205*(-0.2657976199306784 + 0.33933793703051873/(-mchi1 + mchipm1 + 0.17964999106168295))*(9326.661132884612 - 3502.2656429489357/(-mchi1 + mchipm1 + 0.22056877713805761))*(-mchi1 + 7070.205594373127/mchipm1)/mchipm1 + 7070.205594373127/mchipm1)/mchipm1) - 0.4042980470319076 + 0.00023639113465026086*(mchipm1 - 14659.438128031303*(-900.1339416737602 + 338.01036974109327/(-mchi1 + mchipm1 + 0.22056877713805761))*exp(cos(sqrt(mchipm1)))/(mchipm1*(-mchi1 + mchipm1 + 0.37541633508686867)))/mchipm1
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_14_044

Recorded source: `HP_output/TEMP_14/`.

| Recorded field | Value |
|---|---|
| Complexity | 44 |
| Loss | 0.0903690572943183 |
| Test AUC | 0.9516814146280499 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_14_044.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos((cos(0.0011179575743389659*mchipm1) + cos(0.0036365157066324105*mchi1 - 0.5430077792785011))*cos(0.0007418339523333352*mchi1 + cos(0.0017245059292014982*mchi1 + 2*exp(mchi1 - mchipm1) - 0.995728453980836)))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_14_044: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_14_044: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_14_044: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_10_0479

Recorded source: `HP_output/TEMP_10/`.

| Recorded field | Value |
|---|---|
| Complexity | 479 |
| Loss | 0.1027698262892726 |
| Test AUC | 0.9354335802626452 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_10_0479.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos(8.0625313659714127*cos(-0.00015060011547011*mchi1*cos(8.1632093777223689*cos(8.1066148630616316*cos(0.00012100644119419947*mchi1 + 0.00012100644119419947*mchipm1 - 0.0005042645084600892) + 0.1174124306714608)) - 0.0001580646840738506*mchipm1 + 0.012728865304116001*(-0.00012777495482743631*(mchi1 - mchipm1)*(-1.425679823006473*cos(mchi1 + 0.00021581710959157956*cos(mchipm1) - 8.4205043962285695e-5*cos(cos(mchipm1) + 0.013789860831776222) - 7.7710593682122946e-5) - cos(mchi1 - mchipm1 + 0.21165897450759596*cos(cos(85.164421551882859 + 18.416014739083616*(-8.1746485183232503*mchipm1 + 8.1746485183232503*cos(0.00021581710959157956*mchipm1 + cos(mchi1) - 8.4205043962285695e-5*cos(mchipm1**2 + 0.013789860831776222) - 7.7710593682122946e-5) - 1.3415726087407804)/mchipm1)) - 0.3688843157240694 + 1.4450131899843055/mchipm1) - 0.1799636759242319) + 1.4546380889073431)*(-exp(mchi1 - mchipm1) + 8.1648803368513071*cos(7.805562888029305 - 18.416014739083616*(8.1746485183232503*mchipm1 + 8.1746485183232503*cos(cos(mchi1 - 1.0002158171095916*mchipm1 - 0.00021581710959157956*cos(cos(mchipm1) + 0.013789860831776222) + 8.4205043962285695e-5)) - 1.3415726087407804)/mchipm1) + cos(8.159604219242177*cos(cos(9.5544498105053568*mchi1 - 9.5544498105053568*mchipm1 - 1.3551045253314567e-5*cos(mchi1*(mchi1 + mchipm1*(0.03339492119686522 - mchi1))) + 0.41917619363307488 + 11.554449810505357*(-mchipm1 - 1.4450131899843055)/mchipm1) + 0.9925649972255859) + 0.07205116713265368) - 1.6351820651891745)*cos(cos(7.9960860500040497*cos(-mchi1 + mchipm1 + 0.00021581710959157956*cos(-2*mchi1 + 2*mchipm1 + 1.3551045253314567e-5*cos(-mchi1*mchipm1 + mchi1 + mchipm1*(0.03339492119686522 - mchipm1)) + 1.0168134550812663 - 1.543378630276006*(mchipm1*(mchipm1 + 0.03339492119686522) - 1.4450131899843055)/mchipm1) + 0.00021421250878300013))) + 0.054512300477323502*cos(-mchi1 + mchipm1 + 9.9708002096367522) + cos(8.2457082867813856*cos(0.00012667511609787765*mchi1 + 0.00012667511609787765*mchipm1 + 0.36662408932113853)) + 0.036562611135761306*cos(7.882825602635493*cos(-mchi1 + mchipm1 + cos(0.7341055367589796/mchi1) + 10.189765084258168)) + 0.053599055106485029))
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_10_0479: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_10_0479: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_10_0479: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## TEMP_6_0138

Recorded source: `HP_output/TEMP_6/`.

| Recorded field | Value |
|---|---|
| Complexity | 138 |
| Loss | 0.1359070364827088 |
| Test AUC | 0.8768483553429607 |
| Export version | `5.3.0` |
| Snapshot version | `0.1.0` |

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_6_0138.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/roc_curve.pdf)

Split AUCs and row counts on this figure are preserved annotations, not newly calculated measurements.

### Expression and downloads

<details>
<summary>Exact saved SymPy expression</summary>

```text
# Version v5.3.0
cos(cos(0.0061297098632736863*mchi1**3*mchipm1*(cos(cos(cos(0.0067415218184474576*mchi1**4*(cos(cos(0.039411289288254768*mchipm1**2*cos(mchipm1 - 1.0993553408313173)*cos(cos(cos((cos(mchi1**2) - 1.180370972830416)*(cos(cos(1.0864409736134717/mchi1)) + cos(cos(4.4499460275467418e-6*mchi1*(exp(0.016448221487657004*mchi1/mchipm1**3) + 1.3952997099950084) + mchipm1 - 0.22967492753516194))))) - 1.0864409736134717)/mchi1**3)) - 0.2278992666066265)/(mchi1 - 0.6946425812491337)**3))) - 0.9950334412094952)/(mchi1 + 0.789102217619601)**3) + 0.4445403464765526) + 0.06227710785266158
```

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/expression_sympy.txt) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/expression_lambda.py) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/expression.tex) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/expression.tex) |
| Expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/expression.pdf) | [Raw file](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting the named mass columns `mchi1` and `mchipm1`. Its structure was checked without executing predictions.

<details>
<summary>Mass plane: saved scores and reference labels</summary>

![TEMP_6_0138: Mass plane: saved scores and reference labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/mass_plane.pdf)

Observed mass pairs and stored reference labels. Colours represent raw scores, not calibrated probabilities.

</details>

<details>
<summary>One-dimensional mass scan</summary>

![TEMP_6_0138: One-dimensional mass scan.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/mass_scan_1d.pdf)

Saved score scan with charged mass fixed at 2000 GeV. This constructed scan is not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![TEMP_6_0138: Validation subset variability: fixed expression, no refitting.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/plots/subset_variability.pdf)

Six subsets reuse a fixed expression. The SD band is not a confidence interval and does not establish original holdout membership.

</details>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/manifest.json)

The manifest maps the exact logger row and source paths to curated copies, records unavailable plots, and lists checksums. It identifies preparation state separately from unknown historical provenance.

## Historical collection

The following entry comes from `output/TEMP_6/`, separately from the HP batch. It is preserved with its original immutable artifact links and is not ranked against the new batch.

## TEMP_6_038

Recorded winner associated with the local run directory `output/TEMP_6/`.

| Recorded field | Value |
|---|---|
| Complexity | 38 |
| Loss | 0.115475366577816 |
| Test AUC | 0.939721965599798 |
| Export version label | `5.3.0-ATTEMPT2` |
| Curated snapshot version | `0.1.0` |

> **Evidence boundary:** these are existing recorded outputs. No AUCs were recomputed, figures regenerated, or model retrained for this catalogue. The generating commit, original dataset fingerprint, original split membership, run date, and run-specific selection setting are not established by the winner CSV. This entry is not an independent performance validation.

### Recorded ROC

![Recorded full and magnified ROC curves for TEMP_6_038, with training, validation, test, and total split labels.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/roc_curve.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/roc_curve.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/roc_curve.pdf)

The figure is preserved as saved. Its other split AUC labels are rounded annotations, not newly calculated measurements. The source winner CSV separately supplies only the full-precision test AUC displayed above.

### Expression and downloads

<details>
<summary>Saved SymPy expression</summary>

```text
# Version v5.3.0-ATTEMPT2
0.5329653825951353*mchi1*(sin((-mchi1 + mchipm1)**4)**2)**(1/16)*sin(sinh(1.2624352887127586/mchipm1)) + 0.3618155531824624*mchipm1**(1/4) - 1.505232312261181
```

This is the exported expression text. Its output is a raw, uncalibrated score.

</details>

| Format | View | Raw file |
|---|---|---|
| SymPy text | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/expression_sympy.txt) | [Raw text](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/expression_sympy.txt) |
| Python / NumPy | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/expression_lambda.py) | [Raw Python](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/expression_lambda.py) |
| TeX source | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/expression.tex) | [Raw TeX](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/expression.tex) |
| Formatted expression PDF | [View](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/expression.pdf) | [Raw PDF](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/expression.pdf) |

The Python module exposes `FEATURES` and `predict(X)`, accepting a DataFrame with the named mass columns. No checkpoint is needed to use the exported module. This curation checks its source structure without executing predictions.

### Additional recorded figures

<details>
<summary>Mass plane: recorded scores and reference labels</summary>

![Recorded TEMP_6_038 mass-plane panels comparing raw scores with reference labels on test, validation, and training data.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/mass_plane.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/mass_plane.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/mass_plane.pdf)

Observed mass pairs, as recorded in the figure. Colours represent raw scores, not calibrated probabilities. The physical meanings of reference labels 0 and 1 are not established by the winner CSV.

</details>

<details>
<summary>One-dimensional scan: charged mass fixed at 2000 GeV</summary>

![Recorded TEMP_6_038 raw score versus neutral mass mchi1, with charged mass mchipm1 fixed at 2000 GeV.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/mass_scan_1d.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/mass_scan_1d.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/mass_scan_1d.pdf)

The saved title identifies `mchipm1 = 2000 GeV` as fixed; the horizontal axis varies `mchi1`. This is a constructed score scan, not a labelled dataset or an AUC measurement.

</details>

<details>
<summary>Validation subset variability: fixed expression, no refitting</summary>

![Recorded TEMP_6_038 validation subset ROC curves, their mean, and a one-standard-deviation band.](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/subset_variability.png)

[Full-size PNG](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/subset_variability.png) · [PDF](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/plots/subset_variability.pdf)

The six subsets reuse one fixed expression. The plotted SD band is not a confidence interval. The saved plot does not establish original training or holdout membership.

</details>

<details>
<summary>Technical record, provenance, and checksums</summary>

[Snapshot manifest](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/manifest.json) · [Raw manifest](https://raw.githubusercontent.com/wadewolfie999/pysr_ext_higgs/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/manifest.json)

The manifest preserves the selected winner CSV row and maps its original paths to these curated copies. SHA-256 checksums establish byte identity with the local source files at curation time; they do not establish scientific validity.

| Provenance item | What is established |
|---|---|
| Exported feature names | `mchi1`, `mchipm1`, from the Python module |
| Source export label | `5.3.0-ATTEMPT2`, retained without relabelling |
| Generating commit | Not recorded in the winner CSV |
| Original dataset fingerprint and split membership | Not recorded in the winner CSV |
| Historical run date and selection setting | Not recorded in the winner CSV |
| Other full-precision split AUCs | Not supplied by the winner CSV; not recomputed here |

The current v5.3.0 pipeline defaults to test-AUC ranking. The specific historical invocation is not recorded. If a test score is used to select an expression, it is not an untouched final test estimate; see [scikit-learn's model-selection guidance](https://scikit-learn.org/stable/common_pitfalls#data-leakage). Total AUC is descriptive.

</details>

<details>
<summary>Historical protocol notes</summary>

The earlier registry used `masses_exclusions.csv` with mass features `mchi1` and `mchipm1`, naming test ROC-AUC as the primary metric. It labelled `exclusion` as the evaluation set; in the current code, `exclusion` is the target column, while train, validation, test, and total are evaluation datasets. The following development note is retained as history:

  - I was using the ROC-AUC scored from 'total' split of the data (i.e. the whole input data);
    - Then, while browsing optimized methods, i found out i should use 'val' split!
    - But because my input data is small (~12k), i transferred to 'test' split, since it was close the mean of four auc recorded.
    - I will put a link, writing this bug of mine, in detail.

This records the progression of the author's choices. It does not establish that proximity to the mean of split AUCs makes a score an independent test. Any future selection-rule change is a separate research decision.

</details>

[Back to Home](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/)

<sub>Page version 0.2.2 · HP batch snapshot 0.1.0 · Historical snapshot 0.1.0 · Reviewed 2026-10-25.</sub>
