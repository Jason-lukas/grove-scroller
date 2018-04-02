import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import config


def main():
    pygame.init()
    pygame.display.set_mode(config.resolution, DOUBLEBUF|OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                    
        # sim
            # move
            # coll
        # draw


main()
