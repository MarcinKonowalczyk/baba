# %%
import os, sys
sys.path.append(os.path.realpath('.'))
from baba.utils import *

STEPS = ('^','V','<','>')

# Rotations and counter rotations which need to be applied to the grid such that the move direction is up
rotate_0 = lambda x:x; # Null rotation
rots = (rotate_0, rotate_180, rotate_p90, rotate_m90)
rots = dict(zip(STEPS,rots))
crots = (rotate_0, rotate_180, rotate_m90, rotate_p90)
crots = dict(zip(STEPS,crots))

class UnableToMove(Exception):
    pass

def attempt_to_move(pile,behaviors):
    ''' Attempt to move a pile of cells in accordance with their behaviour '''
    
    if len(pile)==0: # Empty pile
        raise UnableToMove
    
    if isempty(pile[0]): # Trivial pile
        return pile
    elif len(pile)==1: # One-element pile
        raise UnableToMove

    # Larger pile
    cantpush = lambda cell: isentity(cell) and not behaviors[cell.lower()]['p']
    if cantpush(pile[0]):
        raise UnableToMove

    if isempty(pile[1]):
        return (pile[1], pile[0], *pile[2:])
    else:
        budged = attempt_to_move(pile[1:],behaviors)
        return (budged[0], pile[0], *budged[1:])

def timestep(grid,behaviors,step):
    ''' Advance grid a single timestep, given the step and the current behaviors '''
    grid = rots[step](grid)
    N, M = len(grid), len(grid[0])
    new_grid = empty_NM(N,M)

    isyou = lambda cell: isentity(cell) and behaviors[cell.lower()]['y']

    for j,row in enumerate(grid):
        for k,cell in enumerate(row):
            if isempty(cell):
                continue # Already empty

            if not isyou(cell):
                new_grid[j][k] = cell;
                continue

            # Attempt to move
            pile = [new_grid[l][k] for l in reversed(range(j))]
            try:
                shifted_pile = attempt_to_move(pile,behaviors)
                for l,elem in enumerate(reversed(shifted_pile)):
                    new_grid[j][k] = elem

                new_grid[j-1][k] = cell;
            except UnableToMove:
                new_grid[j][k] = cell;

    new_grid = crots[step](new_grid)
    return new_grid

new_grid = timestep(grid,behaviors,'^');

for row in new_grid:
    print(' '.join(row))

# %%
def play(grid,sequence):

    pass