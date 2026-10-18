# Local PySR environment

Document version: 0.0.4

Assumes the project Python virtual environment is active.
Open this folder in VS Code and use the corresponding notebook kernel.

## Configuration

`.env` defines the Julia executable, Julia project, and thread count.
The default is `PYTHON_JULIACALL_THREADS=4`.
VS Code loads it through `python.envFile` and `python.terminal.useEnvFile`.

To change threads, edit `.env`, save, and create a new integrated terminal
or restart an idle notebook kernel. Existing processes retain their settings.
External terminals do not automatically load this file.

## Import check

```sh
python verify-julia-env.py
```

For notebooks, run the single cell in `verify-julia-env.ipynb`.
Both VS Code paths were verified with four, six, then four Julia threads.
The checks import PySR and inspect the runtime without training a model.

## Rollback

Restore the previous Julia environment assignments before importing PySR,
remove the two VS Code environment settings, and move `.env` aside.
Then create new terminals or restart idle notebook kernels.
