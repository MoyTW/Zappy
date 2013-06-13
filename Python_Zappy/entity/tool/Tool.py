__author__ = 'Travis Moy'

import entity.Entity as Entity
import warnings


class Tool(Entity.Entity):
    TYPE_ENTITY, TYPE_LOCATION = range(0, 2)

    def __init__(self, _level, _list_target_types, _range=1, _energy_cost=1, _cooldown=0, _image_name=None,
                 _requires_LOS=True):
        super(Tool, self).__init__(image_name=_image_name, level=_level)
        self._range = _range
        self._list_target_types = _list_target_types
        self._energy_cost = _energy_cost
        self._cooldown = _cooldown
        self._requires_LOS = _requires_LOS
        self._turns_until_ready = 0

    def turn_passed(self):
        if self._turns_until_ready > 0:
            self._turns_until_ready -= 1

    def can_use_on_location(self, _x, _y, _user, _level):
        return self._can_use_tool_on(_type=self.TYPE_LOCATION, t_x=_x, t_y=_y, _user=_user) and \
            self._special_can_use_on_location(_x, _y, _user, _level)

    def can_use_on_entity(self, _target, _user, _level):
        _target_x, _target_y = _target.get_coords()
        return self._can_use_tool_on(_type=self.TYPE_ENTITY, _user=_user, t_x=_target_x, t_y=_target_y) and \
            self._special_can_use_on_entity(_target, _user, _level)

    def use_on_location(self, _x, _y, _user, _level):
        warnings.warn("Tool.use_on_location() was called! This should have been overridden in the child class!")
        return False

    def use_on_entity(self, _target, _user, _level):
        warnings.warn("Tool.use_on_entity() was called! This should have been overridden in the child class!")
        return False

    # This function may be overridden to add additional, tool-specific constraints to the Tool.can_use_on_location
    # function.
    def _special_can_use_on_location(self, _x, _y, _user, _level):
        return True

    # This function may be overridden to add additional, tool-specific constraints to the Tool.can_use_on_entity
    # function.
    def _special_can_use_on_entity(self, _target, _user, _level):
        return True

    def _is_ready(self):
        return self._turns_until_ready == 0

    def _target_type_is_valid(self, _type):
        return _type in self._list_target_types

    def _satisfies_LOS(self, _x, _y, _user):
        if not self._requires_LOS:
            return True

        pass

    def _user_has_energy(self, _user):
        pass

    def _location_in_range(self, _x, _y):
        pass

    def _can_use_tool_on(self, _type, _user, t_x, t_y):
        return self._is_ready() and self._target_type_is_valid(_type) and self._user_has_energy(_user) and \
            self._location_in_range(t_x, t_y) and self._satisfies_LOS(t_x, t_y, _user)

    # Flat-out ignores the 'image' data member.
    def __eq__(self, other):
        try:
            self_dict = self.__dict__
            self_dict.pop('_image')
            other_dict = other.__dict__
            other_dict.pop('_image')
            return self_dict == other_dict
        except AttributeError:
            return False