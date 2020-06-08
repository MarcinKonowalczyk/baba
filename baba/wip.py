# %%
from rules import rulefinder

# %% MAKE LEVEL
N, M = 9, 11;
grid = [['.' for j in range(M)] for k in range(N)]

grid[0][0] = 'b';
grid[0][1] = 'i';
grid[0][2] = 'y';
grid[0][-3] = 'f';
grid[0][-2] = 'i';
grid[0][-1] = 'n';

for j in range(M):
    grid[2][j] = 'W';

for j in (3,4,5):
    grid[j][5] = 'R';

grid[4][2] = 'B';
grid[4][8] = 'F';

for j in range(M):
    grid[6][j] = 'W';

grid[-1][0] = 'w';
grid[-1][1] = 'i';
grid[-1][2] = 's';
grid[-1][-3] = 'r';
grid[-1][-2] = 'i';
grid[-1][-1] = 'p';

for row in grid:
    print(''.join(row))

# %% PARSE RULES

rulefinder([['b','i','y']])
# rulefinder([['b','i','y']])

# %%
for rule in rulefinder(grid):
    print(''.join(rule))

# %%
a = 1;
print(a)