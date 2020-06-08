# %%
from more_itertools import windowed
from collections import namedtuple

PROPERTIES = ('y','p','s','n')
NOUNS = ('b','w','f','r')
ENTITIES = tuple(n.upper() for n in NOUNS)

# Helper functions
isproperty = lambda symbol: symbol in PROPERTIES
isnoun = lambda symbol: symbol in NOUNS
isentity = lambda symbol: symbol in ENTITIES

VALID_SYMBOLS = (*PROPERTIES,*NOUNS,*ENTITIES)
issymbol = lambda symbol: symbol in VALID_SYMBOLS
isis = lambda symbol: symbol=='i' # Treat 'is' in a special way

def rulefinder(grid):
    ''' Find all the rules in the grid '''
    N, M = len(grid), len(grid[0])
    rules = [];

    # Check every candidate against the grammar
    # Noun is (Noun OR Property)
    isrule = lambda t:(
        isnoun(t[0]) and isis(t[1]) and
        (isnoun(t[2]) or isproperty(t[2])))

    # Horizontal rules
    if M>=3:
        for row in grid:
            for t in windowed(row,3):
                if isrule(t):
                    rules.append(t)

    # Vertical rules
    if N>=3:
        for col in zip(*grid):
            for t in windowed(col,3):
                if isrule(t):
                    rules.append(t)

    # Sort according to the first letter
    rules = sorted(rules,key=lambda x:x[0])
    return rules

# %%
# TODO: Add tests
def ruleparser(rules):
    ''' Parse valid rules into behaviors '''

    # Initialise behavior and transformations
    behaviors = {}
    for noun in NOUNS:
        behaviors[noun] = dict(zip(PROPERTIES,[False]*4))
    transformations = []

    # Parse the rules
    for subject, _, action in rules:
        # Noun is (Noun OR Property)
        if isproperty(action): # Noun is a Property
            behaviors[subject][action] = True
        else: # (Noun is Noun)
            transformations.append((subject,action))

    # Go through the transformations again to make sure no contradictions
    new_transformations = [];
    for a, b in transformations:
        if a!=b: # Noun_A is Noun_B
            if (a,a) not in transformations: # Noun_A is not stationary
                new_transformations.append((a,b))
        else: # a==a
            new_transformations.append((a,a))
    transformations = new_transformations

    # Add entry for text behavior
    text_behavior = (True,False,True,True)
    behaviors['t'] = dict(zip(PROPERTIES,text_behavior));

    return behaviors, transformations