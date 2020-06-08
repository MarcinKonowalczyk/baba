def grid_to_string(grid):
    return '\n'.join(''.join(row) for row in grid)

def string_to_grid(string):
    return [[cell for cell in row] for row in string.split('\n')]