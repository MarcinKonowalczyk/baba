from more_itertools import windowed

def rulefinder(grid):
    rules = [];
    for row in grid:
        for t in windowed(row,3):
            if t[0].islower() and t[1]=='i' and t[2].islower():
                rules.append(t);
    return rules