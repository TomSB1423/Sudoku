import numpy as np
# sudoku grid 9x9

grid_3x3 = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

grid_9x9 = [
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

grid_12x12 = [
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


# Change grid array here
grid = np.asarray(grid_3x3)


# find possible numbers that could be inserted into space


def find_size(grid):
    if np.asarray(grid).shape[0] % 3 == 0 and np.asarray(grid).shape[1] % 3 == 0:
        size = np.asarray(grid).shape[0]
        replace(grid, size)
        return
    else:
        print("The grid is not in the form of a sudoku puzzle")
        return


def possibilities(y, x, size):
    square_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_list = []
    for i in range(1, size + 1):
        num_list.append(i)
    # find numbers in corrosponding y axis
    for i in range(0, size):
        if grid[y][i] in num_list:
            num_list.remove(grid[y][i])
    # find numbers in corrosponding x axis
    for j in range(0, size):
        if grid[j][x] in num_list:
            num_list.remove(grid[j][x])
    # find valid numbers in small square
    for i in range(0, 3):
        for j in range(0, 3):
            grid_check = grid[j + ((y//3)*3)][i + ((x//3)*3)]
            if grid_check in square_list:
                square_list.remove(grid_check)
    print(num_list, square_list)

    for i in range(len(square_list)):
        if square_list[i] not in num_list:
            print(num_list)
            num_list.append(square_list[i])
    return num_list

# replace each missing value


def replace(grid, size):
    # loop in y
    for y in range(0, size):
        # loop in x
        for x in range(0, size):
            if grid[y][x] == 0:
                # check possible numbers that can be inserted
                possible = possibilities(y, x, size)
                if possible:
                    for i in possible:
                        grid[y][x] = i
                        replace(grid, size)
                        grid[y][x] = 0
                return

    print(np.matrix(grid))
    input("Press a key to attempt to find more solutions")


# call the function
find_size(grid)
print("Could not find any solutions")
