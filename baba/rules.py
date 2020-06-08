from more_itertools import windowed

def rulefinder(grid):
    N, M = len(grid), len(grid[0])
    rules = [];

    if M>=3:
        for row in grid:
            for t in windowed(row,3):
                if t[0].islower() and t[1]=='i' and t[2].islower():
                    rules.append(t);

    return rules