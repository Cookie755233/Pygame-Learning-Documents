import pprint as pp
import pygame
import sys
import time

SCREEN_WIDTH = 800
CELLSIZE = 10

x, y = 150, 200

position = [[x+CELLSIZE*i, y] for i in range(50)] +\
           [[x+CELLSIZE*50, y+CELLSIZE*i] for i in range(50)] +\
           [[x+CELLSIZE*50-CELLSIZE*i, y+CELLSIZE*50]for i in range(50)] +\
           [[x, y+CELLSIZE*50-CELLSIZE*i]for i in range(50)]


def path(list, width):
    output = []
    if len(list) < width:
        width = len(list)
    for i in range(len(list) + width - 1):
        if i+1 < width:
            output.append(list[0:i+1])
        elif i+1 >= width:
            output.append(list[i+1-width: i+1])
        elif i+1 > len(list):
            output.append(list[i+1-width-len(list)::])
    return output

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    draw_pos = path(position, 10)

    count = 0
    while True:
        clock.tick(10)

        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        
                    count = 0
                    while count < 1: 
                        for pos in draw_pos:
                            for block in pos:
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
                                    block[0], block[1], CELLSIZE, CELLSIZE), 0)
                            pygame.display.update()
                            time.sleep(0.01)
                            # screen.fill((255, 255, 255))
                        count += 1
        pygame.display.update()