# %%
from utils import *
STEPS = ('^','V','<','>')

# Rotations and counter rotations which need to be applied to the grid such that the move direction is up
rotate_0 = lambda x:x; # Null rotation
rots = (rotate_0, rotate_180, rotate_p90, rotate_m90)
rots = dict(zip(STEPS,rots))
crots = (rotate_0, rotate_180, rotate_m90, rotate_p90)
crots = dict(zip(STEPS,crots))

def timestep(grid,behaviors,step):
    ''' Advance grid a single timestep, given the step and the current behaviors '''
    grid = rots[step](grid)
    N, M = len(grid), len(grid[0])
    new_grid = empty_NM(N,M)
    for j,row in enumerate(grid):
        # TEMP!
        new_grid[j] = row;

    new_grid = crots[step](new_grid)
    return new_grid

timestep(grid,behaviors,'^');

for row in grid:
    print(' '.join(row))

# %%
def play(grid,sequence):

    pass