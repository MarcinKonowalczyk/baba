import unittest

# Add '.' to path so running this file by itself also works
import os, sys
sys.path.append(os.path.realpath('.'))
from golf.golfing_short import Y

tests = (
    ('>>^>>V',1),
    ('<^<V',0),
    ('<^^^<<V^>>VV<<>>',1),
    ('<VV<V<<^V>>^<',1),
    ('<^^^<<V>V<>>',1),
    ('<^^^<<V^<<VV>><<^>><<',1),
    ('<VVV<^<^>V>^^V<<<<^^^>^>>>>VVV<^>>>',1),
    ('<^<<<<V>>>V>VV<<^^^>^<VV>>V<V<^^>^<V>>>>>>>V<^^^^>^<<<<<<<<<',1),
    ('<V<<<<V>>V>^^>>^^>>^>>V',0),
    ('<V<<<<V>>V>>^^VV>^^',0),
    ('<V<<V^<V>>>^^<^>^^<<V^<<VV>>>^>VVVV^^^<<<<^>>^>VVVV>>V^<<V>>^^>>',1),
    ('>VV>^^<^>V>^VV<<<<<<<V^>V>>^>V^^<<^>^^<<V^<<VV>>>^>VVVV^^^<<<<^>>^>VVVVV^^>>>>>>',1),
    ('<V<<<<V>>V>>>^V<<<^>V>>^V<<^>V>>^^^>>^>>V',0),
    ('<V<<<<V>>V>>>^V<<<^>V>>^V<<^>><^^^>V>V<^<V<VV>>>>^<<<>^^>>^>>V',0),
    ('<^<<<<V>>^<<^^>>V^<<VV>>^><V><V><<<VVV>^^<^>>V>^^<^>VVV>VV<<^^^<^>V>^<^>><<V<<^>>>>>V<^<VV<<',1),
    ('<^<<<<V>>^<<^^>>VV<V>V>>VV<<^V<<^>^^^<^>^>VV>V<V<V>^^>V>V>>>^^<<',1),
    ('<^^^<<V^<<V><VVVVV>>^V<<^>^<^><',0),
    ('<^^^<<V^<<V>>>><<<V>>><<<<VVVV>>^V<<<^^>>>><<<<V>>>><<<<^^>>>><',0),
    ('VVVV>>>>>>>>^^^^^^^>^^>^>^<<<<<<<<<<<<<VVVVVVV^^>>>>>>>>^>',1))

class Golf(unittest.TestCase):

    def test_golf(self):
        ''' Test the minimal golfing implementation '''
        for sequence,expected in tests:
            with self.subTest(sequence=sequence):
                self.assertEqual(Y(sequence),expected)

if __name__ == '__main__':
    unittest.main()