__author__ = 'Travis Moy'

import entity.Entity
import warnings


class Tool(entity.Entity):
    def __init__(self, _level, _range=1, _energy_cost=1, _cooldown=0, _image_name=None):
        super(Tool, self).__init__(image_name=_image_name, level=_level)
        self._range = _range
        self._energy_cost = _energy_cost
        self._cooldown = _cooldown
        self._turns_until_ready = 0

    def is_ready(self):
        return self._turns_until_ready == 0

    def turn_passed(self):
        self._turns_until_ready -= 1

    def use_on_location(self, _x, _y, _user, _level):
        warnings.warn("Tool.use_on_location() was called! This should have been overridden in the child class!")
        return False

    def can_use_on_entity(self, _target, _user, _level):
        warnings.warn("Tool.can_use_on_entity() was called! This should have been overridden in the child class!")
        return False

    def use_on_entity(self, _target, _user, _level):
        warnings.warn("Tool.use_on_entity() was called! This should have been overridden in the child class!")
        return False

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except AttributeError:
            return False