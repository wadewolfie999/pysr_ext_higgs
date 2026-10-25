# PySR in Extended Higgs Sector Models

Symbolic regression for a two-mass classification problem in an extended Higgs model. PySR learns an explicit score from the neutral mass $m_{\chi_1}$ and charged mass $m_{\chi_1^\pm}$, expressed in GeV, to distinguish the dataset's binary reference labels.

## How to run this on your machine

1. Clone the repository and enter its directory:
   ```bash
   git clone https://github.com/wadewolfie999/pysr_ext_higgs.git
   cd pysr_ext_higgs
   ```

2. Check Python; the environment used for this project is Python `3.13.7`:
   ```bash
   python --version
   ```
   If needed, install pyenv with `curl -fsSL https://pyenv.run | bash`, follow its shell setup instructions, and restart your terminal. Then select Python:
   ```bash
   pyenv install 3.13.7
   pyenv local 3.13.7
   ```

3. For the Ubuntu Julia setup, the previous environment used Julia `1.11.9`. Inspect the Snap channels and confirm the desired version before installing:
   ```bash
   snap info julia
   sudo snap install julia --classic --channel=lts/stable
   ```

4. From the repository root with your Python environment active, review `PySRRegressor(...)` in `main.py`, then start training:
   ```bash
   python main.py
   ```
   The first run may take longer while Julia initializes its packages and environment. `sr.py` contains the shared functions; the training entry point is `main.py`.

5. To inspect an existing saved run, set `RUN_DIR` and `EXPRESSION_ID` in `plot_sr.py`, then run:
   ```bash
   python plot_sr.py
   ```
   Saved-run inspection requires the corresponding local output files. It displays plots with saving disabled by default.

Training outputs are in `output/<RUN_ID>/`, expression exports in `output/<RUN_ID>/<Expression_ID>/`, and plots in `output/<RUN_ID>/plots/`. The repository-root `.run_num1_logger.csv` records the winning expression for each finalized run.

## About the project

Read more in the [repository Wiki](https://github.com/wadewolfie999/pysr_ext_higgs/wiki).

## Featured recorded result

**HP saved record · equation 43 · complexity 58**<br>
Highest recorded **total ROC-AUC** among the 15 saved score tables inspected. The run note records approximately **11 hours** of running.

| Training AUC | Recorded test AUC | **Total AUC · selection measure** |
|:---:|:---:|:---:|
| 0.962959 | 0.965642 | **0.965162** |

> Selection used total AUC; the recorded test score is not established as an independent performance estimate. Original split membership is unverified.

## The expression

The full saved expression is written below using intermediate quantities to keep it readable. Here $x$ and $z$ are the numerical values of $m_{\chi_1}$ and $m_{\chi_1^\pm}$ in GeV. The output is a **raw score**, not a probability.

```math
\begin{aligned}
s(x,z)&=\cos\!\left(AV^6W^3\right),\\
A&=-\cos B\\
 &\quad-0.587758126965164.
\end{aligned}
```

<details>
<summary><strong>Expand the full expression · saved coefficients retained</strong></summary>

Long definitions can be scrolled horizontally on small screens.

```math
E=\exp\!\left(0.6395393569247805\,x\left[(x-z)^3+0.005627519890117061\right]\right),
```

```math
C=\cos\!\left(4.4078088991239108\times10^{-26}\,z^9\right),
```

```math
B=-0.00415914734118997\,x+\left(E-0.25362280030866624\right)C,
```

```math
V=\cos\!\left(-3.656044798756617\times10^{-10}\,z^3\right),
```

```math
W=\cos\!\left(\frac{1.2077042267298759\times10^{-17}\,x^6}{-1.6053572398241938}\right).
```

This factorization is checked against the full-precision saved expression by the [export helper](docs/showcase/build_showcase.py). The original export's rounded `tex_expr` is retained in the [source table](docs/showcase/recorded-auc-scores.csv); it is not used to calculate the figures.

</details>

## Results at a glance

The figure and source links below refer to local `docs/` artifacts. That directory is ignored by Git and is not included in a fresh clone.

![ROC for HP equation 43 on all 12,280 current data rows, reproducing total AUC 0.965162.](docs/showcase/roc.svg)

*Full-data ROC, reproduced from the saved expression. This is descriptive evaluation on the full dataset, not a new held-out test.*

![Observed neutral and charged mass pairs: equation-43 scores beside the stored binary reference labels.](docs/showcase/mass-plane.svg)

*The same 12,280 observed mass pairs in both panels. Colours show the full score range on the left and stored `exclusion` labels on the right; no interpolation or probability calibration is applied.* [Open full-size figure](docs/showcase/mass-plane.svg).

---

[Setup and running](docs/wiki-src/Setup-and-running.md) · [Result details and limitations](docs/wiki-src/Featured-result-and-limitations.md) · [Source records](docs/showcase/README.md)

<sub>README v0.3.0 · Code release v5.3.0.</sub>
