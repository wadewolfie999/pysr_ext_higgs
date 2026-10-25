# PySR in Extended Higgs Sector Models

## How to run this in your machine

1. Clone the project:
   ```bash
   cd "$HOME/path/to/destination"
   git clone https://github.com/wadewolfie999/pysr-ext-higgs
   cd pysr-ext-higgs
   ```

2. Check Python; the expected version is `3.13.7`:
   ```bash
   python --version
   ```

3. If needed, install pyenv:
   ```bash
   curl -fsSL https://pyenv.run | bash
   ```
   Follow its shell setup instructions, then restart your terminal.

4. From the project directory, install and select Python 3.13.7:
   ```bash
   pyenv install 3.13.7
   pyenv local 3.13.7
   python --version
   ```
5. Download the Julia 1.11.9 on Ubuntu via snap:
   ```bash
   snap info julia   # Double Check the v1.11.9 is indeed the channel below
   sudo snap install julia --classic --channel=lts/stable
   ```
6. From the project directory, Run `python sr.py` for the first time so Julia initializes and configures its packages and environment
     - The first run might take a little longer
7. Change the `model = PySRRegressor(...)` at will and then enter
   ```python
   python sr.py
   ```
   to run again.
8. All pysr outputs are in `output/<run_id>`
     - plots are in `output/<run_id>/plots`


## About the Project
*You can read more in the [repo's Wiki](https://github.com/wadewolfie999/pysr_ext_higgs/wiki)*


README version 0.1.0 
