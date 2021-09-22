
import pprint as pp
import pygame
import sys
import time
import math


SCREEN_WIDTH = 800
CELLSIZE = 10


class Coordinates():
    def __init__(self, x, y, width, height):
        ''' if circle, width=height=radius '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def rectangle(self):
        Ox = self.x - 1/2*self.width
        Oy = self.y - 1/2*self.height
        output = [[Ox+w, Oy] for w in range(self.width)] +\
                 [[Ox+self.width, Oy+h] for h in range(self.height)] +\
                 [[Ox+self.width-w, Oy+self.height] for w in range(self.width)] +\
                 [[Ox, Oy+self.height-h] for h in range(self.height)]
        return output

    def circle(self) -> list:
        output = []
        for i in [k*0.1 for k in range(3600)]:
            Ox = self.x + self.width * math.sin(math.radians(i))
            Oy = self.y + self.height * math.cos(math.radians(i))
            output.append([Ox, Oy])
        return output


def animation_path(list, width):
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

square = Coordinates(300, 300, 50, 100).rectangle()

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

    count = 0
    while True:
        clock.tick(10)

        screen.fill((255, 255, 255))
        for i in square:
            pygame.draw.rect(screen, (255, 0, 0),
                             pygame.Rect(i[0], i[1], 1, 1), 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ani_square = animation_path(square, 15)
                    count = 0
                    while count < 1:
                        for pos in ani_square:
                            for p in pos:
                                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(
                                    p[0], p[1], 1, 1), 0)
                            pygame.display.update()
                            # screen.fill((255, 255, 255))
                        count += 1
        pygame.display.update()


main()
