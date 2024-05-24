import pygame
from settings import *


def make_2d_array(cols, rows, initial_value=0):
    return [[initial_value for _ in range(rows)] for _ in range(cols)]


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Falling sand')
    clock = pygame.time.Clock()

    cols = WIDTH // CELL
    rows = HEIGHT // CELL
    grid = make_2d_array(cols, rows)
    grid[20][10] = 1

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

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


if __name__ == '__main__':
    main()
