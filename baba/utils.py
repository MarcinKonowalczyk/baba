# %% Things to export
__all__ = ['PROPERTIES','NOUNS','ENTITIES','isproperty','isnoun','isentity','SYMBOLS','issymbol','isis','isempty','grid_to_string','string_to_grid','default_grid_string','default_grid','transpose','fliplr','rotate_p90','rotate_m90','rotate_180','empty_NM']

# %%
PROPERTIES = ('y','p','s','n')
NOUNS = ('b','w','f','r')
ENTITIES = tuple(n.upper() for n in NOUNS)

# Helper functions
isproperty = lambda symbol: symbol in PROPERTIES
isnoun = lambda symbol: symbol in NOUNS
isentity = lambda symbol: symbol in ENTITIES

SYMBOLS = (*PROPERTIES,*NOUNS,*ENTITIES)
issymbol = lambda symbol: symbol in SYMBOLS
isis = lambda symbol: symbol=='i' # Treat 'is' in a special way
isempty = lambda cell: cell=='.'
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

# %%

def empty_NM(N,M,element='.'):
    ''' Make an empty NxM grid '''
    return [[element for _ in range(M)] for _ in range(N)]