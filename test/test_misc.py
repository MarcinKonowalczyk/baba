import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.utils import *

class TestGridStringConversion(unittest.TestCase):
    def test_empty(self):
        ''' Empty grid to empty string '''
        grid = [[]]
        self.assertEqual(grid_to_string(grid),'')

    def test_large(self):
        ''' Simple 3x3 grid string '''
        grid = [['.' for j in range(3)] for k in range(3)]
        target = '...\n...\n...';
        self.assertEqual(grid_to_string(grid), target)

class TestStringGridConversion(unittest.TestCase):
    def test_empty(self):
        ''' Empty string to empty grid '''
        string = ''
        self.assertEqual(string_to_grid(string),[[]])

    def test_large(self):
        ''' 3x3 string to grid '''
        string = '...\n...\n...'
        target = [['.' for j in range(3)] for k in range(3)]
        self.assertEqual(string_to_grid(string), target)

class TestBackAndForthRules(unittest.TestCase):
    def test_backandforth_1(self):
        ''' Check that s2g reverses g2s '''
        grid = [['.' for j in range(10)] for k in range(10)]
        grid[0][0], grid[0][1], grid[0][2] = 'biy';
        grid[0][-3], grid[0][2], grid[0][1] = 'fin';
        grid[-1][0], grid[-1][1], grid[-1][2] = 'wis';
        grid[-1][-3], grid[-1][2], grid[-1][1] = 'rip';

        self.assertEqual(string_to_grid(grid_to_string(grid)),grid)

    def test_backandforth_2(self):
        ''' Check that g2s reverses s2g '''
        string = 'biy.....fin\n...........\nWWWWWWWWWWW\n.....R.....\n..B..R..F..\n.....R.....\nWWWWWWWWWWW\n...........\n wis.....rip'

        self.assertEqual(grid_to_string(string_to_grid(string)),string)

if __name__ == '__main__':
    unittest.main()