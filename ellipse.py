import pygame
import sys


def ellipsemidpoint(rx:float, ry:float, xc:float, yc:float):
    x = 0
    y = ry
    rx2 = rx ** 2
    ry2 = ry ** 2
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    # Region 1
    while dx < dy:
        plot_ellipse_points(xc, yc, x, y)
        x += 1
        dx = 2 * ry2 * x
        if p1 < 0:
            p1 += dx + ry2
        else:
            y -= 1
            dy = 2 * rx2 * y
            p1 += dx - dy + ry2

    # Region 2
    p2 = (ry2) * ((x + 0.5) ** 2) + (rx2) * ((y - 1) ** 2) - (rx2 * ry2)

    while y != 0:
        plot_ellipse_points(xc, yc, x, y)
        y -= 1
        dy = 2 * rx2 * y
        if p2 > 0:
            p2 -= dy + rx2
        else:
            x += 1
            dx = 2 * ry2 * x
            p2 += dx - dy + rx2


def plot_ellipse_points(xc, yc, x, y):
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc - x, yc + y), WHITE)
    screen.set_at((xc + x, yc - y), WHITE)
    screen.set_at((xc - x, yc - y), WHITE)


# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Draw multiple ellipses
        ellipsemidpoint(18, 18, WIDTH // 2, HEIGHT // 2)
        ellipsemidpoint(100, 50, WIDTH // 2, HEIGHT // 2)
        ellipsemidpoint(15, 15, WIDTH // 3, HEIGHT // 5)
        ellipsemidpoint(15, 15, WIDTH // 5, HEIGHT // 2)
        
        ellipsemidpoint(15, 15, 100, 200)


        ellipsemidpoint(150, 75, WIDTH // 2, HEIGHT // 2)
        ellipsemidpoint(200,100, WIDTH // 2 ,HEIGHT // 2)
        ellipsemidpoint(250,125, WIDTH // 2 ,HEIGHT // 2)
        ellipsemidpoint(300,150, WIDTH // 2 ,HEIGHT // 2)
        ellipsemidpoint(350,175, WIDTH // 2 ,HEIGHT // 2)
        ellipsemidpoint(400,200, WIDTH // 2 ,HEIGHT // 2)
        ellipsemidpoint(450,225, WIDTH // 2 ,HEIGHT // 2)



        pygame.display.flip()
        pygame.time.delay(100)


if __name__ == "__main__":
    main()
