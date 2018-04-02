import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import config
from utility import *
from entity import Entity
from my_input import *


def main():
    pygame.init()
    pygame.display.set_mode(config.resolution, DOUBLEBUF | OPENGL)
    gluPerspective(config.camera_fov, config.resolution[0] / config.resolution[1], 0.1, 50.0)

    glTranslatef(0, 0, config.camera_z)

    test_cube = Entity((0, 0, 0))

    move = 0.5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_w:
                    test_cube.pos = add(test_cube.pos, (0, move, 0))
                if event.key == pygame.K_s:
                    test_cube.pos = add(test_cube.pos, (0, -move, 0))
                if event.key == pygame.K_a:
                    test_cube.pos = add(test_cube.pos, ( -move, 0, 0))
                if event.key == pygame.K_d:
                    test_cube.pos = add(test_cube.pos, (move, 0, 0))

                print("x: {} y: {} z: {}".format(test_cube.pos[0], test_cube.pos[1], test_cube.pos[2]))

        mouse_pos = get_input()
        test_cube.pos = (mouse_pos[0], mouse_pos[1], 0)

        # sim
        # move
        # coll
        # draw
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        test_cube.draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
