import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.play import timestep, STEPS, YouWin

from baba.utils import string_to_grid as sg
from baba.utils import make_behaviour as mb
from baba.utils import PROPERTIES, ENTITIES

# 'Baba is you' and 'Flag is win' rules
biy = {'b':mb(you=True)}
rip = {'r':mb(push=True)}

class Walking(unittest.TestCase):

    def test_walking_baba(self):
        ''' Simple waling baba '''
        grids = map(sg,('.\nB','B\n.','.B','B.'))
        targets = map(sg,('B\n.','.\nB','B.','.B'))
        for grid,step,target in zip(grids,STEPS,targets):
            with self.subTest(grid):
                grid2 = timestep(grid,biy,step)
                self.assertEqual(grid2,target)

    def test_walking_entities(self):
        ''' Walking entities '''
        for entity in ENTITIES:
            grid = sg('...\n.{}.\n...'.format(entity))

            # Make target grid states
            target_format = lambda x: sg(x.format(entity))
            targets = map(target_format, \
                ('.{}.\n...\n...','...\n...\n.{}.',
                '...\n{}..\n...','...\n..{}\n...'))

            # 'Entity' is you rule
            behaviours = {entity.lower():dict(zip(PROPERTIES,(True,False,True,True)))} 
            
            for step,target in zip(STEPS,targets):
                with self.subTest(grid):
                    grid2 = timestep(grid,behaviours,step)
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
        paths = ('^<VV>>^^<V','^^VV<><>')
        targets = map(sg,('...\n.B.\n...','...\n...\n.B.'))
        for steps,target in zip(paths,targets):
            grid2 = grid; # Copy grid
            for step in steps:
                grid2 = timestep(grid2,biy,step)
            self.assertEqual(grid2,target)

class Winning(unittest.TestCase):

    def test_win(self):
        ''' Walk into a win '''
        grids = map(sg,('BF','BF.'))
        behaviour = {**biy,'f':mb(win=True)}
        for grid in grids:
            with self.subTest(grid):
                with self.assertRaises(YouWin):
                    timestep(grid,behaviour,'>')

    def test_dont_win_but_push(self):
        ''' Walk into a win which is also push '''
        grids = map(sg,('BF.','BFR.'))
        targets = map(sg,('.BF','.BFR'))
        behaviour = {**biy,**rip,
            'f':mb(win=True,push=True)}
        for grid, target in zip(grids,targets):
            with self.subTest(grid):
                try:
                    grid2 = timestep(grid,behaviour,'>')
                    self.assertEqual(grid2,target)
                except YouWin:
                    self.fail("'timestep' raised YouWin unexpectedly!")

    def test_win_push_wall(self):
        ''' Walk into a win which is also push, but against the wall '''
        grids = map(sg,('BF','BFR'))
        behaviour = {**biy,**rip,
            'f':mb(win=True,push=True)}
        for grid in grids:
            with self.assertRaises(YouWin):
                timestep(grid,behaviour,'>')

    def test_rock_doesnt_win(self):
        ''' Push a rock into a win '''
        grids = map(sg,('BRF','BRF.'))
        targets = map(sg,('BRF','.BRF'))
        behaviour = {**biy,**rip,
            'f':mb(win=True,push=True)}
        for grid,target in zip(grids,targets):
            with self.subTest(grid):
                try:
                    grid2 = timestep(grid,behaviour,'>')
                    self.assertEqual(grid2,target)
                except YouWin:
                    self.fail("'timestep' raised YouWin unexpectedly!")

if __name__ == '__main__':
    unittest.main()