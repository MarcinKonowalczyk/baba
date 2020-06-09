import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.play import timestep, STEPS
from baba.utils import string_to_grid as sg
from baba.utils import PROPERTIES, ENTITIES

# 'Baba is you' rule
biy = behaviors = {'b':dict(zip(PROPERTIES,(True,False,True,True)))}

class Walking(unittest.TestCase):

    def test_walking_baba(self):
        ''' Simple waling baba '''
        grids = map(sg,('.\nB','B\n.','.B','B.'))
        targets = map(sg,('B\n.','.\nB','B.','.B'))
        for grid,step,target in zip(grids,STEPS,targets):
            with self.subTest(grid):
                grid2 = timestep(grid,biy,step)
                self.assertEqual(grid2,target)

    def test_walking_nouns(self):
        ''' Walking entities '''
        for entity in ENTITIES:
            grid = sg('...\n.{}.\n...'.format(entity))

            # Make target grid states
            target_format = lambda x: sg(x.format(entity))
            targets = map(target_format, \
                ('.{}.\n...\n...','...\n...\n.{}.',
                '...\n{}..\n...','...\n..{}\n...'))

            # 'Entity' is you rule
            behaviors = {entity.lower():dict(zip(PROPERTIES,(True,False,True,True)))} 
            
            for step,target in zip(STEPS,targets):
                with self.subTest(grid):
                    grid2 = timestep(grid,behaviors,step)
                    self.assertEqual(grid2,target)

    def test_claustrophobic_baba(self):
        ''' Baba with nowhere to move '''
        grid = sg('B')
        for step in STEPS:
            with self.subTest(grid):
                grid2 = timestep(grid,biy,step)
                self.assertEqual(grid2,grid)

    def test_confused_baba(self):
        ''' Baba bonking into the wall '''
        grids = map(sg,\
            ('.B.\n...\n...','...\n...\n.B.',
            '...\nB..\n...','...\n..B\n...'))
        for grid,step in zip(grids,STEPS):
            with self.subTest(grid):
                grid2 = timestep(grid,biy,step)
                self.assertEqual(grid2,grid)

    def test_complex_walking(self):
        ''' Test more complicates sequences of steps '''
        grid = sg('...\n.B.\n...')
        steps = '^^VV<><>'
        target = sg('...\n...\n.B.')

        grid2 = grid; # Copy grid
        for step in steps:
            grid2 = timestep(grid2,biy,step)

        self.assertEqual(grid2,target)

if __name__ == '__main__':
    unittest.main()