import unittest
from feasibility_study.finance import run_model,npv,irr,apply_multipliers,FinancialInputError
BASE={'currency':'SAR','initial_investment':100.0,'opening_cash':100.0,'financing':0.0,'discount_rate':.1,'years':[{'year':1,'revenue':100.0,'cogs':20.0,'opex':30.0},{'year':2,'revenue':120.0,'cogs':24.0,'opex':30.0}],'unit_economics':{'price':10,'variable_cost_per_unit':4,'annual_fixed_costs':60,'cac':12,'monthly_arpu':10,'gross_margin':.6,'monthly_churn':.05}}
class T(unittest.TestCase):
 def test_run(self): self.assertEqual(len(run_model(BASE)['years']),2)
 def test_gp(self): self.assertEqual(run_model(BASE)['years'][0]['gross_profit'],80)
 def test_be(self): self.assertAlmostEqual(run_model(BASE)['unit_economics']['break_even_units'],10)
 def test_ltv(self): self.assertAlmostEqual(run_model(BASE)['unit_economics']['ltv_cac'],10)
 def test_npv(self): self.assertAlmostEqual(npv([-100,60,60],.1),-100+60/1.1+60/(1.1**2))
 def test_irr(self): self.assertGreater(irr([-100,60,60]),0)
 def test_noirr(self): self.assertIsNone(irr([-100,-20,-10]))
 def test_scenario(self): self.assertEqual(apply_multipliers(BASE,{'revenue':.5})['years'][0]['revenue'],50)
 def test_bad_scenario(self):
  with self.assertRaises(FinancialInputError): apply_multipliers(BASE,{'magic':1})
 def test_negative(self):
  bad={**BASE,'years':[{'year':1,'revenue':-1,'cogs':0,'opex':0}]}
  with self.assertRaises(FinancialInputError): run_model(bad)
