# Project Registry

The current selected expression is **`L2HL_1_050`**. This page collects its scores, saved plots, and downloadable files.

[Wiki Home](https://github.com/wadewolfie999/pysr_ext_higgs/wiki) · [Install and run](https://github.com/wadewolfie999/pysr_ext_higgs#how-to-run-this-on-your-machine) · [Methods and limitations](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Method-and-Limitations)

## L2HL_1_050

**Parent run:** `L2HL_1` · **Complexity:** 50 · **Loss:** `L2HingeLoss()`

The expression uses the mass features **`mchi1`** and **`mchipm1`** (GeV) to return a continuous score for the binary reference target `exclusion`.

### ROC-AUC at a glance

| Evaluation split | ROC-AUC | Role |
|---|---:|---|
| Training | 0.957333 | Current reproduction |
| **Validation** | **0.972696** | Current reproduction on reconstructed validation rows |
| Test | 0.961599 | Matches the recorded expression-selection score |
| All rows | 0.960129 | Descriptive evaluation |

*Values are rounded to six decimal places; the full values are available in the [committed record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/main/results/L2HL_1_050/manifest.json).*

> **Reading these scores:** Validation uses a reconstructed split; original split membership is unknown. Test AUC was used to select the expression, so it is not an independent final-test estimate. See [evaluation and selection](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Method-and-Limitations#evaluation-and-selection) for the details.

### ROC curve

![Saved full and magnified ROC curves for L2HL_1_050.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.png)

*The saved figure is preserved as recorded; the table above reports the current fixed-expression reproduction.*

[Full-size PNG](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.png) · [Download PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.pdf)

### More diagnostic plots

*Expand a plot to inspect it.*

<details>
<summary><strong>Mass plane — expression scores and reference labels</strong></summary>

![Saved L2HL_1_050 mass-plane scores and binary reference labels.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_plane.png)

The two panels compare scores and reference labels at the observed mass pairs. **Scores are uncalibrated**; their colours do not represent probabilities.

[Full-size PNG](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_plane.png) · [PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_plane.pdf)

</details>

<details>
<summary><strong>Mass scan — varying the neutral mass at fixed charged mass</strong></summary>

![Saved L2HL_1_050 score scan with the charged mass fixed at 2000 GeV.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_scan_1d.png)

This constructed scan varies `mchi1` with **`mchipm1 = 2000 GeV`**. It shows how the raw expression behaves along that slice.

[Full-size PNG](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_scan_1d.png) · [PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_scan_1d.pdf)

</details>

<details>
<summary><strong>Validation subsets — one fixed expression, six subsets</strong></summary>

![Saved L2HL_1_050 ROC curves across six validation subsets.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/subset_variability.png)

The expression stays fixed while the validation rows are partitioned into six subsets. This describes subset variability; **it is not refitted cross-validation**, and the standard-deviation band is not a confidence interval.

[Full-size PNG](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/subset_variability.png) · [PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/subset_variability.pdf)

</details>

### Expression downloads

| File | Use |
|---|---|
| [SymPy expression](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression_sympy.txt) | Read the saved expression |
| [NumPy module](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression_lambda.py) | Evaluate it with `predict(X)` using the named mass columns |
| [Expression PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression.pdf) · [TeX source](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression.tex) | Read or typeset the expression |
| [Candidate table](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/hall_of_fame.csv) | Inspect the saved search candidates |
| [Manifest and checksums](https://github.com/wadewolfie999/pysr_ext_higgs/blob/main/results/L2HL_1_050/manifest.json) | Inspect the full recorded metrics and file hashes |

To inspect this expression locally, follow [the README's saved-result instructions](https://github.com/wadewolfie999/pysr_ext_higgs#inspect-the-saved-result).

<details>
<summary><strong>Technical record — dataset, split, and original export</strong></summary>

| Item | Value |
|---|---|
| Current dataset | 12,280 rows from `data/masses_exclusions.csv` |
| Reconstructed split | Stratified 60% / 10% / 30%; seed 42 |
| Split sizes | 7,368 training / 1,228 validation / 3,684 test |
| Recorded objective value | 0.3425168330019069 |
| Original expression export label | `5.3.1` |
| Expression record version | `0.1.0` |

Dataset SHA-256:

```text
c8c8063c84a10143b6369f444a037ef5695ff13f5eef6f9bf00dc86880c3937a
```

The full historical generating commit and original split membership are unverified. The current reproduction matches the recorded test AUC and exported NumPy predictions. Earlier catalogues remain in Git history.

</details>

---

[Wiki Home](https://github.com/wadewolfie999/pysr_ext_higgs/wiki) · [Methods and limitations](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Method-and-Limitations)

<sub>Page v0.6.0 · Expression record v0.1.0 · Updated 2026-10-26.</sub>
