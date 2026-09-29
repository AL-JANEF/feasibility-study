import tempfile, unittest, json
from pathlib import Path
from feasibility_study.study_v2 import init_study, validate_study

class StudyV2Tests(unittest.TestCase):
    def test_init(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td)/"s"
            init_study(d)
            self.assertTrue((d/"21-final-feasibility.md").exists())
            self.assertTrue((d/"deliverables").exists())

    def test_incomplete_profile_fails(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td)/"s"
            init_study(d)
            issues=validate_study(d)
            self.assertTrue(any(level=="ERROR" and "PROJECT_PROFILE" in msg for level,msg in issues))

    def test_complete_profile_passes_structure(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td)/"s"
            init_study(d)
            p=json.loads((d/"PROJECT_PROFILE.json").read_text())
            p.update({
                "project_name":"HukmOS",
                "sector":"Technology",
                "subsector":"SaaS enterprise software",
                "business_model":"subscription",
                "jurisdiction":"Saudi Arabia",
                "stage":"pre-launch",
                "study_mode":"standard",
                "currency":"SAR",
            })
            (d/"PROJECT_PROFILE.json").write_text(json.dumps(p))
            self.assertFalse(any(level=="ERROR" for level,_ in validate_study(d)))

if __name__=="__main__":
    unittest.main()
