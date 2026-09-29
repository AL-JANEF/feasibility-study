import unittest
from feasibility_study.decision import derive_state
class T(unittest.TestCase):
 def test_fatal(self): self.assertEqual(derive_state({'fatal_blockers':['x'],'fatal_blocker_verified':True})['state'],'NO_GO_CURRENT_FORM')
 def test_unknown(self): self.assertEqual(derive_state({'critical_unknowns':['wtp'],'dimensions':{}})['state'],'VALIDATE_FIRST')
 def test_conditional(self): self.assertEqual(derive_state({'dimensions':{'market':{'signal':'STRONG','confidence':'MEDIUM'}}})['state'],'CONDITIONAL_GO')
 def test_go(self): self.assertEqual(derive_state({'dimensions':{'market':{'signal':'STRONG','confidence':'HIGH'},'finance':{'signal':'ADEQUATE','confidence':'HIGH'}}})['state'],'GO')
 def test_early(self): self.assertEqual(derive_state({'technical_readiness':'R&D','enabler_outside_horizon':True})['state'],'TOO_EARLY')
