# Version v5.3.0
import ast
from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

os.environ.setdefault("MPLBACKEND", "Agg")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
import sympy as sp
import sr


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.features = ["mchi1", "mchipm1"]
        self.X = pd.DataFrame({"mchi1": np.arange(1, 37, dtype=float), "mchipm1": 100.0})
        self.y = pd.Series([0] * 18 + [1] * 18)
        self.datasets = {name: (self.X.copy(), self.y.copy()) for name in sr.SPLITS}
        self.HOF = pd.DataFrame({"Complexity": [1, 2, 3, 4], "Loss": [0.1] * 4,
                                 "Equation": ["mchi1", "-mchi1", "0.5", "sqrt(-mchi1)"]})
        self.HOF_01 = sr.expr_indexer(self.HOF, "TEMP_1", self.features)
        self.HOF_02, self.evaluations = sr.auc_recorder(self.HOF_01, self.datasets)
        self.HOF_03, self.winner = sr.top_three_sort(self.HOF_02)

    def tearDown(self):
        plt.close("all")
        self.temp.cleanup()

    def export(self, run_id="TEMP_1", winner=None):
        table = self.HOF_03.copy()
        table["Expression_ID"] = table["Expression_ID"].str.replace("TEMP_1", run_id, regex=False)
        run = self.root / "output" / run_id
        first = sr.expr_expander(table, run, self.features)
        second = sr.expr_pdf_compiler(table, winner or table.iloc[0]["Expression_ID"], run)
        return first, second, run

    def test_csv_and_native_model_inputs(self):
        self.assertEqual(self.HOF_01["Expression_ID"].tolist(), [f"TEMP_1_0{i}" for i in range(1, 5)])
        native = self.HOF.rename(columns=str.lower)
        native["sympy_format"] = self.HOF_01["SymPy_Equation"]
        native["lambda_format"] = self.HOF_01["Lambda_Equation"]
        normalized = sr.expr_indexer(native, "TEMP_2", self.features)
        self.assertIs(normalized.iloc[0]["Lambda_Equation"], native.iloc[0]["lambda_format"])
        self.assertEqual(normalized.iloc[0]["SymPy_Equation"], sp.Symbol("mchi1"))
        self.assertEqual(self.HOF.columns.tolist(), ["Complexity", "Loss", "Equation"])

    def test_invalid_hof_and_features(self):
        for table in [self.HOF.iloc[:0], self.HOF.drop(columns="Equation"),
                      self.HOF.assign(Complexity=[1, 1, 3, 4]), self.HOF.assign(Complexity=[1, 2.5, 3, 4])]:
            with self.subTest(table=table), self.assertRaises(ValueError):
                sr.expr_indexer(table, "TEMP_1", self.features)
        for names in [[], ["mchi1", "mchi1"], ["numpy"], ["class"]]:
            with self.subTest(names=names), self.assertRaises(ValueError):
                sr.expr_indexer(self.HOF, "TEMP_1", names)
        with self.assertRaises(ValueError):
            sr.expr_indexer(self.HOF, "../run", self.features)
        with self.assertRaises(ValueError):
            sr.expr_indexer(self.HOF.assign(Equation="unknown + 1"), "TEMP_1", self.features)

    def test_auc_values_nonfinite_retention_and_ranking(self):
        np.testing.assert_allclose(self.HOF_02["test_auc"].iloc[:3], [1, 0, 0.5])
        self.assertTrue(self.HOF_02[list(sr.SPLITS.values())].iloc[3].isna().all())
        self.assertEqual(len(self.evaluations["TEMP_1_04"]["test"]["scores"]), len(self.X))
        self.assertEqual(self.HOF_03["Expression_ID"].tolist(), ["TEMP_1_01", "TEMP_1_03", "TEMP_1_02"])
        self.assertEqual(self.winner, "TEMP_1_01")
        self.assertEqual(len(sr.top_three_sort(self.HOF_02.iloc[[0, 3]])[0]), 1)
        with self.assertRaises(ValueError):
            sr.top_three_sort(self.HOF_02.iloc[[3]])
        tied = self.HOF_02.iloc[:3].copy()
        tied[list(sr.SPLITS.values())] = 0.5
        self.assertEqual(sr.top_three_sort(tied)[0]["Expression_ID"].tolist(), tied["Expression_ID"].tolist())
        for name, metric in sr.SPLITS.items():
            self.assertEqual(self.HOF_02.iloc[0][metric], roc_auc_score(self.y, self.evaluations[self.winner][name]["scores"]))

    def test_score_evaluation_once_and_plotting_without_writes(self):
        counter = {"calls": 0}
        def counted(X):
            counter["calls"] += 1
            return X["mchi1"].to_numpy()
        table = self.HOF_01.iloc[[0]].copy()
        table["Lambda_Equation"] = [counted]
        _, evaluated = sr.auc_recorder(table, self.datasets)
        self.assertEqual(counter["calls"], 4)
        with patch.object(Figure, "savefig", side_effect=AssertionError("unexpected save")), \
             patch("sr.plt.show", side_effect=AssertionError("unexpected show")), \
             patch("sr.save_plot", side_effect=AssertionError("unexpected saver")):
            sr.plot_roc_curve(self.winner, evaluated)
            sr.plot_roc_curve(self.winner, evaluated, magnified=True)
            sr.plot_mass_plane(self.winner, self.datasets, evaluated)
            _, _, folds, summary, positions = sr.plot_expr_folds_variability(self.winner, self.datasets, evaluated)
            self.assertEqual(counter["calls"], 4)
            scan = self.X.copy()
            sr.plot_1d_mass(counted, scan)
            self.assertEqual(counter["calls"], 5)
        self.assertEqual(len(folds), 6)
        self.assertEqual(summary["rows"], len(self.X))
        np.testing.assert_array_equal(np.sort(np.concatenate(positions)), np.arange(len(self.X)))
        repeat = sr.plot_expr_folds_variability(self.winner, self.datasets, evaluated)[-1]
        for first, second in zip(positions, repeat):
            np.testing.assert_array_equal(first, second)

    def test_dataset_and_plot_boundaries(self):
        invalid = dict(self.datasets, test=(self.X, self.y.iloc[::-1]))
        with self.assertRaises(ValueError):
            sr.auc_recorder(self.HOF_01, invalid)
        with self.assertRaises(ValueError):
            sr.auc_recorder(self.HOF_01, {"test": (self.X, self.y)})
        with self.assertRaises(ValueError):
            sr.auc_recorder(self.HOF_01, {name: (self.X, self.y * 0) for name in sr.SPLITS})
        with self.assertRaises(ValueError):
            sr._scores(lambda X: np.ones((len(X), 2)), self.X)
        with self.assertRaises(ValueError):
            sr._scores(lambda X: np.full(len(X), 1j), self.X)
        for zoom in [(0.5, 0.1), (np.nan, 0.5)]:
            with self.assertRaises(ValueError):
                sr.plot_roc_curve(self.winner, self.evaluations, True, zoom=zoom)
        with self.assertRaises(ValueError):
            sr.plot_expr_folds_variability(self.winner, self.datasets, self.evaluations, n_splits=19)
        with self.assertRaises(ValueError):
            sr.plot_mass_plane(self.winner, self.datasets, self.evaluations, metrics=())
        with self.assertRaises(ValueError):
            sr.plot_1d_mass(lambda X: X.mchi1, self.X.assign(mchipm1=np.arange(len(self.X))))
        with self.assertRaises(ValueError):
            sr.plot_1d_mass(lambda X: np.nan, self.X)
        _, ax = sr.plot_1d_mass(lambda X: np.where(X.mchi1 < 10, np.nan, X.mchi1), self.X)
        self.assertTrue(np.isnan(ax.lines[0].get_ydata()[:9]).all())

    def test_standalone_exports_and_precision(self):
        first = sr.expr_expander(self.HOF_03, self.root / "output/TEMP_1", self.features)
        self.assertEqual(len(first), 3)
        self.assertEqual(len(list(self.root.rglob("expression_lambda.py"))), 3)
        self.assertFalse(list(self.root.rglob("*.pdf")))
        for _, row in first.iterrows():
            spec = importlib.util.spec_from_file_location("exported_expression", row["Lambda"])
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            original = self.HOF_03.set_index("Expression_ID").loc[row["Expression_ID"], "Lambda_Equation"]
            expected = sr._scores(original, self.X)
            np.testing.assert_allclose(module.predict(self.X[self.features[::-1]]), expected)
            self.assertEqual(module.FEATURES, tuple(self.features))
        precise = sr.expr_indexer(pd.DataFrame({"Complexity": [9], "Loss": [0.1],
                    "Equation": ["0.12345678901234567 * mchi1"]}), "TEMP_1", self.features)
        precise["test_auc"] = 1.0
        exported = sr.expr_expander(precise, self.root / "output/TEMP_1", self.features).iloc[0]
        self.assertIn("0.12345678901234567", exported["SymPy"].read_text())

    @unittest.skipUnless(shutil.which("pdflatex"), "pdflatex unavailable")
    def test_pdf_and_logger_history_same_run_replacement(self):
        logger = self.root / ".run_num1_logger.csv"
        logger.touch()
        first, second, run = self.export()
        self.assertEqual(len(list(run.rglob("*.pdf"))), 1)
        self.assertTrue((run / self.winner / "expression.pdf").read_bytes().startswith(b"%PDF"))
        final = sr.run_finalizer(first, second, "TEMP_1", logger)
        self.assertEqual(final.columns.tolist(), ["Expression_ID", "Complexity", "Loss", "test_auc", "SymPy", "Lambda", "TeX", "PDF"])
        self.assertTrue(all(not Path(final.iloc[0][key]).is_absolute() for key in ["SymPy", "Lambda", "TeX", "PDF"]))
        other_first, other_second, _ = self.export("TEMP_10")
        sr.run_finalizer(other_first, other_second, "TEMP_10", logger)
        new_second = sr.expr_pdf_compiler(self.HOF_03, "TEMP_1_03", run)
        sr.run_finalizer(first, new_second, "TEMP_1", logger)
        sr.run_finalizer(first, new_second, "TEMP_1", logger)
        self.assertEqual(pd.read_csv(logger)["Expression_ID"].tolist(), ["TEMP_10_01", "TEMP_1_03"])
        before = logger.read_bytes()
        with patch.object(Path, "replace", side_effect=OSError("test replacement failure")), self.assertRaises(OSError):
            sr.run_finalizer(first, new_second, "TEMP_1", logger)
        self.assertEqual(logger.read_bytes(), before)
        self.assertFalse(list(self.root.glob("*.tmp")))

    @unittest.skipUnless(shutil.which("pdflatex"), "pdflatex unavailable")
    def test_compilation_failure_preserves_tex_diagnostics_and_logger(self):
        logger = self.root / ".run_num1_logger.csv"
        logger.write_text("prior contents\n")
        run = self.root / "output/TEMP_1"
        sr.expr_expander(self.HOF_03, run, self.features)
        with patch("sr.sp.latex", return_value=r"\UnknownExpressionCommand"), self.assertRaises(RuntimeError):
            sr.expr_pdf_compiler(self.HOF_03, self.winner, run)
        self.assertTrue((run / self.winner / "expression.tex").is_file())
        self.assertTrue((run / self.winner / "expression.log").is_file())
        self.assertEqual(logger.read_text(), "prior contents\n")

    def test_save_is_explicit(self):
        fig, _ = sr.plot_roc_curve(self.winner, self.evaluations)
        path = sr.save_plot(fig, "roc.pdf", self.root, dpi=50)
        self.assertTrue(path.is_file())
        self.assertTrue(path.with_suffix(".png").is_file())


class EntryPointTests(unittest.TestCase):
    def test_imports_do_not_allocate_run_or_import_pysr(self):
        code = ("import sys; from pathlib import Path; "
                f"sys.path.insert(0, {str(ROOT)!r}); "
                "import sr, main, plot_sr; "
                "assert 'pysr' not in sys.modules and 'juliacall' not in sys.modules; "
                "assert not list(Path('.').iterdir())")
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run([sys.executable, "-B", "-c", code], cwd=directory, check=True,
                           env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})

    def test_utilities_and_training_configuration_are_unchanged(self):
        original = subprocess.check_output(["git", "show", "e29c896:sr.py"], cwd=ROOT, text=True)
        current = (ROOT / "sr.py").read_text()
        for name in ["run_id_ledger", "do_split"]:
            old = next(n for n in ast.parse(original).body if isinstance(n, ast.FunctionDef) and n.name == name)
            new = next(n for n in ast.parse(current).body if isinstance(n, ast.FunctionDef) and n.name == name)
            self.assertEqual(ast.get_source_segment(original, old), ast.get_source_segment(current, new))
        previous_main = subprocess.check_output(["git", "show", "e29c896:main.py"], cwd=ROOT, text=True)
        previous_main = previous_main.replace("from sr import expr_indexer, ", "from sr import expr_indexer")
        def config(source):
            return next(n for n in ast.walk(ast.parse(source)) if isinstance(n, ast.Call)
                        and isinstance(n.func, ast.Name) and n.func.id == "PySRRegressor")
        self.assertEqual(ast.dump(config(previous_main)), ast.dump(config((ROOT / "main.py").read_text())))

    def test_notebook_and_script_on_saved_expression_without_writes(self):
        import plot_sr
        before_logger = (ROOT / ".run_num1_logger.csv").read_bytes()
        before_counter = (ROOT / ".run_id_counter").read_bytes()
        with patch.object(plot_sr, "SHOW_PLOTS", False), patch.object(Figure, "savefig", side_effect=AssertionError("unexpected save")), redirect_stdout(io.StringIO()):
            plot_sr.main()
        nb = json.loads((ROOT / "plot.ipynb").read_text())
        namespace = {}
        for cell in nb["cells"]:
            if cell.get("cell_type") == "code":
                code = "".join(cell["source"])
                tree = ast.parse(code)
                # Exercise a fixed saved fixture without changing the user's notebook settings or outputs.
                settings = {"RUN_DIR": f"Path({str(ROOT / 'output/TEMP_4')!r})",
                            "EXPRESSION_ID": repr("TEMP_4_0118"), "SAVE_PLOTS": "False", "SHOW_PLOTS": "False"}
                for node in tree.body:
                    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                        if node.targets[0].id in settings:
                            node.value = ast.parse(settings[node.targets[0].id], mode="eval").body
                ast.fix_missing_locations(tree)
                with patch.object(Figure, "savefig", side_effect=AssertionError("unexpected save")), patch.object(plt, "show"), redirect_stdout(io.StringIO()):
                    exec(compile(tree, "plot.ipynb", "exec"), namespace)
        self.assertEqual(namespace["HOF_02"].iloc[0]["Expression_ID"], "TEMP_4_0118")
        _, labels = namespace["datasets"]["total"]
        scores = namespace["evaluations"]["TEMP_4_0118"]["total"]["scores"]
        self.assertAlmostEqual(namespace["HOF_02"].iloc[0]["total_auc"], roc_auc_score(labels, scores))
        self.assertEqual((ROOT / ".run_num1_logger.csv").read_bytes(), before_logger)
        self.assertEqual((ROOT / ".run_id_counter").read_bytes(), before_counter)
        plt.close("all")

    @unittest.skipUnless(shutil.which("pdflatex"), "pdflatex unavailable")
    def test_training_entrypoint_with_fake_model_and_run_collision(self):
        import main
        with tempfile.TemporaryDirectory() as directory:
            root, previous = Path(directory).resolve(), Path.cwd()
            (root / "data").mkdir()
            pd.DataFrame({"mchi1": np.arange(1, 121), "mchipm1": 2000.0,
                          "exclusion": [0] * 60 + [1] * 60}).to_csv(root / "data/masses_exclusions.csv", index=False)
            fitted = []
            class FakeModel:
                def __init__(self, **options):
                    self.equations_ = pd.DataFrame({"complexity": [1, 2, 3], "loss": [0.1] * 3,
                                                    "equation": ["mchi1", "-mchi1", "0.5"]})
                def fit(self, X, y, *, weights):
                    fitted.append((len(X), len(y), len(weights)))
            try:
                os.chdir(root)
                with patch.object(main, "PROJECT_DIR", root), patch.object(main, "SAVE_PLOTS", False), \
                     patch.dict(sys.modules, {"pysr": types.SimpleNamespace(PySRRegressor=FakeModel)}), redirect_stdout(io.StringIO()):
                    main.main()
                    (root / "output/TEMP_2").mkdir()
                    with self.assertRaises(FileExistsError):
                        main.main()
                self.assertEqual(fitted, [(72, 72, 72)])
                self.assertEqual(pd.read_csv(root / ".run_num1_logger.csv").iloc[0]["Expression_ID"], "TEMP_1_01")
                self.assertFalse(list((root / "output").rglob("*curve.pdf")))
            finally:
                os.chdir(previous)
                plt.close("all")


if __name__ == "__main__":
    unittest.main()
