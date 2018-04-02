from random import uniform

import config


class Spawner:
    def __init__(self, drawn, simulated, spawned_class, delay):
        self.drawn = drawn
        self.simulated = simulated
        self.spawned_class = spawned_class
        self.delay = delay
        self.time_left = self.delay

    def sim(self):
        self.time_left -= config.delta_t
        if self.time_left <= 0:
            x = config.x_max + config.margin
            y = uniform(config.y_min, config.y_max)
            z = 0

            spawned = self.spawned_class((x, y, z))
            self.drawn.append(spawned)
            self.simulated.append(spawned)

            self.time_left += uniform(0.5, 1.5)* self.delay
