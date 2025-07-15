import pygame
import sys
import math


pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Trasformation")
WHITE = (255, 255, 255)
red = (255, 0,0)
BLACK = (0, 0, 0)
color = (100,200,0)

def translation(x1,y1,x2,y2):
    pygame.draw.line(screen ,WHITE ,(x1,y1),(x2,y2),5)
    tx=120
    ty=120
    x1a = x1 + tx 
    y1a = y1 + ty
    x2a = x2 + tx
    y2a = y2 + tx
    pygame.draw.line(screen ,red ,(x1a,y1a),(x2a,y2a),5)

def scaling(x1,y1,x2,y2):

    sx=1
    sy=2
    x1aa = x1 * sx
    y1aa = y1 * sy
    x2aa = x2 * sx
    y2aa = y2 * sy
    
    pygame.draw.line(screen , color ,(x1aa,y1aa),(x2aa,y2aa),5)

def rotation(x1,y1,x2,y2):
    a=math.radians(-15)
    x1aaa = x1 * math.cos(a)- y1 * math.sin(a)
    y1aaa = x1 * math.sin(a)+ y1 * math.cos(a)
    x2aaa = x2 * math.cos(a)- y2 * math.sin(a)
    y2aaa = x2 * math.sin(a)- y2 * math.cos(a)
    pygame.draw.line(screen , color ,(x1aaa,y1aaa),(x2aaa,y2aaa),5)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        x1=150
        y1=150
        x2=100
        y2=100
        translation(x1,y1,x2,y2)
        scaling(x1,y1,x2,y2)
        rotation(x1,y1,x2,y2)
       


       
        pygame.display.flip()
        pygame.time.delay(100)


if __name__ == "__main__":
    main()
