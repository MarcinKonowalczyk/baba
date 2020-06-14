import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.play import play, YouWin, YouLose

from baba.utils import default_grid
class Win(unittest.TestCase):

    def test_simple_win(self):
        ''' Simplest win on a default grid '''
        grid = default_grid()
        sequence = '>>^>>V'
        with self.assertRaises(YouWin):
            play(grid,sequence)

    def test_instant_win(self):
        ''' Instantenous win on a grid '''
        grid = default_grid()
        grid[6][1], grid[6][2], grid[6][3] = 'bin'
        with self.assertRaises(YouWin):
            play(grid,'')

    def test_ring_of_babas(self):
        ''' Win by making rock is baba and walking into a flag '''
        grid = default_grid()
        sequence = '<^^^<<V^>>VV<<>>'
        with self.assertRaises(YouWin):
            play(grid,sequence)

class Lose(unittest.TestCase):

    def test_simple_loss(self):
        ''' Simplest loss on a default grid '''
        grid = default_grid()
        sequence = '<^<V'
        with self.assertRaises(YouLose):
            play(grid,sequence)
    
    def test_instant_loss(self):
        ''' Instantenous loss on a grid '''
        grid = default_grid()
        grid[3][3] = '.'
        with self.assertRaises(YouLose):
            play(grid,'')

    def test_no_baba_left(self):
        ''' Become flag and therefore loose (since flag is not you) '''
        grid = default_grid()
        steps = '<V<<^V>>^^<<'
        with self.assertRaises(YouLose):
            play(grid,steps)

if __name__ == '__main__':
    unittest.main()