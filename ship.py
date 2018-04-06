import my_input
from entity import Entity
import config
import utility


target_y = my_input.mouse_y


class Ship(Entity):
    def sim(self):
        move = config.max_speed * config.delta_t
        y = utility.clamp(target_y, pos[1] - move, pos[1] + move)
        pos = (pos[0], y, pos[2])
