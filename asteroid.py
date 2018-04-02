from random import uniform

from entity import Entity
import config
from utility import *


class Asteroid(Entity):
    def __init__(self, pos, rot_rate=60.0):
        super(Asteroid, self).__init__(pos)
        self.color_f = (0.5, 0.5, 0.5)

        self.rot_speed = self.rot_random(rot_rate)
        self.speed = (-1, 0, 0)

    @staticmethod
    def rot_random(rate):
        return rate, uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)

    def sim(self):
        super(Asteroid, self).sim()

        move = tuple(s * config.delta_t for s in self.speed)
        self.pos = add(self.pos, move)

        # simplified rotation
        angle = self.rot_speed[0] * config.delta_t
        self.rot = (self.rot[0] + angle, self.rot_speed[1], self.rot_speed[2], self.rot_speed[3])
