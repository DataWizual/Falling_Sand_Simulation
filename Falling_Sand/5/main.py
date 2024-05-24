import pygame
import random
from settings import *


def make_2d_array(cols, rows, initial_value=0):
    return [[initial_value for _ in range(rows)] for _ in range(cols)]


def update_grid_state(grid, cols, rows):
    new_grid = make_2d_array(cols, rows)

    for i in range(cols):
        for j in range(rows):
            state = grid[i][j]
            if state == 1:
                direction = 1
                if random.uniform(0, 1) < 0.5:
                    direction *= -1
                if j == rows - 1:
                    new_grid[i][j] = 1
                elif grid[i][j + 1] == 0:
                    new_grid[i][j + 1] = 1
                elif 0 <= i + direction <= cols - 1 and grid[i+direction][j+1] == 0:
                    new_grid[i+direction][j+1] = 1
                elif 0 <= i - direction <= cols - 1 and grid[i-direction][j+1] == 0:
                    new_grid[i-direction][j+1] = 1
                else:
                    new_grid[i][j] = 1
    return new_grid


def mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_col, mouse_row = mouse_x // CELL, mouse_y // CELL
    return mouse_col, mouse_row


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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        matrix = 3
        extend = matrix // 2
        for i in range(-extend, extend + 1):
            for j in range(-extend, extend + 1):
                if pygame.mouse.get_pressed()[0]:
                    mouse_col, mouse_row = mouse_position()
                    col = mouse_col + i
                    row = mouse_row + j
                    if 0 <= col <= cols - 1 and 0 <= row <= rows - 1:
                        grid[col][row] = 1

        grid = update_grid_state(grid, cols, rows)

        for i in range(cols):
            for j in range(rows):
                if grid[i][j] == 1:
                    x = i*CELL
                    y = j*CELL
                    rect = pygame.Rect(x, y, CELL, CELL)
                    color = (grid[i][j] * 255, grid[i]
                             [j] * 255, grid[i][j] * 255)
                    pygame.draw.rect(
                        screen, color, rect, 0)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
