__author__ = 'Travis Moy'

import entity.Entity as Entity
from z_algs import Z_ALGS


class Tool(Entity.Entity):
    DEFAULT_IMAGE_PATH = 'images/defaults/default_tool.png'
    TYPE_ACTOR, TYPE_ENTITY, TYPE_LOCATION = range(0, 3)

    def __init__(self, _level, _user=None, _entity_name='Default Tool Name', _list_target_types=None, _range=1, _energy_cost=1,
                 _cooldown=0, _image_name=None, _requires_LOS=True):
        super(Tool, self).__init__(_image_name=_image_name, _level=_level, _entity_name=_entity_name)
        self._user = _user
        self._range = _range
        self._energy_cost = _energy_cost
        self._cooldown = _cooldown
        self._requires_LOS = _requires_LOS
        self._turns_until_ready = 0

        if _list_target_types is None:
            self._list_target_types = list()
        else:
            self._list_target_types = _list_target_types

    # This function may be overridden to add additional, tool-specific constraints to the Tool.can_use_on_location
    # function.
    def _special_can_use_on_location(self, _x, _y):
        return True

    # This function may be overridden to add additional, tool-specific constraints to the Tool.can_use_on_entity
    # function.
    def _special_can_use_on_entity(self, _target):
        return True

    # This function should be overridden to do whatever it is the tool should do.
    def _effects_of_use_on_location(self, _x, _y):
        return False

    # This function should be overridden to do whatever it is the tool should do.
    def _effects_of_use_on_entity(self, _target):
        return False

    def targets_actors(self):
        return self.TYPE_ACTOR in self._list_target_types

    def targets_locations(self):
        return self.TYPE_LOCATION in self._list_target_types

    def targets_entities(self):
        return self.TYPE_ENTITY in self._list_target_types

    def turn_passed(self):
        if self._turns_until_ready > 0:
            self._turns_until_ready -= 1

    def can_use_on_location(self, _x, _y):
        return self._can_use_tool_on(self.TYPE_LOCATION, _x, _y) and \
               self._special_can_use_on_location(_x, _y)

    def can_use_on_entity(self, _target):
        _target_x, _target_y = _target.get_coords()
        return self._can_use_tool_on(self.TYPE_ENTITY, _target_x, _target_y) and \
               self._special_can_use_on_entity(_target)

    def use_on_location(self, _x, _y):
        self._on_use_tool_apply_costs()
        return self._effects_of_use_on_location(_x, _y)

    def use_on_entity(self, _target):
        self._on_use_tool_apply_costs()
        return self._effects_of_use_on_entity(_target)

    # Call this when the tool is used. Sets the tool on CD, and applies costs.
    def _on_use_tool_apply_costs(self):
        self._user.use_energy(self._energy_cost)
        self._turns_until_ready += (self._cooldown + 1)

    def _is_ready(self):
        return self._turns_until_ready == 0

    def _target_type_is_valid(self, _type):
        return _type in self._list_target_types

    def _satisfies_LOS(self, _x, _y):
        if not self._requires_LOS:
            return True
        u_x, u_y = self._user.get_coords()
        print u_x, u_y
        return Z_ALGS.check_los(_x, _y, u_x, u_y, self._range + 1, self._level.cell_is_transparent)

    def _user_has_energy(self):
        return self._user.get_current_energy() >= self._energy_cost

    def _location_in_range(self, _x, _y):
        u_x, u_y = self._user.get_coords()
        cells_in_range = Z_ALGS.calc_coords_in_range(self._range, u_x, u_y)
        return (_x, _y) in cells_in_range

    def _can_use_tool_on(self, _type, _t_x, _t_y):
        return self._is_ready() and self._target_type_is_valid(_type) and self._user_has_energy() and \
               self._location_in_range(_t_x, _t_y) and self._satisfies_LOS(_t_x, _t_y)

    # Flat-out ignores the 'image' data member.
    def __eq__(self, other):
        try:
            self_dict = self.__dict__
            self_dict.pop('_image')
            other_dict = other.__dict__
            other_dict.pop('_image')
            self_list = self_dict.pop('_list_target_types')
            other_list = other_dict.pop('_list_target_types')
            print self_list, other_list
            return self_dict == other_dict and sorted(self_list) == sorted(other_list)
        except AttributeError:
            return False