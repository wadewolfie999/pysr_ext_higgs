"""Research-workflow regression tests, version 0.2.0. Never fit a real model."""
import csv
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator

import sr

ROOT = Path(__file__).resolve().parents[1]
IDS = ("EXP_6_072", "ELEM_7_0198", "L2HL_1_050", "L2HL_2_0235")
BASE_COLUMNS = ["Expression_ID", "Complexity", "Loss", "test_auc", "SymPy", "Lambda", "TeX", "PDF"]


class LoggerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.logger = self.root / "logger.csv"
        self.row = dict(zip(BASE_COLUMNS, ["L2HL_1_050", "50", "0.3", "0.96", "s.txt", "l.py", "e.tex", "e.pdf"]))
        for name in ("SymPy", "Lambda", "TeX", "PDF"):
            (self.root / self.row[name]).write_text("fixture\n")
        self.exports = pd.DataFrame([{**{k: self.row[k] for k in BASE_COLUMNS[:4]},
                                     **{k: self.root / self.row[k] for k in ("SymPy", "Lambda")}}])
        self.pdf = pd.DataFrame([{k: self.row[k] if k == "Expression_ID" else self.root / self.row[k]
                                  for k in ("Expression_ID", "TeX", "PDF")}])

    def write_logger(self, curve=None):
        row = dict(self.row)
        if curve is not None:
            row["validation_learning_curve"] = curve
        with self.logger.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(row))
            writer.writeheader()
            writer.writerow(row)

    def test_legacy_logger_is_upgraded_and_repeat_does_not_duplicate(self):
        self.write_logger()
        for _ in range(2):
            sr.run_finalizer(self.exports, self.pdf, "L2HL_1", self.logger)
        saved = pd.read_csv(self.logger, keep_default_na=False)
        self.assertEqual(len(saved), 1)
        self.assertEqual(saved.validation_learning_curve.tolist(), [""])

    def test_current_logger_curve_path_and_other_decimal_text_survive(self):
        self.write_logger(" - ")
        other = dict(self.row, Expression_ID="EXP_6_072", test_auc="0.9637619186481049",
                     validation_learning_curve="")
        with self.logger.open("a", newline="") as stream:
            csv.DictWriter(stream, fieldnames=[*BASE_COLUMNS, "validation_learning_curve"]).writerow(other)
        curve = self.root / "curve.png"
        curve.write_bytes(b"fixture")
        sr.run_finalizer(self.exports, self.pdf, "L2HL_1", self.logger,
                         validation_learning_curve=curve)
        saved = pd.read_csv(self.logger, dtype=str, keep_default_na=False)
        self.assertEqual(saved.loc[saved.Expression_ID == self.row["Expression_ID"],
                                   "validation_learning_curve"].item(), "curve.png")
        self.assertEqual(saved.loc[saved.Expression_ID == "EXP_6_072", "test_auc"].item(),
                         "0.9637619186481049")

    def test_invalid_schema_or_missing_curve_preserves_original(self):
        self.write_logger()
        original = self.logger.read_bytes()
        with self.assertRaises(FileNotFoundError):
            sr.run_finalizer(self.exports, self.pdf, "L2HL_1", self.logger,
                             validation_learning_curve=self.root / "missing.png")
        self.assertEqual(original, self.logger.read_bytes())
        self.logger.write_text(self.logger.read_text().replace("test_auc", "wrong"))
        original = self.logger.read_bytes()
        with self.assertRaises(ValueError):
            sr.run_finalizer(self.exports, self.pdf, "L2HL_1", self.logger)
        self.assertEqual(original, self.logger.read_bytes())

    def test_same_winner_keeps_existing_curve_when_optional_argument_is_omitted(self):
        (self.root / "curve.png").write_bytes(b"fixture")
        self.write_logger(" curve.png ")
        sr.run_finalizer(self.exports, self.pdf, "L2HL_1", self.logger)
        saved = pd.read_csv(self.logger, dtype=str, keep_default_na=False)
        self.assertEqual(saved.validation_learning_curve.item(), "curve.png")

    def test_write_failure_preserves_original_and_removes_temporary(self):
        self.write_logger("-")
        original = self.logger.read_bytes()
        with patch.object(pd.DataFrame, "to_csv", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                sr.run_finalizer(self.exports, self.pdf, "L2HL_1", self.logger)
        self.assertEqual(original, self.logger.read_bytes())
        self.assertEqual(list(self.root.glob("*.tmp")), [])


class SavedExpressionTests(unittest.TestCase):
    def test_test_auc_remains_the_selection_metric(self):
        candidates = pd.DataFrame({"Expression_ID": ["a", "b"], "train_auc": [.9, .8],
                                   "val_auc": [.99, .6], "test_auc": [.7, .95], "total_auc": [.9, .8]})
        _, winner = sr.top_three_sort(candidates)
        self.assertEqual(winner, "b")

    def test_offline_plotting_rejects_changed_data_and_source_overwrites(self):
        import plot_sr
        with tempfile.TemporaryDirectory() as temporary:
            changed = Path(temporary) / "changed.csv"
            changed.write_bytes((ROOT / "data/masses_exclusions.csv").read_bytes() + b"\n")
            with self.assertRaisesRegex(ValueError, "Dataset differs"):
                plot_sr.main(data_csv=changed, show_plots=False)
        with self.assertRaisesRegex(ValueError, "outside the source evidence"):
            plot_sr.main(save_plots=True, show_plots=False,
                         plot_dir=ROOT / "results/L2HL_1_050/plots")

    def test_raw_run_identity_and_selected_expression(self):
        with tempfile.TemporaryDirectory() as temporary:
            run = Path(temporary) / "RUN_1"
            run.mkdir()
            pd.DataFrame({"Complexity": [1, 2], "Loss": [1., .5],
                          "Equation": ["mchi1", "mchi1 + mchipm1"]}).to_csv(run / "hall_of_fame.csv", index=False)
            selected = sr.load_saved_expression(run, "RUN_1_02")
            X = pd.DataFrame({"mchi1": [1., 2.], "mchipm1": [3., 4.]})
            np.testing.assert_array_equal(selected.iloc[0].Lambda_Equation(X), [4., 6.])
            with self.assertRaises(ValueError):
                sr.load_saved_expression(run, "OTHER_1_02")
            with self.assertRaises(ValueError):
                sr.load_saved_expression(run, "RUN_1_03")

    def test_all_curated_hashes_predictions_and_exact_recorded_test_scores(self):
        batch = ROOT / "results/current-runs-v0.1.0"
        with (batch / "logger.csv").open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(tuple(row["Expression_ID"] for row in rows), IDS)
        frame = pd.read_csv(ROOT / "data/masses_exclusions.csv")
        X, y = frame[["mchi1", "mchipm1"]].astype(float), frame.exclusion.astype(int)
        splits = sr.do_split(X, y)
        datasets = dict(zip(sr.SPLITS, [(splits[i], splits[i + 1]) for i in range(0, 8, 2)]))
        for row in rows:
            with self.subTest(expression=row["Expression_ID"]):
                folder = ROOT / "results" / row["Expression_ID"]
                manifest = json.loads((folder / "manifest.json").read_text())
                for asset in manifest["files"]:
                    asset_path = folder / asset["path"]
                    if not asset_path.exists():
                        self.assertIn(asset_path.suffix, {".png", ".pdf"})
                        continue  # Hosted binaries are optional ignored cache, verified by download tests.
                    content = asset_path.read_bytes()
                    self.assertEqual(hashlib.sha256(content).hexdigest(), asset["sha256"])
                selected = sr.load_saved_expression(folder / "manifest.json", row["Expression_ID"])
                scored, _ = sr.auc_recorder(selected, datasets)
                self.assertEqual(scored.test_auc.item(), float(row["test_auc"]))
                module = runpy.run_path(str(folder / "expression_lambda.py"))
                np.testing.assert_array_equal(selected.iloc[0].Lambda_Equation(X), module["predict"](X))
                self.assertEqual(manifest["diagnostics"]["refitted_curves"]["available"],
                                 row["Expression_ID"].startswith("L2HL_"))

    def test_curated_identity_and_tampering_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary) / "selected"
            shutil.copytree(ROOT / "results/L2HL_1_050", folder)
            with self.assertRaises(ValueError):
                sr.load_saved_expression(folder / "manifest.json", "L2HL_2_0235")
            with (folder / "hall_of_fame.csv").open("a") as stream:
                stream.write("\n")
            with self.assertRaises(ValueError):
                sr.load_saved_expression(folder / "manifest.json", "L2HL_1_050")

    def test_tracked_candidate_only_script_and_notebook_do_not_import_pysr_or_change_assets(self):
        with tempfile.TemporaryDirectory() as temporary:
            isolated = Path(temporary)
            for name in ("sr.py", "plot_sr.py", "plot.ipynb", "fetch_artifacts.py", "data/masses_exclusions.csv"):
                target = isolated / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, target)
            shutil.copytree(ROOT / "results", isolated / "results", ignore=shutil.ignore_patterns("*.png", "*.pdf"))
            program = r'''
import builtins, hashlib, json, pathlib, runpy, sys, urllib.request
import matplotlib.pyplot as plt
real_import = builtins.__import__
def no_training(name, *args, **kwargs):
    if name.split('.')[0] in {'pysr', 'juliacall', 'juliapkg'}:
        raise AssertionError('Training dependency imported: ' + name)
    return real_import(name, *args, **kwargs)
builtins.__import__ = no_training
def no_download(*args, **kwargs):
    raise AssertionError('Ordinary inspection must not download artifacts')
urllib.request.urlopen = no_download
root = pathlib.Path.cwd()
files = [p for p in (root / 'results').rglob('*') if p.is_file()]
before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
import plot_sr
plot_sr.main(show_plots=False)
notebook = json.loads((root / 'plot.ipynb').read_text())
namespace = {'__name__': '__main__'}
plt.show = lambda *args, **kwargs: plt.close('all')
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        exec(compile(''.join(cell['source']), f'plot.ipynb:cell{i}', 'exec'), namespace)
assert not (root / 'output').exists()
assert before == {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
assert namespace['RUN_CURVE_FITS'] is False
assert 'pysr' not in sys.modules
print('PORTABLE_OFFLINE_PASS')
'''
            environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "MPLBACKEND": "Agg"}
            result = subprocess.run([sys.executable, "-c", program], cwd=isolated, env=environment,
                                    text=True, capture_output=True, timeout=120)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("PORTABLE_OFFLINE_PASS", result.stdout)


class ProvenanceTests(unittest.TestCase):
    def test_nondefault_split_seed_and_weight_policy_are_explicit_not_inferred(self):
        X = pd.DataFrame({"mchi1": np.arange(40.), "mchipm1": np.arange(40.) + 1})
        y = pd.Series([0, 1] * 20)
        parts = sr.do_split(X, y, seed=7)
        datasets = dict(zip(sr.SPLITS, [(parts[i], parts[i + 1]) for i in range(0, 8, 2)]))
        with tempfile.TemporaryDirectory() as temporary:
            options = dict(project_dir=ROOT, data_csv=ROOT / "data/masses_exclusions.csv",
                           datasets=datasets, model_parameters={}, training_labels=2 * parts[1] - 1,
                           sample_weights=np.ones(len(parts[1])))
            unknown = json.loads(sr.write_run_metadata(Path(temporary), **options).read_text())
            self.assertIsNone(unknown["split_seed"])
            self.assertIsNone(unknown["weight_policy"])
            path = sr.write_run_metadata(Path(temporary), **options,
                                         split_seed=7, weight_policy="uniform weights")
            record = json.loads(path.read_text())
            self.assertEqual(record["split_seed"], 7)
            self.assertEqual(record["weight_policy"], "uniform weights")
            self.assertEqual(record["splits"]["train"]["row_ids"], parts[0].index.tolist())
            path = sr.write_run_metadata(Path(temporary), **options)
            record = json.loads(path.read_text())
            self.assertIsNone(record["split_seed"])
            self.assertIsNone(record["weight_policy"])

    def test_metadata_records_actual_rows_labels_weights_configuration_and_source_hashes(self):
        X = pd.DataFrame({"mchi1": np.arange(20.), "mchipm1": np.arange(20.) + 1})
        y = pd.Series([0, 1] * 10)
        parts = sr.do_split(X, y)
        datasets = dict(zip(sr.SPLITS, [(parts[i], parts[i + 1]) for i in range(0, 8, 2)]))
        with tempfile.TemporaryDirectory() as temporary:
            path = sr.write_run_metadata(Path(temporary), project_dir=ROOT,
                                         data_csv=ROOT / "data/masses_exclusions.csv", datasets=datasets,
                                         model_parameters={"elementwise_loss": "L2HingeLoss()", "maxsize": 280},
                                         training_labels=2 * parts[1] - 1,
                                         sample_weights=np.ones(len(parts[1])))
            record = json.loads(path.read_text())
            self.assertEqual(record["selection_metric"], "test_auc")
            self.assertEqual(record["splits"]["train"]["row_ids"], parts[0].index.tolist())
            self.assertEqual(record["training_labels"], (2 * parts[1] - 1).tolist())
            self.assertEqual(record["sample_weights"], [1.] * len(parts[1]))
            self.assertEqual(record["model_parameters"]["elementwise_loss"], "L2HingeLoss()")
            self.assertEqual(record["source_hashes"]["sr.py"], hashlib.sha256((ROOT / "sr.py").read_bytes()).hexdigest())


class CurveTests(unittest.TestCase):
    def helper(self):
        import ast
        notebook = json.loads((ROOT / "plot.ipynb").read_text())
        functions = []
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                functions.extend(node for node in ast.parse("".join(cell["source"])).body
                                 if isinstance(node, ast.FunctionDef) and node.name == "plot_pysr_curves")
        self.assertEqual(len(functions), 1)
        namespace = {}
        exec(compile(ast.Module(body=functions, type_ignores=[]), "curve_helper", "exec"), namespace)
        return namespace["plot_pysr_curves"]

    def test_misaligned_training_or_validation_series_fails_before_fitting_or_writing(self):
        class NoFitEstimator(BaseEstimator):
            def __init__(self, maxsize=280, warm_start=True, run_id=None, output_directory=None):
                self.maxsize, self.warm_start = maxsize, warm_start
                self.run_id, self.output_directory = run_id, output_directory
            def fit(self, *args, **kwargs):
                raise AssertionError("A mismatched-label input must never reach fit")

        X = pd.DataFrame({"mchi1": np.arange(40.), "mchipm1": np.arange(40.)})
        labels = pd.Series([0, 1] * 20, index=X.index)
        for train_labels, val_labels in [(labels.iloc[::-1], labels), (labels, labels.iloc[::-1])]:
            with self.subTest(training_aligned=train_labels.index.equals(X.index)):
                with tempfile.TemporaryDirectory() as temporary:
                    destination = Path(temporary) / "must-not-exist"
                    with self.assertRaisesRegex(ValueError, "indices must match"):
                        self.helper()(NoFitEstimator(), X, train_labels, X, val_labels,
                                      output_dir=destination, parent_run_id="fixture")
                    self.assertFalse(destination.exists())

    def test_failed_child_is_recorded_and_existing_destination_is_never_reused(self):
        class FailingEstimator(BaseEstimator):
            def __init__(self, maxsize=280, warm_start=True, run_id=None, output_directory=None):
                self.maxsize, self.warm_start = maxsize, warm_start
                self.run_id, self.output_directory = run_id, output_directory
            def fit(self, X, y, weights):
                raise RuntimeError("synthetic interrupted search")

        X = pd.DataFrame({"mchi1": np.arange(40.), "mchipm1": np.arange(40.)})
        y = np.array([0, 1] * 20)
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "curves"
            with self.assertRaisesRegex(RuntimeError, "synthetic interrupted"):
                self.helper()(FailingEstimator(), X, y, X, y,
                              output_dir=destination, parent_run_id="fixture")
            metadata = json.loads((destination / "curve_manifest.json").read_text())
            self.assertEqual(metadata["status"], "failed")
            self.assertEqual(metadata["children"][-1]["status"], "failed")
            before = (destination / "curve_manifest.json").read_bytes()
            with self.assertRaises(FileExistsError):
                self.helper()(FailingEstimator(), X, y, X, y,
                              output_dir=destination, parent_run_id="fixture")
            self.assertEqual(before, (destination / "curve_manifest.json").read_bytes())

    def test_opted_in_curve_orchestration_uses_stub_and_records_eight_children(self):

        class StubEstimator(BaseEstimator):
            calls = []
            def __init__(self, maxsize=280, warm_start=True, run_id=None, output_directory=None):
                self.maxsize, self.warm_start = maxsize, warm_start
                self.run_id, self.output_directory = run_id, output_directory
            def fit(self, X, y, weights):
                self.calls.append((self.run_id, len(X), set(y), self.maxsize, self.warm_start))
                self.equations_ = pd.DataFrame({"complexity": [1], "loss": [.1], "equation": ["mchi1"]})
                return self
            def predict(self, X):
                return X.mchi1.to_numpy()
            def get_best(self):
                return self.equations_.iloc[0]

        X = pd.DataFrame({"mchi1": np.arange(40.), "mchipm1": np.arange(40.)})
        y = np.array([0, 1] * 20)
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "curves"
            fig, results = self.helper()(StubEstimator(), X, y, X, y,
                                         output_dir=destination, parent_run_id="fixture")
            plt.close(fig)
            self.assertEqual(len(StubEstimator.calls), 8)
            self.assertEqual([call[1] for call in StubEstimator.calls[4:]], [10, 20, 30, 40])
            self.assertTrue(all(call[2] == {-1., 1.} and call[4] is False for call in StubEstimator.calls))
            self.assertEqual(len(set(call[0] for call in StubEstimator.calls)), 8)
            self.assertEqual(results["validation"].shape, (4, 3))
            self.assertEqual(results["learning"].shape, (4, 3))
            metadata = json.loads((destination / "curve_manifest.json").read_text())
            self.assertEqual(len(metadata["children"]), 8)
            self.assertTrue((destination / "validation.csv").is_file())
            self.assertTrue((destination / "learning.csv").is_file())
            self.assertTrue((destination / "valid-learn-curve.png").is_file())


class CatalogueTests(unittest.TestCase):
    def test_batch_and_all_relative_documentation_targets_are_consistent(self):
        import re
        from urllib.parse import urlparse
        batch_path = ROOT / "results/current-runs-v0.1.0/manifest.json"
        batch = json.loads(batch_path.read_text())
        for entry in batch["entries"]:
            asset = batch_path.parent / entry["manifest"]
            self.assertEqual(hashlib.sha256(asset.read_bytes()).hexdigest(), entry["manifest_sha256"])
        self.assertEqual(hashlib.sha256(batch_path.with_name("logger.csv").read_bytes()).hexdigest(),
                         batch["logger_sha256"])
        self.assertEqual(len(batch["withdrawal"]["published_expression_ids"]), 18)
        self.assertEqual(batch["withdrawal"]["already_deleted_tracked_files"], 223)
        pages = [ROOT / "README.md", *sorted((ROOT / "wiki").glob("*.md"))]
        for page in pages:
            for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', page.read_text()):
                parsed = urlparse(target)
                if parsed.scheme:
                    if parsed.netloc == "logs.reshub.lol":
                        prefix = "/pysr-ext-higgs/0.1.0/"
                        self.assertTrue(parsed.path.startswith(prefix), target)
                        relative = parsed.path[len(prefix):]
                        if not relative:
                            continue
                        package = json.loads((ROOT / "deployment/logs-reshub/0.1.0/package-manifest-v0.1.0.json").read_text())
                        self.assertIn(relative, {item["path"] for item in package["files"]}, target)
                        continue
                    if parsed.netloc == "raw.githubusercontent.com" and "/pysr_ext_higgs/main/" in parsed.path:
                        resolved = ROOT / parsed.path.split("/pysr_ext_higgs/main/", 1)[1]
                    elif parsed.netloc == "github.com" and "/pysr_ext_higgs/blob/main/" in parsed.path:
                        resolved = ROOT / parsed.path.split("/pysr_ext_higgs/blob/main/", 1)[1]
                    else:
                        continue
                elif not parsed.path:
                    continue
                else:
                    resolved = page.parent / parsed.path
                    if not resolved.suffix:
                        resolved = resolved.with_suffix(".md")
                self.assertTrue(resolved.is_file(), f"{page.name}: {target}")


if __name__ == "__main__":
    unittest.main()
