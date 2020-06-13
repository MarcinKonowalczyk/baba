import unittest

from string import ascii_letters
from random import choice, randrange
from itertools import permutations

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.utils import *

class StringConversion(unittest.TestCase):

    def test_grid_to_string(self):
        ''' 3x3 grid to string '''
        grid = [['.' for _ in range(3)] for _ in range(3)]
        target = '...\n...\n...';
        self.assertEqual(grid_to_string(grid), target)

    def test_string_to_grid(self):
        ''' 3x3 string to grid '''
        string = '...\n...\n...'
        target = [['.' for _ in range(3)] for _ in range(3)]
        self.assertEqual(string_to_grid(string), target)
        
    def test_back_and_forth(self):
        ''' Check that s2g reverses g2s '''
        grid = default_grid()
        self.assertEqual(string_to_grid(grid_to_string(grid)),grid)

    def test_forth_and_back(self):
        ''' Check that g2s reverses s2g '''
        string = default_grid_string()
        self.assertEqual(grid_to_string(string_to_grid(string)),string)

    def test_other_delimiters(self):
        ''' g2s with other delimiters '''
        delimiters = ('\n','',' ','|')
        grid = [['.' for _ in range(3)] for _ in range(3)]
        for d1,d2 in permutations(delimiters,2):
            with self.subTest(d1=d1,d2=d2):
                target = f'.{d2}.{d2}.{d1}.{d2}.{d2}.{d1}.{d2}.{d2}.'
                string = grid_to_string(grid,row_delimiter=d1,col_delimiter=d2)
                self.assertEqual(string, target)

    def test_other_delimiters(self):
        ''' s2g with other delimiters '''
        delimiters = ('\n','',' ','|')
        grid = [['.' for _ in range(3)] for _ in range(3)]
        for d1,d2 in permutations(delimiters,2):
            with self.subTest(d1=d1,d2=d2):
                string = f'.{d2}.{d2}.{d1}.{d2}.{d2}.{d1}.{d2}.{d2}.'

                if d1=='': # empty separator, therefore cannot remake grid
                    with self.assertRaises(ValueError):
                        string_to_grid(string,row_delimiter=d1,col_delimiter=d2)
                else:
                    grid2 = string_to_grid(string,row_delimiter=d1,col_delimiter=d2)
                    self.assertEqual(grid2, grid)

class RotatingSquares(unittest.TestCase):

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
            self.assertEqual(transpose(grid),target)

    def test_fliplr(self):
        ''' Flip left right '''
        with self.subTest('2x2'):
            grid = [['A','B'],['C','D']]
            target = [['B','A'],['D','C']]
            self.assertEqual(fliplr(grid),target)
        with self.subTest('3x3'):
            grid = [['A','B','C'],['D','E','F'],['G','H','I']]
            target = [['C','B','A'],['F','E','D'],['I','H','G']]
            self.assertEqual(fliplr(grid),target)

class RotatingRectangles(unittest.TestCase):

    def test_clockwise(self):
        ''' Clockwise rotation '''
        grids = ([['A','B']],[['A'],['B']],
            [['A','B','C'],['D','E','F']],
            [['A','B'],['C','D'],['E','F']])
        targets = ([['A'],['B']],[['B','A']],
            [['D','A'],['E','B'],['F','C']],
            [['E','C','A'],['F','D','B']])
        for grid,target in zip(grids,targets):
            with self.subTest():
                self.assertEqual(rotate_p90(grid),target)

    def test_counterclockwise(self):
        ''' Counter-clockwise rotation '''
        grids = ([['A','B']],[['A'],['B']],
            [['A','B','C'],['D','E','F']],
            [['A','B'],['C','D'],['E','F']])
        targets = ([['B'],['A']],[['A','B']],
            [['C','F'],['B','E'],['A','D']],
            [['B','D','F'],['A','C','E']])
        for grid,target in zip(grids,targets):
            with self.subTest():
                self.assertEqual(rotate_m90(grid),target)

    def test_180(self):
        ''' 180 deg rotation '''
        grids = ([['A','B']],[['A'],['B']],
            [['A','B','C'],['D','E','F']],
            [['A','B'],['C','D'],['E','F']])
        targets = ([['B','A']],[['B'],['A']],
            [['F','E','D'],['C','B','A']],
            [['F','E'],['D','C'],['B','A']])
        for grid,target in zip(grids,targets):
            with self.subTest():
                self.assertEqual(rotate_180(grid),target)

    def test_transpose(self):
        ''' Transpose '''
        grids = ([['A','B']],[['A'],['B']],
            [['A','B','C'],['D','E','F']],
            [['A','B'],['C','D'],['E','F']])
        targets = ([['A'],['B']],[['A','B']],
            [['A','D'],['B','E'],['C','F']],
            [['A','C','E'],['B','D','F']])
        for grid,target in zip(grids,targets):
            with self.subTest():
                self.assertEqual(transpose(grid),target)

    def test_fliplr(self):
        ''' Flip left right '''
        grids = ([['A','B']],[['A'],['B']],
            [['A','B','C'],['D','E','F']],
            [['A','B'],['C','D'],['E','F']])
        targets = ([['B','A']],[['A'],['B']],
            [['C','B','A'],['F','E','D']],
            [['B','A'],['D','C'],['F','E']])
        for grid,target in zip(grids,targets):
            with self.subTest():
                self.assertEqual(fliplr(grid),target)


class EmptyCreation(unittest.TestCase):
    
    def test_creation_1(self):
        ''' Creation of full grid '''
        self.assertEqual(empty_NM(0,0),[])
        self.assertEqual(empty_NM(0,0,element='b'),[])

    def test_creation_2(self):
        ''' Creation of normal grid '''
        target = [['.']*3]*3
        self.assertEqual(empty_NM(3,3),target)
        target = [['b']*3]*3
        self.assertEqual(empty_NM(3,3,element='b'),target)

class GridValidator(unittest.TestCase):

    def test_valid_shapes(self):
        ''' Invalid grid shapes '''
        grids = ([['.']*(j+1)]*(j+1) for j in range(5))
        for grid in grids:
            with self.subTest(grid=grid):
                try:
                    isvalidgrid(grid)
                except AssertionError:
                    self.fail('Unexpected AssertionError on a valid grid')

    def test_invalid_shapes(self):
        ''' Invalid grid shapes '''
        grids = ([],[[]],[[],[]],[['.'],['.','.']])
        for grid in grids:
            with self.subTest(grid=grid):
                with self.assertRaises(AssertionError):
                    isvalidgrid(grid)

    def test_valid_symbols(self):
        ''' Valid symbols in a grid '''
        for symbol in SYMBOLS:
            grid = ([[f'{symbol}','.'],['.',f'{symbol}']])
            with self.subTest(symbol=symbol):
                try:
                    isvalidgrid(grid)
                except AssertionError:
                    self.fail('Unexpected AssertionError on a valid grid')

    def test_invalid_symbols(self):
        ''' Invalid symbols in a grid '''
        for symbol in filter(lambda x: x not in SYMBOLS,ascii_letters):
            grid = ([[f'{symbol}','.'],['.',f'{symbol}']])
            with self.subTest(symbol=symbol):
                with self.assertRaises(AssertionError):
                    isvalidgrid(grid)

    def test_random_valid(self):
        ''' Grid filled with random but valid symbols '''
        for _ in range(10):
            N, M = (randrange(1,11),randrange(1,11))
            grid = [[choice((*SYMBOLS,'.')) for _ in range(M)] for _ in range(N)]
            grid_string = grid_to_string(grid,row_delimiter='|');
            with self.subTest(N=N,M=M,grid=grid_string):
                try:
                    isvalidgrid(grid)
                except AssertionError:
                    self.fail('Unexpected AssertionError on a valid grid')

class MakeBehaviour(unittest.TestCase):

    def test_all_false(self):
        target = dict(zip(PROPERTIES,[False,]*len(PROPERTIES)))
        behaviour = make_behaviour()
        self.assertDictEqual(behaviour,target)
    

if __name__ == '__main__':
    unittest.main()