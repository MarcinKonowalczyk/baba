# %%
from rules import rulefinder, ruleparser
from utils import *

# %%
grid_string = '''.............
.............
...biy.fin...
.............
...WWWWWWW...
......R......
....B.R.F....
......R......
...WWWWWWW...
.............
...wis.rip...
...wiw.......
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