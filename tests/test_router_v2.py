import unittest
from feasibility_study.router import routing_plan, route_sector

class RouterTests(unittest.TestCase):
    def profile(self, sector="Technology", subsector="SaaS"):
        return {
            "project_name":"X",
            "sector":sector,
            "subsector":subsector,
            "business_model":"subscription",
            "jurisdiction":"Saudi Arabia",
            "stage":"pre-launch",
            "study_mode":"standard",
            "currency":"SAR",
        }

    def test_saas_routes(self):
        r=routing_plan(self.profile())
        self.assertIn("references/sectors/digital-services.md",r["sector_files"])
        self.assertFalse(r["dynamic_sector_pack_required"])
        self.assertEqual(r["jurisdiction_hint"],"references/jurisdictions/saudi-arabia-v2.md")

    def test_unknown_requires_dynamic_pack(self):
        r=routing_plan(self.profile("Space","orbital servicing"))
        self.assertTrue(r["dynamic_sector_pack_required"])

    def test_missing_field(self):
        p=self.profile(); p["currency"]=""
        with self.assertRaises(ValueError): routing_plan(p)

if __name__=="__main__":
    unittest.main()
