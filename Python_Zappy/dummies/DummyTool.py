__author__ = 'Travis Moy'


class DummyTool(object):

    def __init__(self, _range, _energy_cost, _cooldown, _level, _image_name=None):
        self._range = _range
        self._energy_cost = _energy_cost
        self._cooldown = _cooldown
        self._level = _level

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except AttributeError:
            return False