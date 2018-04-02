import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import config
from entity import Entity


def main():
    pygame.init()
    pygame.display.set_mode(config.resolution, DOUBLEBUF | OPENGL)
    gluPerspective(config.camera_fov, config.resolution[0] / config.resolution[1], 0.1, 50.0)

    glTranslatef(0, 0, config.camera_z)

    test_cube = Entity((0, 0, 0))

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
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        test_cube.draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
