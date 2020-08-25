import pygame
from Sudoku_9x9 import *
# from 9x9_Sudoku import possibilities, replace


def create_window():
    # setting up environment
    (height, width) = (452, 500)
    background_colour = (255, 255, 255)
    screen = pygame.display.set_mode((height, width))
    screen.fill(background_colour)
    pygame.display.set_caption('Sudoku')
    return screen


def board_setup(screen):
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, (0, 0, 0),
                             (50*i, 50*j, 50, 50), 1)
            if (j) % 3 == 0:
                pygame.draw.line(screen, (128, 128, 128), (50*i, 50*j),
                                 (450, 50*j), 4)
            elif (i) % 3 == 0:
                pygame.draw.line(screen, (128, 128, 128), (50*i, 0),
                                 (50*i, 450), 4)
            j += 1

        i += 1
    pygame.draw.line(screen, (128, 128, 128), (0, 450),
                     (450, 450), 4)
    pygame.draw.line(screen, (128, 128, 128), (450, 0),
                     (450, 450), 4)


def display_matrix(grid, screen):
    global font
    for i in range(9):
        for j in range(9):
            num = grid[j][i]
            if num != 0:
                img = font.render(str(num), 1, (0, 0, 0))
                screen.blit(img, (18 + 50*i, 8 + 50*j))


def on_click(grid, screen):
    mouse_pos = pygame.mouse.get_pos()
    column = mouse_pos[0] // (50)
    row = mouse_pos[1] // (50)
    if column <= 8 and row <= 8:
        # pygame.draw.rect(screen, (255, 0, 0),
        # (50*column, 50*row, 50, 50), 3)
        # pygame.display.flip()
        return (row, column)


def wrong_num():
    pass


def detect_key(event):
    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
        return 1
    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
        return 2
    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
        return 3
    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
        return 4
    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
        return 5
    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
        return 6
    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
        return 7
    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
        return 8
    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
        return 9


def main(grid):
    screen = create_window()
    board_setup(screen)
    display_matrix(grid, screen)
    pygame.display.flip()
    running = True
    pos = None
    #solved_grid = replace(grid)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = on_click(grid, screen)
            elif pos != None and grid[pos[0]][pos[1]] == 0 and event.type == pygame.KEYDOWN:
                key = detect_key(event)
                print(solved_grid, key)


pygame.init()
font = pygame.font.SysFont('Arial', 30)
main(completed_grid)
pygame.quit()
