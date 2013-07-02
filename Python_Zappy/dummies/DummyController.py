__author__ = 'Travis Moy'


class DummyController(object):
    def __init__(self, level):
        self.level = level

    def get_level(self):
        return self.level

    @property
    def zappy(self):
        return "zappy"

    def get_zappy_x_y(self):
        return (0, 0)

    def zappy_attempt_move(self, order):
        self.zappy_attempt_move_called_with = order

    def zappy_use_item(self):
        self.zappy_use_item_called = True

    def zappy_get_tools(self):
        return ["Tool1", "Tool2", "Tool3"]