__author__ = 'Travis Moy'


class DummyController(object):
    def __init__(self, level):
        self.level = level
        if level is not None:
            self.level_view = level.view
        else:
            self.level_view = None

    def get_level(self):
        return self.level

    @property
    def zappy_eid(self):
        return 0

    @property
    def level_width(self):
        return self.level.level_width

    @property
    def level_height(self):
        return self.level.level_height

    def get_zappy_x_y(self):
        return (0, 0)

    def zappy_attempt_move(self, order):
        self.zappy_attempt_move_called_with = order

    def zappy_use_item(self):
        self.zappy_use_item_called = True

    def zappy_get_tools(self):
        return ["Tool1", "Tool2", "Tool3"]