from .mapping import splitOn, mapAll


def parseGrid(data, type = None):

    ret = splitOn(splitOn(data, "\n"), "")

    if type is not None:
        ret = mapAll(ret, type)

    return ret


def printGrid(grid):

    for line in grid:
        print(line)


def insideGrid(grid, row, col, wrap = False):

    if not wrap and (row < 0 or col < 0): return False
    return len(grid) > row or len(grid[0]) > col


def getNeighbours(grid, row, col, diagonals = True, wrap = False):

    ret = []

    if diagonals:
        for i in range(-1,2):
            for j in range(-1,2):
                if i == j == 0: continue
                if wrap:
                    i %= len(grid)
                    j %= len(grid[0])
                elif row+i < 0 or row+i >= len(grid) or col+j < 0 or col+j >= len(grid[0]): continue
                ret.append(grid[row+i][col+j])

    else:
        if wrap:
            ret.append(grid[row-1][col])
            ret.append(grid[row][col-1])
            ret.append(grid[(row+1) % len(grid)][col])
            ret.append(grid[row][(col+1) % len(grid[0])])

        else:
            for y,x in [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]:
                if insideGrid(grid, y, x):
                    ret.append(grid[y][x])

    return ret