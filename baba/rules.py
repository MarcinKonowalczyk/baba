from more_itertools import windowed

def rulefinder(grid):
    N, M = len(grid), len(grid[0])
    rules = [];

    canberule = lambda t : t[0].islower() and t[1]=='i' and t[2].islower()

    if M>=3:
        for row in grid:
            for t in windowed(row,3):
                if canberule(t):
                    rules.append(t)

    if N>=3:
        for col in zip(*grid):
            for t in windowed(col,3):
                if canberule(t):
                    rules.append(t)

    # Sort according to the first letter
    rules = sorted(rules,key=lambda x:x[0])
    return rules
