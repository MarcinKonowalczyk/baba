import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.utils import *

class StringConversion1(unittest.TestCase):
    def test_empty(self):
        ''' Empty grid to empty string '''
        grid = [[]]
        self.assertEquals(grid_to_string(grid),'')

    def test_large(self):
        ''' Simple 3x3 grid string '''
        grid = [['.' for _ in range(3)] for _ in range(3)]
        target = '...\n...\n...';
        self.assertEquals(grid_to_string(grid), target)

class StringConversion2(unittest.TestCase):
    def test_empty(self):
        ''' Empty string to empty grid '''
        string = ''
        self.assertEquals(string_to_grid(string),[[]])

    def test_large(self):
        ''' 3x3 string to grid '''
        string = '...\n...\n...'
        target = [['.' for _ in range(3)] for _ in range(3)]
        self.assertEquals(string_to_grid(string), target)

class StringConvertion3(unittest.TestCase):
    def test_backandforth_1(self):
        ''' Check that s2g reverses g2s '''
        grid = [['.' for _ in range(10)] for _ in range(10)]
        grid[0][0], grid[0][1], grid[0][2] = 'biy';
        grid[0][-3], grid[0][2], grid[0][1] = 'fin';
        grid[-1][0], grid[-1][1], grid[-1][2] = 'wis';
        grid[-1][-3], grid[-1][2], grid[-1][1] = 'rip';

        self.assertEquals(string_to_grid(grid_to_string(grid)),grid)

    def test_backandforth_2(self):
        ''' Check that g2s reverses s2g '''
        string = 'biy.....fin\n...........\nWWWWWWWWWWW\n.....R.....\n..B..R..F..\n.....R.....\nWWWWWWWWWWW\n...........\n wis.....rip'

        self.assertEquals(grid_to_string(string_to_grid(string)),string)

class Rotations(unittest.TestCase):
    def test_clockwise(self):
        ''' Clockwise rotation '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['C','A'],['D','B']]
            self.assertEquals(rotate_p90(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['G','D','A'],['H','E','B'],['I','F','C']]
            self.assertEquals(rotate_p90(grid),target)

    def test_counterclockwise(self):
        ''' Counter-clockwise rotation '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['B','D'],['A','C']]
            self.assertEquals(rotate_m90(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['C','F','I'],['B','E','H'],['A','D','G']]
            self.assertEquals(rotate_m90(grid),target)

    def test_180(self):
        ''' 180 deg rotation '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['D','C'],['B','A']]
            self.assertEquals(rotate_180(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['I','H','G'],['F','E','D'],['C','B','A']]
            self.assertEquals(rotate_180(grid),target)

    def test_transpose(self):
        ''' Transpose '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['A','C'],['B','D']]
            self.assertEquals(transpose(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['A','D','G'],['B','E','H'],['C','F','I']]
            self.assertEquals(transpose(grid),target)

    def test_fliplr(self):
        ''' Flip left right '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['B','A'],['D','C']]
            self.assertEquals(fliplr(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['C','B','A'],['F','E','D'],['I','H','G']]
            self.assertEquals(fliplr(grid),target)

class EmptyCreation(unittest.TestCase):
    
    def test_creation_1(self):
        ''' Creation of full grid '''
        self.assertEquals(empty_NM(0,0),[])
        self.assertEquals(empty_NM(0,0,element='b'),[])

    def test_creation_2(self):
        ''' Creation of normal grid '''
        target = [['.']*3]*3
        self.assertEquals(empty_NM(3,3),target)
        target = [['b']*3]*3
        self.assertEquals(empty_NM(3,3,element='b'),target)

if __name__ == '__main__':
    unittest.main()