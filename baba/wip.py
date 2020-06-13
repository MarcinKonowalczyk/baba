# %%
import os, sys
sys.path.append(os.path.realpath('..'))

from baba.rules import rulefinder, ruleparser
from baba.utils import *
from baba.play import *

# %%

string = '''.............
.rip...RRRRR.
.......R...R.
.biy.B.R.F.R.
.......R...R.
.fin...RRRRR.
.............
'''
grid = string_to_grid(string);
# grid[11][3], grid[11][4], grid[11][5] = 'wiy'
# grid[11][7], grid[11][8], grid[11][9] = 'bin'
for row in grid:
    print(' '.join(row))
print('\n')

rules = rulefinder(grid)
print('Rules:\n', rules, '\n')

behaviours, swaps = ruleparser(rules)
print('Behaviours:\n', behaviours, '\n')
print('Swaps:\n', swaps, '\n')

# %%

grid2 = play(grid,'')
for row in grid2:
    print(' '.join(row))

# %%

pile = ('.','R','f','i','w','W','.','R','W')