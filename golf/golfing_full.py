PROPERTIES = ("y", "p", "n")  # you, push, win
NOUNS = ("b", "f", "r")  # baba, flag, rock (the nouns)
ENTITIES = ("B", "F", "R")  # Baba, Flag, Rock (the entities)

isproperty = lambda symbol: symbol in PROPERTIES
isnoun = lambda symbol: symbol in NOUNS
isentity = lambda symbol: symbol in ENTITIES
isempty = lambda cell: cell == "."

# Grid transformations
transpose = lambda grid: [list(col) for col in zip(*grid)]
fliplr = lambda grid: [list(reversed(row)) for row in grid]
rotate_p90 = lambda grid: fliplr(transpose(grid))  # 90 deg clockwise
rotate_m90 = lambda grid: transpose(fliplr(grid))  # 90 deg counterclockwise
rotate_180 = lambda grid: rotate_p90(rotate_p90(grid))
rotate_0 = lambda x: x
# Null rotation

# Stripped down 'windowed' from more_itertools
# Can't import more_itertools because it's not in the standard library
from collections import deque


def each_three(seq):
    window = deque(maxlen=3)
    i = 3
    for _ in map(window.append, seq):
        i -= 1
        if not i:
            i = 1
            yield tuple(window)


def rulefinder(grid):
    """Find all the rules in the grid"""
    N, M = len(grid), len(grid[0])
    rules = []

    isis = lambda symbol: symbol == "i"
    # Check every candidate against the grammar
    # Noun is (Noun OR Property)
    isrule = lambda t: (
        isnoun(t[0]) and isis(t[1]) and (isnoun(t[2]) or isproperty(t[2]))
    )

    # Horizontal rules
    if M >= 3:
        for row in grid:
            for t in each_three(row):
                if isrule(t):
                    rules.append((t[0], t[2]))

    # Vertical rules
    if N >= 3:
        for col in zip(*grid):
            for t in each_three(col):
                if isrule(t):
                    rules.append((t[0], t[2]))

    rules = sorted(rules)
    return rules


def make_behaviour(you=False, push=False, win=False):
    """Helper to make a behaviour dictionary"""
    return dict(zip(PROPERTIES, (you, push, win)))


def ruleparser(rules):
    """Parse valid rules into behaviours and swaps"""

    behaviours = {noun: (make_behaviour()) for noun in NOUNS}
    swaps = []

    # Parse the rules
    for subject, action in rules:
        # Noun is (Noun OR Property)
        if isproperty(action):  # Noun is a Property
            behaviours[subject][action] = True
        else:  # (Noun is Noun)
            swaps.append((subject, action))
    swaps = sorted(swaps)
    return behaviours, swaps


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
    istext = lambda symbol: symbol in (*PROPERTIES, *NOUNS, "i")
    pushable = lambda cell: (
        isentity(cell) and behaviours[cell.lower()]["p"]
    ) or istext(cell)
    if not pushable(pile[0]):
        raise UnableToMove

    if isempty(pile[1]):
        return (pile[1], pile[0], *pile[2:])
    else:
        budged = attempt_to_move(pile[1:], behaviours)
        return (budged[0], pile[0], *budged[1:])


STEPS = ("^", "V", "<", ">")

# Rotations and counter rotations which need to be applied to the grid such that the move directioisempty
rots = (rotate_0, rotate_180, rotate_p90, rotate_m90)
rots = dict(zip(STEPS, rots))
crots = (rotate_0, rotate_180, rotate_m90, rotate_p90)
crots = dict(zip(STEPS, crots))


class YouWin(Exception):
    pass


def timestep(grid, behaviours, step):
    """Advance grid a single timestep, given the step and the current behaviours"""
    grid = rots[step](grid)
    new_grid = [["." for _ in row] for row in grid]

    isyou = lambda cell: isentity(cell) and behaviours[cell.lower()]["y"]
    iswin = lambda cell: isentity(cell) and behaviours[cell.lower()]["n"]

    for j, row in enumerate(grid):
        for k, cell in enumerate(row):
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
                    raise YouWin

                new_grid[j][k] = cell

    new_grid = crots[step](new_grid)
    return new_grid


def swap(grid, swaps):
    """Apply all the swaps to the grid"""
    new_grid = [[cell for cell in row] for row in grid]
    for a, b in swaps:
        for j, row in enumerate(grid):
            for k, cell in enumerate(row):
                if isentity(cell):
                    if cell.lower() == a and new_grid[j][k] is cell:
                        new_grid[j][k] = b.upper()

    return new_grid


def play(sequence):
    """Play a game, given the sequence of moves"""

    grid = ".............|.rip....RRR..|.......R...R.|.biy.B.R.F.R.|.......R...R.|.fin....RRR..|............."
    grid = [[cell for cell in row] for row in grid.split("|")]

    try:
        for step in (*sequence, None):
            rules = rulefinder(grid)
            behaviours, swaps = ruleparser(rules)

            # Check for you is win condition
            for noun in behaviours:
                if behaviours[noun]["y"] and behaviours[noun]["n"]:
                    raise YouWin

            # Do the swap
            grid = swap(grid, swaps)
            if step:
                grid = timestep(grid, behaviours, step)
    except YouWin:
        return 1
    else:
        return 0


if __name__ == "__main__":

    import os, sys

    sys.path.append(os.path.realpath("."))
    from baba.test_cases import TEST_CASES

    green = lambda x: f"\x1b[32m{x}\x1b[0m"
    red = lambda x: f"\x1b[31m{x}\x1b[0m"
    exit_code = 0
    for name in TEST_CASES:
        sequence = TEST_CASES[name]["sequence"]
        expected = TEST_CASES[name]["outcome"]
        if play(sequence) == expected:
            result = green("- PASS -")
        else:
            result = red("! FAIL !")
            exit_code = 1
        print(f"{sequence}\n{result}")
    exit(exit_code)
