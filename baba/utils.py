# %% Things to export
__all__ = ['PROPERTIES','NOUNS','ENTITIES','isproperty','isnoun','isentity','SYMBOLS','issymbol','isis','istext','isempty','grid_to_string','string_to_grid','default_grid_string','default_grid','transpose','fliplr','rotate_p90','rotate_m90','rotate_180','empty_NM','make_behaviour','isvalidgrid']

# %%
# you, push, win
PROPERTIES = ('y','p','n')
# baba, wall, flag, rock
NOUNS = ('b','w','f','r')
ENTITIES = tuple(n.upper() for n in NOUNS)

# Helper functions
isproperty = lambda symbol: symbol in PROPERTIES
isnoun = lambda symbol: symbol in NOUNS
isentity = lambda symbol: symbol in ENTITIES

SYMBOLS = (*PROPERTIES,*NOUNS,*ENTITIES,'i')
issymbol = lambda symbol: symbol in SYMBOLS
isis = lambda symbol: symbol=='i'

TEXT = (*PROPERTIES,*NOUNS,'i')
istext = lambda symbol: symbol in TEXT
isempty = lambda cell: cell=='.'

# %%
def grid_to_string(grid,row_delimiter='\n',col_delimiter=''):
    ''' Convert grid to multiline string '''
    return row_delimiter.join(col_delimiter.join(row) for row in grid)

# %%
def string_to_grid(string,row_delimiter='\n',col_delimiter=''):
    ''' Convert multiline string to grid '''
    return [[cell for cell in row.replace(col_delimiter,'')] for row in string.split(row_delimiter)]

# %%
def default_grid_string():
    ''' Hardcoded default grid string '''
    string = '.............\n.............\n...biy.fin...\n.............\n...WWWWWWW...\n......R......\n....B.R.F....\n......R......\n...WWWWWWW...\n.............\n...wi..rip...\n.............\n.............''';
    return string

def default_grid():
    ''' Hardcoded default grid '''
    grid = [['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','b','i','y','.','f','i','n','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','W','W','W','W','W','W','W','.','.','.'],['.','.','.','.','.','.','R','.','.','.','.','.','.'],['.','.','.','.','B','.','R','.','F','.','.','.','.'],['.','.','.','.','.','.','R','.','.','.','.','.','.'],['.','.','.','W','W','W','W','W','W','W','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','w','i','.','.','r','i','p','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.','.']]
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

def make_behaviour(you=False,push=False,win=False):
    ''' Helper to make a behaviour '''
    return dict(zip(PROPERTIES,(you,push,win)))

#%%

def isvalidgrid(grid):
    ''' A pile of assertion to check that the grid is valid '''
    
    # Make sure grid is a list of lists
    assert isinstance(grid,list), 'Grid is not a list'
    assert len(grid)>0, 'Grid is an empty list'
    assert isinstance(grid[0],list), 'Grid must be a list of lists'

    N, M = len(grid), len(grid[0])
    
    assert M>0, 'Grid has zero width'
        
    for row in grid:
        assert len(row)==M, 'Grid must be rectangular'
        for cell in row:
            assert cell in (*SYMBOLS,'.'), f"'{cell}' is not a valid symbol"