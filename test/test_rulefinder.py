import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.rules import rulefinder
from baba.utils import string_to_grid as sg

class ValidInput(unittest.TestCase):

    def test_empty(self):
        ''' Parse null grid '''
        grid = [[]]
        self.assertEqual(rulefinder(grid), [])

    def test_large(self):
        ''' Parse large empty grid '''
        grid = [['.' for j in range(10)] for k in range(10)]
        self.assertEqual(rulefinder(grid), [])

    def test_tall(self):
        ''' Parse 1-wide grid '''
        grid = [['.' for j in range(1)] for k in range(10)]
        self.assertEqual(rulefinder(grid), [])

    def test_wide(self):
        ''' Parse 1-tall grid '''
        grid = [['.' for j in range(10)] for k in range(1)]
        self.assertEqual(rulefinder(grid), [])

class HorizontalRules(unittest.TestCase):

    def test_single_rule_1(self):
        ''' Parsing of a tiny grid with a simple rule '''
        grids = map(sg,('biy','.biy','biy.','.biy.'))
        for grid in grids:
            with self.subTest(grid):
                rules = rulefinder(grid)
                self.assertEqual(len(rules),1)
                self.assertEqual(''.join(rules[0]), 'biy')

    def test_grid(self):
        ''' Parsing of a larger grid with multiple rules '''
        grid = sg('biy.fin\n.......\n.......\nwis.rip')
        targets = sorted(('biy','fin','wis','rip'), key=lambda x:x[0])
        
        rules = rulefinder(grid)
        for rule,target in zip(rules,targets):
            with self.subTest(target):
                self.assertEqual(''.join(rule),target)

class VerticalRules(unittest.TestCase):

    def test_single_rule_1(self):
        ''' Parsing of a tiny grid with a simple rule '''
        grids = map(lambda x: sg('\n'.join(x)),('biy','.biy','biy.','.biy.'))
        for grid in grids:
            with self.subTest(grid):
                rules = rulefinder(grid)
                self.assertEqual(len(rules),1)
                self.assertEqual(''.join(rules[0]), 'biy')

    def test_grid(self):
        ''' Parsing of a larger grid wit more rules '''
        grid = sg('.......\nb.f.w.r\ni.i.i.i\ny.n.s.p\n.......')
        targets = sorted(('biy','fin','wis','rip'), key=lambda x:x[0])

        rules = rulefinder(grid)
        for rule,target in zip(rules,targets):
            with self.subTest(target):
                self.assertEqual(''.join(rule),target)


if __name__ == '__main__':
    unittest.main()