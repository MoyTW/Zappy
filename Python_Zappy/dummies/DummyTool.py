__author__ = 'Travis Moy'


class DummyTool(object):

    def __init__(self, _range, _energy_cost, _cooldown, _level):
        self._range = _range
        self._energy_cost = _energy_cost
        self._cooldown = _cooldown
        self._level = _level

    '''
    def use_on(self, cell):
        self.use_on_called_with = cell
        return True
    '''

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except AttributeError:
            return False