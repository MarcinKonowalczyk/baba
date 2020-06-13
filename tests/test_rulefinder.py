import unittest

from itertools import product, chain

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.rules import rulefinder

from baba.utils import string_to_grid as sg
from baba.utils import grid_to_string as gs
from baba.utils import NOUNS, PROPERTIES, ENTITIES, SYMBOLS

class ValidInput(unittest.TestCase):
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

    def test_single_rule(self):
        ''' Parsing of a tiny grid with a simple rule '''
        grid_strings = ('biy','.biy','biy.','.biy.')
        for grid_string in grid_strings:
            grid = sg(grid_string)
            with self.subTest(grid=grid_string):
                rules = rulefinder(grid)
                self.assertEqual(len(rules),1)
                self.assertEqual(''.join(rules[0]), 'by')

    def test_grid(self):
        ''' Parsing of a larger grid with multiple rules '''
        grid = sg('biy.fin\n.......\n.......\nwis.rip')
        targets = sorted(('by','fn','ws','rp'), key=lambda x:x[0])
        
        rules = rulefinder(grid)
        for rule,target in zip(rules,targets):
            with self.subTest(target):
                self.assertEqual(''.join(rule),target)

class VerticalRules(unittest.TestCase):

    def test_single_rule(self):
        ''' Parsing of a tiny grid with a simple rule '''
        grids = map(lambda x: sg('\n'.join(x)),('biy','.biy','biy.','.biy.'))
        for grid in grids:
            with self.subTest(grid):
                rules = rulefinder(grid)
                self.assertEqual(len(rules),1)
                self.assertEqual(''.join(rules[0]), 'by')

    def test_grid(self):
        ''' Parsing of a larger grid wit more rules '''
        grid = sg('.......\nb.f.w.r\ni.i.i.i\ny.n.s.p\n.......')
        targets = sorted(('by','fn','ws','rp'), key=lambda x:x[0])

        rules = rulefinder(grid)
        for rule,target in zip(rules,targets):
            with self.subTest(target):
                self.assertEqual(''.join(rule),target)

class Combinations(unittest.TestCase):

    def test_noun_is_noun(self):
        ''' Noun is Noun should be a rule '''
        for n1,n2 in product(NOUNS,repeat=2):
            grid_string = f'.....\n.{n1}i{n2}.\n.....'
            target = f'{n1}{n2}'
            grid = sg(grid_string)
            with self.subTest(grid=grid_string):
                rules = rulefinder(grid)
                self.assertEqual(len(rules),1)
                self.assertEqual(''.join(rules[0]), target)

    def test_noun_is_property(self):
        ''' Noun is Property should be a rule '''
        for n in NOUNS:
            for p in PROPERTIES:
                grid_string = f'.....\n.{n}i{p}.\n.....'
                target = f'{n}{p}'
                grid = sg(grid_string)
                with self.subTest(grid=grid_string):
                    rules = rulefinder(grid)
                    self.assertEqual(len(rules),1)
                    self.assertEqual(''.join(rules[0]), target)

    def test_property_is_noun(self):
        ''' Property is Noun shouldn't be a rule '''
        for p in PROPERTIES:
            for n in NOUNS:
                grid_string = f'.....\n.{p}i{n}.\n.....'
                grid = sg(grid_string)
                with self.subTest(grid=grid_string):
                    rules = rulefinder(grid)
                    self.assertEqual(len(rules),0)

    def test_property_is_property(self):
        ''' Property is Property shouldn't be a rule '''
        for p1,p2 in product(PROPERTIES,repeat=2):
            grid_string = f'.....\n.{p1}i{p2}.\n.....'
            grid = sg(grid_string)
            with self.subTest(grid=grid_string):
                rules = rulefinder(grid)
                self.assertEqual(len(rules),0)
    
    def test_entity_is_anything(self):
        ''' Entity is anything shouldn't be a rule '''
        for e in ENTITIES:
            for a in chain(SYMBOLS):
                grid_string = f'.....\n.{e}i{a}.\n.....'
                grid = sg(grid_string)
                with self.subTest(grid=grid_string):
                    rules = rulefinder(grid)
                    self.assertEqual(len(rules),0)

    def test_anything_is_entity(self):
        ''' Anything is entity shouldn't be a rule '''
        for a in chain(SYMBOLS):
            for e in ENTITIES:
                grid_string = f'.....\n.{a}i{e}.\n.....'
                grid = sg(grid_string)
                with self.subTest(grid=grid_string):
                    rules = rulefinder(grid)
                    self.assertEqual(len(rules),0)

if __name__ == '__main__':
    unittest.main()