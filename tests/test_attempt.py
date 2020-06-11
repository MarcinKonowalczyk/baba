import unittest
from itertools import chain

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.play import attempt_to_move, UnableToMove
from baba.utils import make_behaviour
from baba.utils import ENTITIES, PROPERTIES, NOUNS, TEXT

# 'Rock is push' and, implicitly, 'Wall is stop'
behaviours = {'r':make_behaviour(push=True),'w':make_behaviour()}

# String to pile
sp = lambda string: tuple(j for j in string)

class RockAndWall(unittest.TestCase):
    def test_simple_null(self):
        ''' Simple null cases '''
        piles = map(sp,('.','.R','.RR','.R.','.R.R','.W','.WW','.RW'))
        for pile in piles:
            with self.subTest(pile): 
                self.assertEqual(attempt_to_move(pile,behaviours),pile)

    def test_simple_moves(self):
        ''' Simple successful moves '''
        piles   = map(sp,('R.','R..','R.R','R.W','RR.W','R.R..W'))
        targets = map(sp,('.R','.R.','.RR','.RW','.RRW','.RR..W'))
        for pile,target in zip(piles,targets):
            with self.subTest(pile): 
                self.assertEqual(attempt_to_move(pile,behaviours),target)

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
                self.assertEqual(attempt_to_move(pile,behaviours),target)

    def test_long_stuck(self):
        ''' Long pile raising UnableToMove exception '''
        piles = map(sp,('R'*100,'RW'+'.'*100,'W'*100+'.'))
        for pile in piles:
            with self.assertRaises(UnableToMove):
                attempt_to_move(pile,behaviours)

    def test_no_behaviour(self):
        ''' Push entity with no associated behaviour dictionary '''
        for entity in ENTITIES:
            pile = sp('{}.'.format(entity))
            with self.assertRaises(KeyError):
                attempt_to_move(pile,{})

    def test_no_property(self):
        ''' Push entity with no property in the behaviour dictionary '''
        for entity in ENTITIES:
            pile = sp('{}.'.format(entity))
            behaviour = {'{}'.format(entity.lower):{}}
            with self.assertRaises(KeyError):
                attempt_to_move(pile,behaviour)

class PushingText(unittest.TestCase):
    def test_pushing(self):
        ''' Test pushing all the pieces of text '''
        for text in chain(NOUNS,PROPERTIES,'i'):
            format_fun = lambda x: sp(x.format(text))
            piles = map(format_fun,('{0}.','{0}{0}.','{0}.{0}'))
            targets = map(format_fun,('.{0}','.{0}{0}','.{0}{0}'))
            print('\n',text,[i for i in piles],[i for i in targets])
            for pile,target in zip(piles,targets):
                with self.subTest(text):
                    self.assertEqual(attempt_to_move(pile,behaviours),target)

    def test_no_behaviour(self):
        ''' Push text with no associated behaviour dictionary '''
        for text in TEXT:
            pile = sp('{}.'.format(text))
            with self.subTest(text):
                with self.assertRaises(KeyError):
                    attempt_to_move(pile,{})

    def test_no_property(self):
        ''' Push text with no associated behaviour dictionary '''
        for text in TEXT:
            pile = sp('{}.'.format(text))
            behaviour = {'t':{}}
        with self.assertRaises(KeyError):
            attempt_to_move(pile,behaviour)

if __name__ == '__main__':
    unittest.main()