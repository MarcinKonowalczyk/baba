# %%
import os, sys
sys.path.append(os.path.realpath('..'))

from baba.rules import rulefinder, ruleparser
from baba.utils import *
from baba.play import *

# %%

grid = default_grid();
grid[5][4] = 'W';
grid[11][3], grid[11][4], grid[11][5] = 'wiy'
for row in grid:
    print(' '.join(row))
print('\n')

rules = rulefinder(grid)
print('Rules:\n', rules, '\n')

behaviours, transformations = ruleparser(rules)
print('Behaviours:\n', behaviours, '\n')
print('Transformations:\n', transformations, '\n')

# %%
grid2 = timestep(grid,behaviours,'>');
for row in grid2:
    print(' '.join(row))
# %%

pile = ('.','R','f','i','w','W','.','R','W')