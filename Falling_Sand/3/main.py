import pygame
from settings import *


def make_2d_array(cols, rows, initial_value=0):
    return [[initial_value for _ in range(rows)] for _ in range(cols)]


def update_grid_state(grid, cols, rows):
    new_grid = make_2d_array(cols, rows)
    for i in range(cols):
        for j in range(rows):
            state = grid[i][j]
            if state == 1:
                if j < rows - 1 and grid[i][j + 1] == 0:
                    new_grid[i][j + 1] = 1
                else:
                    new_grid[i][j] = 1
    return new_grid


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Falling sand')
    clock = pygame.time.Clock()

    cols = WIDTH // CELL
    rows = HEIGHT // CELL
    grid = make_2d_array(cols, rows)

    while True:
        screen.fill((0, 0, 0))

        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col, row = mouse_x // CELL, mouse_y // CELL
            grid[col][row] = 1

        grid = update_grid_state(grid, cols, rows)

        for i in range(cols):
            for j in range(rows):
                x = i*CELL
                y = j*CELL
                rect = pygame.Rect(x, y, CELL, CELL)
                pygame.draw.rect(
                    screen, (grid[i][j] * 255, grid[i][j] * 255, grid[i][j] * 255), rect, 0)
                pygame.draw.rect(screen, (127, 127, 127), rect, 1)

        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == '__main__':
    main()
