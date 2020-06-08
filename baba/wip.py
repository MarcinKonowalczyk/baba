# %%
import os, sys
sys.path.append(os.path.realpath('..'))

from baba.rules import rulefinder, ruleparser
from baba.utils import *

# %%
grid_string = '''.............
.............
...biy.fin...
.............
...WWWWWWW...
....W.R......
....B.R.F....
......R......
...WWWWWWW...
.............
...wis.rip...
...wip.......
.............''';

grid = string_to_grid(grid_string);
for row in grid:
    print(' '.join(row))

# %% PARSE RULES

rules = rulefinder(grid)
print(rules)

behaviors, transformations = ruleparser(rules)
print('Behaviors', behaviors)
print('')
print('Transformations', transformations)

# %%
for rule in rulefinder(grid):
    print(''.join(rule))

# %%
def grid_to_string(grid):
    return '\n'.join(''.join(row) for row in grid)
    

# %%

pile = ('.','R','f','i','w','W','.','R','W')

class UnableToMove(Exception):
    pass

def attempt_to_move(pile,behaviors):
    ''' Attempt to move a pile of cell '''

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
    pass

try:
    shifted_pile = attempt_to_move(pile,behaviors)
    print(shifted_pile)
except UnableToMove:
    print('Unable to move!')