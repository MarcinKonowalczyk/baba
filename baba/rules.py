# %%
from more_itertools import windowed
from collections import namedtuple

import os, sys
sys.path.append(os.path.realpath('.'))

from baba.utils import *

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
    ''' Parse valid rules into behaviours '''

    behaviours = {noun:(make_behaviour()) for noun in NOUNS}
    transformations = []

    # Parse the rules
    for subject, _, action in rules:
        # Noun is (Noun OR Property)
        if isproperty(action): # Noun is a Property
            behaviours[subject][action] = True
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

    # Add entry for text behaviour
    behaviours['t'] = make_behaviour(push=True);

    return behaviours, transformations