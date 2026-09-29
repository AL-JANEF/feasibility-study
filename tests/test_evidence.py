import tempfile,unittest
from pathlib import Path
from feasibility_study.evidence import validate_record,validate_ledger,load_jsonl
class T(unittest.TestCase):
 def test_fact_source(self): self.assertTrue(any(i.level=='ERROR' for i in validate_record({'id':'E1','kind':'FACT','statement':'x','source_tier':'PRIMARY','confidence':'HIGH','status':'CURRENT'})))
 def test_unknown_high(self): self.assertTrue(any('HIGH confidence' in i.message for i in validate_record({'id':'E1','kind':'FACT','statement':'x','source':'u','source_tier':'UNKNOWN','confidence':'HIGH','status':'CURRENT'})))
 def test_estimate_basis(self): self.assertTrue(any(i.level=='ERROR' for i in validate_record({'id':'E1','kind':'ESTIMATE','statement':'x','source_tier':'PRIMARY','confidence':'MEDIUM','status':'CURRENT'})))
 def test_duplicate(self):
  rows=[{'id':'E1','kind':'FACT','statement':'x','source':'u','source_tier':'PRIMARY','confidence':'HIGH','status':'CURRENT'},{'id':'E1','kind':'FACT','statement':'y','source':'v','source_tier':'PRIMARY','confidence':'HIGH','status':'CURRENT'}]
  self.assertTrue(any('duplicate' in i.message for i in validate_ledger(rows)))
 def test_dependency(self):
  rows=[{'id':'E2','kind':'ESTIMATE','statement':'x','formula':'a+b','depends_on':['E1'],'source_tier':'PRIMARY','confidence':'MEDIUM','status':'CURRENT'}]
  self.assertTrue(any('missing id' in i.message for i in validate_ledger(rows)))
 def test_loader(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'e'; p.write_text('{"id":"E1"}\n\n{"id":"E2"}\n'); self.assertEqual(len(load_jsonl(p)),2)
