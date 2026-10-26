"""Artifact-store contract tests, version 0.1.0. No public network or model fits."""
import hashlib
from io import BytesIO
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]


class InterruptedResponse(BytesIO):
    def read(self, size=-1):
        if self.tell():
            raise OSError("connection interrupted")
        return super().read(3)


class ArtifactStoreTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location("fetch_artifacts", ROOT / "fetch_artifacts.py")
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name).resolve()
        self.folder = self.root / "results/L2HL_1_050"
        self.folder.mkdir(parents=True)
        self.content = b"curated fixture binary"
        self.entry = {"path": "plots/roc_curve.png", "bytes": len(self.content),
                      "sha256": hashlib.sha256(self.content).hexdigest()}
        self.manifest = {"expression_id": "L2HL_1_050", "files": [self.entry]}
        self.write_manifest()

    def write_manifest(self):
        (self.folder / "manifest.json").write_text(json.dumps(self.manifest))

    def fetch(self):
        return self.module.fetch_expression("L2HL_1_050", project_dir=self.root)

    def test_download_verifies_checksum_and_skips_valid_cache(self):
        with patch.object(self.module, "urlopen", return_value=BytesIO(self.content)) as transport:
            files = self.fetch()
            self.assertEqual(files, [self.folder / self.entry["path"]])
            self.assertEqual(files[0].read_bytes(), self.content)
            self.assertIn("https://logs.reshub.lol/pysr-ext-higgs/0.1.0/", transport.call_args.args[0])
        with patch.object(self.module, "urlopen", side_effect=AssertionError("unexpected network")):
            self.assertEqual(self.fetch(), files)

    def test_wrong_hash_preserves_existing_file_and_removes_partial(self):
        target = self.folder / self.entry["path"]
        target.parent.mkdir()
        target.write_bytes(b"old local bytes")
        with patch.object(self.module, "urlopen", return_value=BytesIO(b"x" * len(self.content))):
            with self.assertRaises(ValueError):
                self.fetch()
        self.assertEqual(target.read_bytes(), b"old local bytes")
        self.assertEqual(list(self.folder.rglob("*.part")), [])
        self.assertIsNone(self.module.cached_artifact("L2HL_1_050", self.entry["path"], project_dir=self.root))

    def test_interruption_does_not_leave_a_completed_or_partial_file(self):
        with patch.object(self.module, "urlopen", return_value=InterruptedResponse(self.content)):
            with self.assertRaises(OSError):
                self.fetch()
        self.assertFalse((self.folder / self.entry["path"]).exists())
        self.assertEqual(list(self.folder.rglob("*.part")), [])

    def test_short_or_oversized_responses_are_rejected(self):
        for payload in (self.content[:-1], self.content + b"extra"):
            with self.subTest(length=len(payload)):
                with patch.object(self.module, "urlopen", return_value=BytesIO(payload)):
                    with self.assertRaises(ValueError):
                        self.fetch()
                self.assertFalse((self.folder / self.entry["path"]).exists())

    def test_http_error_leaves_existing_cache_untouched(self):
        with patch.object(self.module, "urlopen", side_effect=HTTPError("fixture", 404, "not found", {}, None)):
            with self.assertRaises(HTTPError):
                self.fetch()
        self.assertEqual(list(self.folder.rglob("*.part")), [])

    def test_manifest_identity_and_traversal_are_rejected_before_network(self):
        for mutation in ({"expression_id": "OTHER_1_01"}, {"files": [{**self.entry, "path": "../../outside.png"}]}):
            self.manifest = {"expression_id": "L2HL_1_050", "files": [self.entry], **mutation}
            self.write_manifest()
            with patch.object(self.module, "urlopen", side_effect=AssertionError("unexpected network")):
                with self.assertRaises(ValueError):
                    self.fetch()

    def test_symlink_destination_cannot_escape_cache(self):
        outside = self.root / "outside"
        outside.mkdir()
        (self.folder / "plots").symlink_to(outside, target_is_directory=True)
        with patch.object(self.module, "urlopen", side_effect=AssertionError("unexpected network")):
            with self.assertRaises(ValueError):
                self.fetch()
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
