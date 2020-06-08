import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.rules import rulefinder

class TestValidInput(unittest.TestCase):

    def test_empty(self):
        grid = [[]]
        self.assertEqual(rulefinder(grid), [])

    def test_large(self):
        grid = [['.' for j in range(10)] for k in range(10)]
        self.assertEqual(rulefinder(grid), [])

    def test_tall(self):
        grid = [['.' for j in range(1)] for k in range(10)]
        self.assertEqual(rulefinder(grid), [])

    def test_wide(self):
        grid = [['.' for j in range(10)] for k in range(1)]
        self.assertEqual(rulefinder(grid), [])

class TestSingleRules(unittest.TestCase):
    grid = [['.' for j in range(10)] for k in range(10)]
    grid[0][0], grid[0][1], grid[0][2] = 'biy';
    grid[0][-3], grid[0][2], grid[0][1] = 'fin';
    grid[-1][0], grid[-1][1], grid[-1][2] = 'wis';
    grid[-1][-3], grid[-1][2], grid[-1][1] = 'rip';

    def test_single_rule(self):
        grid = [['b','i','y']]
        rules = rulefinder(grid);
        self.assertEqual(len(rules),1)
        self.assertEqual(''.join(rules[0]), 'biy')

if __name__ == '__main__':
    unittest.main()