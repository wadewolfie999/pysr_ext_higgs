# PySR in Extended Higgs Sector Models

<!-- Keep this README as the introduction and setup guide. Preserve the numbered workflow; detailed results belong in Project Registry and evaluation details in Methods and limitations. -->

Use **PySR** to search for symbolic classifiers in the **inert two-Higgs-doublet model (i2HDM)**, also known as the **Inert Doublet Model (IDM)**. This model extends the Standard Model's Higgs sector and is studied in **beyond-the-Standard-Model (BSM)** physics. The inputs are the neutral and charged mass columns, `mchi1` and `mchipm1` (GeV); the reference target is `exclusion`.

**Want to run the project yourself? Start with the eight steps below.** For the selected expression, plots, and downloads, visit the [Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry).

[Setup and first run](#how-to-run-this-on-your-machine) · [Where outputs go](#where-outputs-go) · [Inspect the saved result](#inspect-the-saved-result) · [Wiki](https://github.com/wadewolfie999/pysr_ext_higgs/wiki)

## How to run this on your machine

*Run these commands in a terminal on macOS or Linux. After cloning, keep the repository root as your working directory.*

### 1. Clone the repository

```bash
git clone https://github.com/wadewolfie999/pysr_ext_higgs.git
cd pysr_ext_higgs
```

### 2. Select Python 3.13.7

This is the Python version used for the project:

```bash
python --version
```

If you already have Python **3.13.7**, continue to step 3. Otherwise, install and configure [pyenv](https://github.com/pyenv/pyenv#installation), then run:

```bash
pyenv install -s 3.13.7
pyenv local 3.13.7
python --version
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
python --version
```

Keep this environment active for the remaining steps. In a new terminal, return to the repository and run `source .venv/bin/activate` again.

### 4. Install the Python dependencies

```bash
python -m pip install -r requirements.txt
python -m pip show pysr
```

The committed requirements pin **PySR 2.7.0** along with the other Python packages used by the project.

### 5. Prepare Julia and the PDF compiler

**Julia:** PySR uses Julia for the equation search. On macOS, this project has used PySR's automatic Julia installation and initialization. The first import can take longer while the runtime and packages are prepared:

```bash
python -c "from pysr import PySRRegressor; print('PySR is ready')"
```

See the [PySR installation guide](https://github.com/astroautomata/PySR#installation) if initialization fails.

<details>
<summary><strong>Ubuntu: the earlier Julia 1.11.9 setup</strong></summary>

The earlier Linux environment required **Julia 1.11.9**. This is an environment note, rather than a Julia version pinned for every platform. If using that Ubuntu Snap route, first inspect the channel:

```bash
snap info julia
```

Only if `lts/stable` provides the version you intend to use, install it and check the result:

```bash
sudo snap install julia --classic --channel=lts/stable
julia --version
```

</details>

**Expression PDFs:** The training pipeline also needs a TeX installation providing `pdflatex`. Check it **before starting a search**:

```bash
pdflatex --version
```

If this command is missing, install a TeX distribution for your operating system. Without it, the pipeline stops at PDF export after fitting and retains the TeX source.

### 6. Review the data and search settings

- **Dataset:** [data/masses_exclusions.csv](data/masses_exclusions.csv), with the columns `mchi1`, `mchipm1`, and `exclusion`.
- **Search configuration:** `PySRRegressor(...)` in [main.py](main.py). Adjust the loss, operators, complexity limit, iterations, and time budget here.
- **Shared functions:** [sr.py](sr.py) handles splitting, scoring, expression exports, and plotting.

The current search uses `L2HingeLoss()` and a time budget of up to **one hour**. Review these settings before running it.

### 7. Start the search

From the repository root, with `.venv` active:

```bash
python main.py
```

**This starts a new training run.** The terminal shows search progress and, on completion, the finalized expression table. Julia's first initialization may add startup time.

*`main.py` is the training entry point; `sr.py` is the shared module.*

### 8. Find your results

Each search gets a run ID, such as `L2HL_1`. Its outputs are organized as follows:

```text
output/<RUN_ID>/
├── hall_of_fame.csv             # Candidate equations
├── run_metadata.json           # Data, split, and search metadata
├── <Expression_ID>/            # Selected expression exports
│   ├── expression_sympy.txt
│   ├── expression_lambda.py
│   ├── expression.tex          # Winner only
│   └── expression.pdf          # Winner only
└── plots/                      # Winner's diagnostic plots
```

The root `.run_num1_logger.csv` records the winning expression for each finalized run.

## Where outputs go

| Location | What you will find |
|---|---|
| `output/<RUN_ID>/` | New local runs, checkpoints, exports, and plots; ignored by Git |
| `results/L2HL_1_050/` | The selected expression's committed text exports, candidate table, and manifest |
| [Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry) | The selected result, score table, figures, and downloads |

## Inspect the saved result

**To inspect the existing expression without a new search**, complete the Python setup through step 4, then run:

```bash
python plot_sr.py
```

The script is configured for **`L2HL_1_050`**. It prints the split ROC-AUCs and displays the ROC, mass-plane, mass-scan, and validation-subset plots. It uses the committed expression and dataset; Julia, checkpoints, and `pdflatex` are unnecessary for this path. Plot saving is off by default.

For your own saved run, edit `RUN_SOURCE` and `EXPRESSION_ID` in [plot_sr.py](plot_sr.py) to point to `output/<RUN_ID>/` and one of its expression IDs. For a curated manifest, the script checks the dataset fingerprint before evaluating it.

**Notebook alternative:** [plot.ipynb](plot.ipynb) provides interactive inspection. Set **`RUN_CURVE_FITS = False` before running all cells** if you only want to inspect saved results. Enabling it starts fresh diagnostic searches and requires the corresponding local checkpoint, which is absent from a fresh clone.

<details>
<summary><strong>Optional: download the published plots and expression PDF</strong></summary>

The published binary artifacts are hosted separately. To cache them locally:

```bash
python fetch_artifacts.py --expression L2HL_1_050
```

The downloader verifies each file's byte count and SHA-256 against the committed manifest. Ordinary saved-result inspection does not need this download.

</details>

## Read more

- **[Wiki Home](https://github.com/wadewolfie999/pysr_ext_higgs/wiki):** a short guide to the documentation.
- **[Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry):** the current selected expression and its results.
- **[Methods and limitations](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Method-and-Limitations):** the loss, evaluation procedure, and interpretation of the reported scores.
- **[Issues](https://github.com/wadewolfie999/pysr_ext_higgs/issues):** questions, problems, and feedback.

<sub>README v0.8.1 · Code release v5.7.0.</sub>
