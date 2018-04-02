import pygame

import config
from utility import *


def get_input():
    # weź mysz
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    # ogranicz do ekranu
    mouse_x = clamp(mouse_x, 0, config.resolution[0])
    mouse_y = clamp(mouse_y, 0, config.resolution[1])
    # przeskaluj na jednostki
    x = lerp(config.x_min, config.x_max, float(mouse_x)/float(config.resolution[0]))
    y = -lerp(config.y_min, config.y_max, float(mouse_y) / float(config.resolution[1]))

    return x, y
