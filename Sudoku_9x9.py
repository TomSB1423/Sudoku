# Working 9x9 Sudoku solver
import numpy as np
# sudoku grid 9x9
grid = [
    [4, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0],
]

completed_grid = grid
# find possible numbers that could be inserted into space


def possibilities(y, x):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # find numbers in corrosponding y axis
    for i in range(0, 9):
        if grid[y][i] in num_list:
            num_list.remove(grid[y][i])
    # find numbers in corrosponding x axis
    for j in range(0, 9):
        if grid[j][x] in num_list:
            num_list.remove(grid[j][x])
    # find valid numbers in small square
    for i in range(0, 3):
        for j in range(0, 3):
            grid_check = grid[j + ((y//3)*3)][i + ((x//3)*3)]
            if grid_check in num_list:
                num_list.remove(grid_check)
    return num_list

# replace each missing value


def replace(grid):
    # loop in y
    for y in range(0, 9):
        # loop in x
        for x in range(0, 9):
            if grid[y][x] == 0:
                # check possible numbers that can be inserted
                possible = possibilities(y, x)
                if possible:
                    for i in possible:
                        grid[y][x] = i
                        replace(grid)
                        grid[y][x] = 0
                final = np.matrix(grid)
                return final


# call the function
print(replace(completed_grid))
