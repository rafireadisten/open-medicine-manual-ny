import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('runtime', ROOT / 'agents/runtime/run_batch.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.rows = m.load_records(ROOT / 'research/normalized/curriculum_subtopics.json')
        self.card = json.loads((ROOT / 'research/drafts/OMM-W01-S01.json').read_text())
    def test_all_weeks(self):
        q = m.build_queue(self.rows)
        self.assertEqual(len(q), 78)
        self.assertEqual(len({r['week'] for r in q}), 26)
        self.assertFalse(any(r['complete'] for r in q))
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError): m.build_queue(self.rows + [self.rows[0]])
    def test_missing_week_rejected(self):
        with self.assertRaises(ValueError): m.build_queue([r for r in self.rows if r['week'] != 26])
    def test_approval_rejected(self):
        self.card['clinical_approval_status'] = 'approved'
        with self.assertRaises(ValueError): m.validate_card(self.card)
    def test_no_review_as_trial(self):
        self.card['x1']['design'] = 'review'
        with self.assertRaises(ValueError): m.validate_card(self.card)
    def test_missing_picot_rejected(self):
        del self.card['x1']['picot']['O']
        with self.assertRaises(ValueError): m.validate_card(self.card)
    def test_valid_draft(self):
        self.assertTrue(m.validate_card(self.card))
    def test_legacy_csv_wrapper(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'x.csv'
            p.write_text('<PARSED TEXT FOR SHEET: 1 / 1 TABS\nTAB NAME: x.csv>\nindex,id,title\n0,a,"a,b"\n')
            self.assertEqual(m.load_records(p), [{'id':'a','title':'a,b'}])
    def test_empty_inventory(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'x.json'; p.write_text('{"items": []}')
            with self.assertRaises(ValueError): m.load_records(p)
    def test_html_escaped_and_incomplete(self):
        with tempfile.TemporaryDirectory() as d:
            self.card['scope'] = '<script>alert(1)</script>'
            m.produce(self.card, m.build_queue(self.rows), Path(d))
            page = (Path(d) / 'hypertension.html').read_text()
            self.assertNotIn('<script>', page)
            self.assertIn('&lt;script&gt;', page)
            self.assertEqual(json.loads((Path(d) / 'draft_index.json').read_text())['indexed_complete'], [])
if __name__ == '__main__': unittest.main()
