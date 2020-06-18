import unittest

from copy import deepcopy

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))

from baba.rules import ruleparser
from baba.utils import make_behaviour as mb
from baba.utils import NOUNS
# from baba.utils import string_to_grid as sg

# Default behaviours
db = {noun:(mb()) for noun in NOUNS}
db['t'] = mb(push=True)

class ParseRules(unittest.TestCase):

    def test_grid_rules(self):
        ''' Just behaviours '''
        rules = [('b','y'),('f','n'),('r','p')];

        target_behaviours = deepcopy(db)
        target_behaviours['b']['y'] = True
        target_behaviours['f']['n'] = True
        target_behaviours['r']['p'] = True

        behaviours, swaps = ruleparser(rules)
        for key in behaviours:
            with self.subTest(key=key):
                self.assertDictEqual(behaviours[key],target_behaviours[key])
        with self.subTest('swaps'):
            self.assertEqual(swaps,[])

    def test_swaps(self):
        ''' Just swaps '''
        rules = sorted([('b','w'),('b','b'),('b','r'),('w','r'),('f','r')]);
        behaviours, swaps = ruleparser(rules)
        for key in behaviours:
            with self.subTest(key=key):
                self.assertDictEqual(behaviours[key],db[key])
        with self.subTest('swaps'):
            self.assertEqual(swaps,rules)

    def test_both(self):
        ''' Both behaviours and swaps '''
        rules = [('b','y'),('f','n'),('f','r'),('w','w')];
        
        target_behaviours = deepcopy(db)
        target_behaviours['b']['y'] = True
        target_behaviours['f']['n'] = True

        target_swaps = [('f','r'),('w','w')]

        behaviours, swaps = ruleparser(rules)
        for key in behaviours:
            with self.subTest(key=key):
                self.assertDictEqual(behaviours[key],target_behaviours[key])
        with self.subTest('swaps'):
            self.assertListEqual(swaps,target_swaps)

if __name__ == '__main__':
    unittest.main()