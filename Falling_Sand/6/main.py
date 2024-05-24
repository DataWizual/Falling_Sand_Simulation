import pygame
import random
from settings import *


def make_2d_array(cols, rows, initial_value=0):
    return [[initial_value for _ in range(rows)] for _ in range(cols)]


def within_cols(i, cols):
    return 0 <= i < cols


def within_rows(j, rows):
    return 0 <= j < rows


def update_grid_state(grid, velocity_grid, cols, rows):
    next_grid = make_2d_array(cols, rows)
    next_velocity_grid = make_2d_array(cols, rows)
    for i in range(cols):
        for j in range(rows):
            state = grid[i][j]
            velocity = velocity_grid[i][j]
            moved = False
            if state > 0:
                new_position = int(j + velocity)
                for y in range(new_position, j, -1):
                    if within_rows(y, rows):
                        below = grid[i][y]
                        direction = 1 if random.random() < 0.5 else -1
                        below_a = grid[i +
                                       direction][y] if within_cols(i + direction, cols) else -1
                        below_b = grid[i -
                                       direction][y] if within_cols(i - direction, cols) else -1
                        if below == 0:
                            next_grid[i][y] = state
                            next_velocity_grid[i][y] = velocity + GRAVITY
                            moved = True
                            break
                        elif below_a == 0:
                            next_grid[i + direction][y] = state
                            next_velocity_grid[i +
                                               direction][y] = velocity + GRAVITY
                            moved = True
                            break
                        elif below_b == 0:
                            next_grid[i - direction][y] = state
                            next_velocity_grid[i -
                                               direction][y] = velocity + GRAVITY
                            moved = True
                            break
            if state > 0 and not moved:
                next_grid[i][j] = grid[i][j]
                next_velocity_grid[i][j] = velocity_grid[i][j] + GRAVITY
    grid = next_grid
    velocity_grid = next_velocity_grid
    return next_grid, next_velocity_grid


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

    hue_value = 200

    grid = make_2d_array(cols, rows)
    velocity_grid = make_2d_array(cols, rows, 1)

    while True:
        screen.fill((0, 0, 0))

        grid, velocity_grid = update_grid_state(
            grid, velocity_grid, cols, rows)

        if pygame.mouse.get_pressed()[0]:
            mouse_col, mouse_row = mouse_position()
            matrix = 6
            extent = matrix // 2
            for i in range(-extent, extent + 1):
                for j in range(-extent, extent + 1):
                    if random.random() < 0.75:
                        col = mouse_col + i
                        row = mouse_row + j
                        if within_cols(col, cols) and within_rows(row, rows):
                            grid[col][row] = hue_value
                            velocity_grid[col][row] = 1
            hue_value += 0.5
            if hue_value > 360:
                hue_value = 1

        for i in range(cols):
            for j in range(rows):
                if grid[i][j] > 0:
                    color = pygame.Color(0)
                    color.hsva = (grid[i][j], 100, 100)
                    pygame.draw.rect(
                        screen, color, (i * CELL, j * CELL, CELL, CELL))

        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == '__main__':
    main()
