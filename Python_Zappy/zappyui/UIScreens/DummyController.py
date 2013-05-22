__author__ = 'Travis Moy'


class DummyController(object):
    def __init__(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def get_zappy(self):
        return "zappy"