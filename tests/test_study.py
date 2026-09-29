import tempfile,unittest
from pathlib import Path
from feasibility_study.study import init_study,validate_study
ROOT=Path(__file__).resolve().parents[1]
class T(unittest.TestCase):
 def test_init(self):
  with tempfile.TemporaryDirectory() as td:
   d=Path(td)/'s'; init_study(d,ROOT/'templates/study','standard'); self.assertTrue((d/'15-final-decision.md').exists()); self.assertFalse(any(l=='ERROR' for l,_ in validate_study(d)))
 def test_refuse(self):
  with tempfile.TemporaryDirectory() as td:
   d=Path(td)/'s'; d.mkdir(); (d/'x').write_text('x')
   with self.assertRaises(FileExistsError): init_study(d,ROOT/'templates/study')
 def test_missing(self):
  with tempfile.TemporaryDirectory() as td:
   d=Path(td)/'s'; init_study(d,ROOT/'templates/study'); (d/'08-financial-model.md').unlink(); self.assertTrue(any('08-financial-model' in m for l,m in validate_study(d) if l=='ERROR'))
