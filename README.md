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


### 6. Review the data and search settings

- **Dataset:** [data/masses_exclusions.csv](data/masses_exclusions.csv), with the columns `mchi1`, `mchipm1`, and `exclusion`.


### 7. Start the search


### 8. Find your results

Each search gets a run ID, such as `L2HL_1`. Its outputs are organized as follows:

```text
output/<RUN_ID>/
├── hall_of_fame.csv             # Candidate equations
├── run_metadata.json           # Data, split, and search metadata
```

The root `.run_num1_logger.csv` records the winning expression for each finalized run.

## Where outputs go

| Location | What you will find |
|---|---|
| `output/<RUN_ID>/` | New local runs, checkpoints, exports, and plots; ignored by Git |
| `results/L2HL_1_050/` | The selected expression's committed text exports, candidate table, and manifest |
| [Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry) | The selected result, score table, figures, and downloads |

## Read more

- **[Wiki Home](https://github.com/wadewolfie999/pysr_ext_higgs/wiki):** a short guide to the documentation.
- **[Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry):** the current selected expression and its results.
- **[Methods and limitations](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Method-and-Limitations):** the loss, evaluation procedure, and interpretation of the reported scores.
- **[Issues](https://github.com/wadewolfie999/pysr_ext_higgs/issues):** questions, problems, and feedback.

<sub>README v0.8.1 · Code release v5.7.0.</sub>
