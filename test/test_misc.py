import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.utils import *

class StringConversion1(unittest.TestCase):
    def test_empty(self):
        ''' Empty grid to empty string '''
        grid = [[]]
        self.assertEqual(grid_to_string(grid),'')

    def test_large(self):
        ''' Simple 3x3 grid string '''
        grid = [['.' for j in range(3)] for k in range(3)]
        target = '...\n...\n...';
        self.assertEqual(grid_to_string(grid), target)

class StringConversion2(unittest.TestCase):
    def test_empty(self):
        ''' Empty string to empty grid '''
        string = ''
        self.assertEqual(string_to_grid(string),[[]])

    def test_large(self):
        ''' 3x3 string to grid '''
        string = '...\n...\n...'
        target = [['.' for j in range(3)] for k in range(3)]
        self.assertEqual(string_to_grid(string), target)

class StringConvertion3(unittest.TestCase):
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

class Rotations(unittest.TestCase):
    def test_clockwise(self):
        ''' Clockwise rotation '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['C','A'],['D','B']]
            self.assertEqual(rotate_p90(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['G','D','A'],['H','E','B'],['I','F','C']]
            self.assertEqual(rotate_p90(grid),target)

    def test_counterclockwise(self):
        ''' Counter-clockwise rotation '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['B','D'],['A','C']]
            self.assertEqual(rotate_m90(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['C','F','I'],['B','E','H'],['A','D','G']]
            self.assertEqual(rotate_m90(grid),target)

    def test_180(self):
        ''' 180 deg rotation '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['D','C'],['B','A']]
            self.assertEqual(rotate_180(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['I','H','G'],['F','E','D'],['C','B','A']]
            self.assertEqual(rotate_180(grid),target)

    def test_transpose(self):
        ''' Transpose '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['A','C'],['B','D']]
            self.assertEqual(transpose(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['A','D','G'],['B','E','H'],['C','F','I']]
            self.assertEquals(transpose(grid),target)

    def test_fliplr(self):
        ''' Flip left right '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['B','A'],['D','C']]
            self.assertEqual(fliplr(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['C','B','A'],['F','E','D'],['I','H','G']]
            self.assertEquals(fliplr(grid),target)

if __name__ == '__main__':
    unittest.main()