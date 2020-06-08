# %%
def grid_to_string(grid):
    ''' Convert grid to multiline string '''
    return '\n'.join(''.join(row) for row in grid)

# %%
def string_to_grid(string):
    ''' Convert multiline string to grid '''
    return [[cell for cell in row] for row in string.split('\n')]

# %%
def default_grid_string():
    ''' Hardcoded default grid string '''
    string = '.............\n.............\n...biy.fin...\n.............\n...WWWWWWW...\n......R......\n....B.R.F....\n......R......\n...WWWWWWW...\n.............\n...wis.rip...\n.............\n.............''';
    return string

def default_grid():
    ''' Hardcoded default grid '''
    grid = [['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','b','i','y','.','f','i','n','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','W','W','W','W','W','W','W','.','.','.'],['.','.','.','.','.','.','R','.','.','.','.','.','.'],['.','.','.','.','B','.','R','.','F','.','.','.','.'],['.','.','.','.','.','.','R','.','.','.','.','.','.'],['.','.','.','W','W','W','W','W','W','W','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','w','i','s','.','r','i','p','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.']]
    return grid

# %%
def transpose(grid):
    return [list(col) for col in zip(*grid)]

def fliplr(grid):
    return [list(reversed(row)) for row in grid]

def rotate_p90(grid):
    ''' Rotate grid 90 deg clockwise '''
    return fliplr(transpose(grid))

def rotate_m90(grid):
    ''' Rotate grid 90 deg counterclockwise '''
    return transpose(fliplr(grid))

def rotate_180(grid):
    ''' Rotate grid 180 deg '''
    return rotate_p90(rotate_p90(grid))
