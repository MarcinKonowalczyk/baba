import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.play import attempt_to_move, UnableToMove
from baba.utils import make_behaviour

# 'Rock is push' and 'Wall is stop'
behaviours = {'r':make_behaviour(push=True),'w':make_behaviour(stop=True)}

# String to pile
sp = lambda string: tuple(j for j in string)

class RockAndWall(unittest.TestCase):
    def test_simple_null(self):
        ''' Simple null cases '''
        piles = map(sp,('.','.R','.RR','.R.','.R.R','.W','.WW','.RW'))
        for pile in piles:
            with self.subTest(pile): 
                self.assertEquals(attempt_to_move(pile,behaviours),pile)

    def test_simple_moves(self):
        ''' Simple successful moves '''
        piles   = map(sp,('R.','R..','R.R','R.W','RR.W','R.R..W'))
        targets = map(sp,('.R','.R.','.RR','.RW','.RRW','.RR..W'))
        for pile,target in zip(piles,targets):
            with self.subTest(pile): 
                self.assertEquals(attempt_to_move(pile,behaviours),target)

    def test_simple_stuck(self):
        ''' Simple cases of UnableToMove exception '''
        piles = map(sp,('','R','RR','RRR','W','RW','RW.','W.','RRW.WR','RWW..'))
        for pile in piles:
            with self.subTest(pile): 
                with self.assertRaises(UnableToMove):
                    attempt_to_move(pile,behaviours)

    def test_long_move(self):
        ''' Long successful move '''
        piles   = map(sp,('R'*100+'.','R'*100+'.W'))
        targets = map(sp,('.'+'R'*100,'.'+'R'*100+'W'))
        for pile,target in zip(piles,targets):
            with self.subTest(pile): 
                self.assertEquals(attempt_to_move(pile,behaviours),target)

    def test_long_stuck(self):
        ''' Long pile raising UnableToMove exception '''
        piles = map(sp,('R'*100,'RW'+'.'*100,'W'*100+'.'))
        for pile in piles:
            with self.assertRaises(UnableToMove):
                attempt_to_move(pile,behaviours)

if __name__ == '__main__':
    unittest.main()