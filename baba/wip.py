# %%
import os, sys
sys.path.append(os.path.realpath('..'))

from baba.rules import rulefinder, ruleparser
from baba.utils import *
from baba.play import *

# %%
grid = default_grid()
# grid[11][3], grid[11][4], grid[11][5] = 'wiy'
# grid[6][1], grid[6][2], grid[6][3] = 'bin'
for row in grid:
    print(' '.join(row))
print('\n')

rules = rulefinder(grid)
print('Rules:\n', rules, '\n')

behaviours, swaps = ruleparser(rules)
print('Behaviours:\n', behaviours, '\n')
print('Swaps:\n', swaps, '\n')

# %%
sequence = '<VVV<<^V>>^^<<'
grid2 = play(grid,sequence)
for row in grid2:
    print(' '.join(row))

# %%

pile = ('.','R','f','i','w','W','.','R','W')