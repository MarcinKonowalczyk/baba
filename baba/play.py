# %%
from copy import deepcopy
from more_itertools import flatten

import os, sys

sys.path.append(os.path.realpath("."))
from baba.utils import *
from baba.rules import *

sn = symbol_to_name

STEPS = ("^", "V", "<", ">")

# Rotations and counter rotations which need to be applied to the grid such that the move direction is up
rotate_0 = lambda x: x
# Null rotation
rots = (rotate_0, rotate_180, rotate_p90, rotate_m90)
rots = dict(zip(STEPS, rots))
crots = (rotate_0, rotate_180, rotate_m90, rotate_p90)
crots = dict(zip(STEPS, crots))


class UnableToMove(Exception):
    pass


def attempt_to_move(pile, behaviours):
    """Attempt to move a pile of cells in accordance with their behaviour"""

    if len(pile) == 0:  # Empty pile
        raise UnableToMove

    if isempty(pile[0]):  # Trivial pile
        return pile
    elif len(pile) == 1:  # One-element pile
        raise UnableToMove

    # Larger pile
    pushable = lambda cell: (isentity(cell) and behaviours[cell.lower()]["p"]) or (
        istext(cell) and behaviours["t"]["p"]
    )
    if not pushable(pile[0]):
        raise UnableToMove

    if isempty(pile[1]):
        return (pile[1], pile[0], *pile[2:])
    else:
        budged = attempt_to_move(pile[1:], behaviours)
        return (budged[0], pile[0], *budged[1:])


def timestep(grid, behaviours, step):
    """Advance grid a single timestep, given the step and the current behaviours"""
    grid = rots[step](grid)
    N, M = len(grid), len(grid[0])
    new_grid = empty_NM(N, M)

    isyou = lambda cell: isentity(cell) and behaviours[cell.lower()]["y"]
    iswin = lambda cell: isentity(cell) and behaviours[cell.lower()]["n"]
    youwin = None  # youwin exception

    for j, row in enumerate(grid):
        for k, cell in enumerate(row):
            if isempty(cell):
                continue  # Already empty

            if not isyou(cell):
                new_grid[j][k] = cell
                continue

            # Attempt to move
            pile = [new_grid[l][k] for l in reversed(range(j))]
            try:
                shifted_pile = attempt_to_move(pile, behaviours)
                for l, elem in enumerate(reversed(shifted_pile)):
                    new_grid[l][k] = elem

                new_grid[j - 1][k] = cell
            except UnableToMove:
                if len(pile) > 0 and iswin(pile[0]):
                    youwin = YouWin(
                        f"You are '{sn(cell)}' and you've walked onto a '{sn(pile[0])}'"
                        " which is 'win'. Hooray! :D "
                    )
                new_grid[j][k] = cell

    new_grid = crots[step](new_grid)
    return new_grid, youwin


def swap(grid, swaps):
    """Apply all the swaps to the grid"""

    stationary = (a for a, b in swaps if a == b)
    swaps = ((a, b) for a, b in swaps if a != b and a not in stationary)

    new_grid = deepcopy(grid)
    for a, b in swaps:
        for j, row in enumerate(grid):
            for k, cell in enumerate(row):
                if isentity(cell):
                    # If the rule applies to the cell, and no other rule has been applied yet
                    if cell.lower() == a and new_grid[j][k] is cell:
                        new_grid[j][k] = b.upper()

    return new_grid


class YouWin(Exception):
    pass


class YouLose(Exception):
    pass


def play(grid, sequence):
    """Play a game, given the sequence of moves"""

    isvalidgrid(grid)

    for step in (*sequence, None):
        rules = rulefinder(grid)
        behaviours, swaps = ruleparser(rules)

        # Check for you is win condition
        for noun in behaviours:
            if behaviours[noun]["y"] and behaviours[noun]["n"]:
                raise YouWin(f"You are '{sn(noun)}' and you are 'win'. Hooray! :D")

        # Do the swap
        grid = swap(grid, swaps)

        entities_present = {j.lower() for j in flatten(grid) if isentity(j)}
        if not any(behaviours[e]["y"] for e in entities_present):
            raise YouLose("Nothing is 'you'. Game over.")

        # Timestep the grid
        if step:
            (grid, youwin) = timestep(grid, behaviours, step)
            if youwin:
                raise youwin

    return grid
