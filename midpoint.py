import pygame
import sys


def draw_circle_midpoint(xc, yc, r):
    x = 0
    y = r
    d = 1 - r

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

def plot_circle_points(xc, yc, x, y):
    # Use 8-way symmetry to draw circle
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc - x, yc + y), WHITE)
    screen.set_at((xc + x, yc - y), WHITE)
    screen.set_at((xc - x, yc - y), WHITE)
    screen.set_at((xc + y, yc + x), WHITE)
    screen.set_at((xc - y, yc + x), WHITE)
    screen.set_at((xc + y, yc - x), WHITE)
    screen.set_at((xc - y, yc - x), WHITE)

pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("mid point circle Drawing Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
       # Draw circle at center of screen with radius 100
        draw_circle_midpoint(WIDTH // 2, HEIGHT //2, 100)
        draw_circle_midpoint(WIDTH // 2, HEIGHT //2, 150)



        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()