"""Regression coverage for fail-closed reference-inventory audits."""
import csv
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "inventory_audit", ROOT / "agents/runtime/validate_reference_inventory.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ReferenceInventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / "research", self.root / "research")

    def test_two_nonapproved_reference_records_are_structurally_valid(self):
        result = m.audit(self.root)
        self.assertTrue(result["draft_schema_valid"], result["errors"])
        self.assertEqual(result["reference_documents"], 2)
        self.assertEqual(result["evidence_cards_linked"], 2)
        self.assertEqual(result["human_approved_registry_documents"], 0)

    def test_strict_completion_fails_without_exhaustive_inventory_and_signoff(self):
        result = m.audit(self.root)
        self.assertFalse(result["completion_eligible"])
        self.assertTrue(any("not certified" in s for s in result["completion_blockers"]))
        self.assertTrue(any("human clinical sign-off" in s for s in result["completion_blockers"]))

    def test_empty_registry_never_passes(self):
        path = self.root / "research/reference_registry.csv"
        path.write_text(path.read_text().splitlines()[0] + "\n", encoding="utf-8")
        result = m.audit(self.root)
        self.assertFalse(result["draft_schema_valid"])
        self.assertFalse(result["completion_eligible"])

    def test_duplicate_reference_document_rejected(self):
        path = self.root / "research/reference_registry.csv"
        lines = path.read_text().splitlines()
        path.write_text("\n".join(lines + [lines[1]]) + "\n", encoding="utf-8")
        self.assertFalse(m.audit(self.root)["draft_schema_valid"])

    def test_missing_picot_field_rejected(self):
        path = self.root / "research/drafts/OMM-W07-S02.json"
        card = json.loads(path.read_text())
        del card["x1"]["picot"]["O"]
        path.write_text(json.dumps(card), encoding="utf-8")
        self.assertFalse(m.audit(self.root)["draft_schema_valid"])

    def test_approval_status_mismatch_rejected(self):
        path = self.root / "research/drafts/OMM-W02-S03.json"
        card = json.loads(path.read_text())
        card["clinical_approval_status"] = "approved"
        path.write_text(json.dumps(card), encoding="utf-8")
        self.assertFalse(m.audit(self.root)["draft_schema_valid"])


if __name__ == "__main__":
    unittest.main()
