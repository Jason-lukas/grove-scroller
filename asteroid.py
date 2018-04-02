from random import uniform

from entity import Entity
import config
from utility import *


class Asteroid(Entity):
    def __init__(self, rot_rate=60.0):
        super(Asteroid, self).__init__()
        self.rot_speed = self.rot_random(rot_rate)
        self.speed = (-1, 0, 0)

    @staticmethod
    def rot_random(rate):
        return rate, uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)

    def sim(self):
        super(Asteroid, self).sim(self)

        move = (s * config.delta_t for s in self.speed)
        self.pos = add(self.pos, move)
