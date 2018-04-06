import my_input
from entity import Entity
import config
import utility


target_y = my_input.mouse_y


class Ship(Entity):
    def sim(self):
        move = config.max_speed * config.delta_t
        y = utility.clamp(target_y, self.pos[1] - move, self.pos[1] + move)
        pos = (self.pos[0], y, self.pos[2])
