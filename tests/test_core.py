import unittest
from memory_taint_paths import run
class DomainTests(unittest.TestCase):
 def test_alternative_support_does_not_erase_taint(self):
  r=run({'nodes':[{'id':'a','kind':'source'},{'id':'b','kind':'source'},{'id':'d','kind':'derived','rules':[['a'],['b']]}],'revoked':['a']})['nodes'][-1];self.assertTrue(r['supported_by_unrevoked_sources']);self.assertTrue(r['requires_regeneration_review']);self.assertEqual(r['clean_support_rule'],['b'])
 def test_and_support_requires_all(self):
  r=run({'nodes':[{'id':'a','kind':'source'},{'id':'b','kind':'source'},{'id':'d','kind':'derived','rules':[['a','b']]}],'revoked':['a']})['nodes'][-1];self.assertFalse(r['supported_by_unrevoked_sources'])
 def test_cycle_cannot_self_justify(self):
  r=run({'nodes':[{'id':'a','kind':'derived','rules':[['b']]},{'id':'b','kind':'derived','rules':[['a']]}],'revoked':[]});self.assertTrue(all(not n['supported_by_unrevoked_sources'] for n in r['nodes']))
 def test_clean_source_breaks_cycle(self):
  r=run({'nodes':[{'id':'s','kind':'source'},{'id':'a','kind':'derived','rules':[['b'],['s']]},{'id':'b','kind':'derived','rules':[['a']]}],'revoked':[]});self.assertTrue(all(n['supported_by_unrevoked_sources'] for n in r['nodes']))
 def test_unknown_parent(self):
  with self.assertRaises(ValueError):run({'nodes':[{'id':'a','kind':'derived','rules':[['missing']]}],'revoked':[]})
