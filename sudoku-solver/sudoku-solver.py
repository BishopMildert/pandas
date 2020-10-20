import numpy as np

# Add the puzzle you want to solve here:
grid = [[0, 0, 0, 2, 0, 0, 0, 0, 9],
        [0, 3, 7, 1, 0, 9, 0, 2, 0],
        [0, 0, 9, 7, 5, 0, 0, 0, 8],
        [0, 5, 2, 3, 0, 0, 9, 6, 7],
        [7, 0, 6, 5, 2, 1, 4, 8, 0],
        [3, 4, 8, 0, 6, 7, 1, 5, 0],
        [5, 0, 1, 4, 0, 0, 0, 7, 6],
        [0, 0, 3, 0, 7, 5, 2, 4, 1],
        [0, 0, 4, 0, 0, 2, 0, 0, 5]
        ]


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False

    return True


print(np.matrix(grid))


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
