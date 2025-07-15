import pygame
import sys

def bresenham(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)

    x=x1
    y=y1
    if(x2>x1):
        lx=1
    else:
        lx=-1
    if(y2>y1):
        ly=1
    else:
        ly=-1
    
    if(dx>dy):
        p=2*dy-dx
        while x != x2:
            if(p<0):
                x=x+lx
                y=y
                p=p+2*dy
            else:
                x=x+lx
                y=y+lx
                p=p+2*dy-2*dx
            screen.set_at((round(x), round(y)), WHITE)
            
    else:
        p=2*dx-2*dy
        while y != y2:
            if(p<0):
                x=x
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+lx
                p=p+2*dx-2*dy
            screen.set_at((round(x), round(y)), WHITE)


pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Bresenham Line Drawing Algorithm")

WHITE = (12, 15, 255)
BLACK = (255, 255, 255)


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        bresenham(50, 50, 750, 50)     # Top line
        bresenham(50, 550, 750, 550)   # Bottom line
        bresenham(50, 50, 50, 550)     # Left line
        bresenham(750, 50, 750, 550)   # Right line

        bresenham(400, 50, 400, 550)  #middle line

        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()