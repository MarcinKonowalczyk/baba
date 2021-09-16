import unittest

from itertools import permutations, filterfalse

# Add '.' to path so running this file by itself also works
import os, sys

sys.path.append(os.path.realpath("."))
from baba.play import swap

from baba.utils import string_to_grid as sg
from baba.utils import ENTITIES, SYMBOLS

# Wall is rock
wir = ("w", "r")
wiw = ("w", "w")


class SwapsAndStationaries(unittest.TestCase):
    def test_no_swaps(self):
        """Lots of walls but no swap rule"""
        grid = sg(".W.\n..W\nWWW")
        grid2 = swap(grid, ())
        self.assertEqual(grid2, grid)

    def test_wall_to_rock(self):
        """Swap wall into a rock"""
        grid = sg(".W.\n..W\nWWW")
        target = sg(".R.\n..R\nRRR")
        swaps = (wir,)
        grid2 = swap(grid, swaps)
        self.assertEqual(grid2, target)

    def test_but_wall_is_wall(self):
        """Would swap wall to rock, but wall is wall"""
        grid = sg(".W.\n..W\nWWW")
        swaps = (wir, wiw)
        grid2 = swap(grid, swaps)
        self.assertEqual(grid2, grid)

    def test_all_no_swaps(self):
        """No swaps on all symbols"""
        for symbol in SYMBOLS:
            with self.subTest(symbol=symbol):
                grid = sg(".{0}.\n..{0}\n{0}{0}{0}".format(symbol))
                grid2 = swap(grid, ())
                self.assertEqual(grid2, grid)

    def test_all_swaps(self):
        """A is B"""
        for a, b in permutations(ENTITIES, 2):
            with self.subTest(entity_a=a, entity_b=b):
                grid = sg(f".{a}.\n..{a}\n{a}{a}{a}")
                target = sg(f".{b}.\n..{b}\n{b}{b}{b}")
                swaps = ((a, b),)
                grid2 = swap(grid, ())
                self.assertEqual(grid2, grid)

    def test_all_swaps_but_stationary(self):
        """A is B, but B is B"""
        for a, b in permutations(ENTITIES, 2):
            with self.subTest(entity_a=a, entity_b=b):
                grid = sg(f".{a}.\n..{a}\n{a}{a}{a}")
                target = sg(f".{b}.\n..{b}\n{b}{b}{b}")
                swaps = ((a, b), (a, a))
                grid2 = swap(grid, ())
                self.assertEqual(grid2, grid)

    def test_no_byproducts(self):
        """Wall is rock does not mess anything else up"""
        for e in filterfalse(lambda x: x == "W", ENTITIES):
            with self.subTest(entity=e):
                grid = sg(f".W{e}\n..W\nW{e}W")
                target = sg(f".R{e}\n..R\nR{e}R")
                swaps = (wir,)
                grid2 = swap(grid, swaps)
                self.assertEqual(grid2, target)


if __name__ == "__main__":
    unittest.main()
