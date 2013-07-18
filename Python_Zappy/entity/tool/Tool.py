__author__ = 'Travis Moy'

import entity.Entity as Entity
from z_algs import Z_ALGS
import warnings


class Tool(Entity.Entity):
    DEFAULT_IMAGE_PATH = 'images/defaults/default_tool.png'
    TYPE_ACTOR, TYPE_ENTITY, TYPE_LOCATION = range(0, 3)

    def __init__(self, _eid, _level, _user=None, _entity_name='Default Tool Name', _list_target_types=None, _range=1,
                 _energy_cost=1, _move_cost=1, _cooldown=0, _image_name=None, _requires_LOS=True, **kwargs):
        """
        :type _eid: int
        :type _level: level.LevelView.LevelView
        :type _entity_name: str
        :type _list_target_types: list
        :type _range: int
        :type _energy_cost: int
        :type _move_cost: int
        :type _cooldown: int
        :type _image_name: str
        :type _requires_LOS: bool
        """
        super(Tool, self).__init__(_eid=_eid, _image_name=_image_name, _level=_level, _entity_name=_entity_name,
                                   **kwargs)
        self.user = _user
        self.range = _range
        self.energy_cost = _energy_cost
        self.move_cost = _move_cost
        self._cooldown = _cooldown
        self._requires_LOS = _requires_LOS
        self._turns_until_ready = 0

        if _list_target_types is None:
            self._list_target_types = list()
        else:
            self._list_target_types = _list_target_types

    @property
    def cooldown(self):
        return self._cooldown

    @cooldown.setter
    def cooldown(self, value):
        self._cooldown = value
        if self._turns_until_ready > self._cooldown:
            self._put_on_cooldown()

    def _put_on_cooldown(self):
        self._turns_until_ready = (self._cooldown + 1)

    @property
    def requires_los(self):
        return self._requires_LOS

    @property
    def turns_until_ready(self):
        return self._turns_until_ready

    def is_ready(self):
        return self._turns_until_ready == 0

    def user_has_energy(self):
        return self.user.current_energy >= self.energy_cost

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
        """
        :type _x: int
        :type _y: int
        :rtype: bool
        """
        return self._can_use_tool_on(self.TYPE_LOCATION, _x, _y) and \
            self._special_can_use_on_location(_x, _y)

    def can_use_on_entity(self, _target):
        """
        :type _target: int
        :rtype: bool
        """
        _target_x, _target_y = _target.get_coords()
        return self._can_use_tool_on(self.TYPE_ENTITY, _target_x, _target_y) and \
            self._special_can_use_on_entity(_target)

    def use_on_location(self, _x, _y):
        """
        :type _x: int
        :type _y: int
        :rtype: bool
        """
        self._on_use_tool_apply_costs()
        return self._effects_of_use_on_location(_x, _y)

    def use_on_entity(self, _target):
        """
        :type _target: int
        :rtype: bool
        """
        self._on_use_tool_apply_costs()
        return self._effects_of_use_on_entity(_target)

    # This function may be overridden to add additional, tool-specific constraints to the Tool.can_use_on_location
    # function.
    def _special_can_use_on_location(self, _x, _y):
        """
        :type _x: int
        :type _y: int
        :rtype: bool
        """
        return True

    # This function may be overridden to add additional, tool-specific constraints to the Tool.can_use_on_entity
    # function.
    def _special_can_use_on_entity(self, _target):
        """
        :type _target: int
        :rtype: bool
        """
        return True

    # This function should be overridden to do whatever it is the tool should do.
    def _effects_of_use_on_location(self, _x, _y):
        """
        :type _x: int
        :type _y: int
        :rtype: bool
        """
        return False

    # This function should be overridden to do whatever it is the tool should do.
    def _effects_of_use_on_entity(self, _target):
        """
        :type _target: int
        :rtype: bool
        """
        return False

    # Call this when the tool is used. Sets the tool on CD, and applies costs.
    def _on_use_tool_apply_costs(self):
        warnings.warn("Tool._on_use_tool_apply_costs() does not use commands!")
        self._put_on_cooldown()
        self.user.use_energy(self.energy_cost)
        self.user.use_moves(self.move_cost)

    def _target_type_is_valid(self, _type):
        if _type == self.TYPE_ENTITY:
            return self.TYPE_ACTOR in self._list_target_types or self.TYPE_ENTITY in self._list_target_types
        return _type in self._list_target_types

    def _satisfies_LOS(self, _x, _y):
        if not self._requires_LOS:
            return True
        u_x, u_y = self.user.get_coords()
        return Z_ALGS.check_los(_x, _y, u_x, u_y, self.range + 1, self._level.cell_is_transparent)

    def _location_in_range(self, _x, _y):
        u_x, u_y = self.user.get_coords()
        cells_in_range = Z_ALGS.calc_coords_in_range(self.range, u_x, u_y)
        return (_x, _y) in cells_in_range

    def _user_has_moves(self):
        return self.user.current_moves >= self.move_cost

    def _can_use_tool_on(self, _type, _t_x, _t_y):
        if not self.is_ready():
            print "TOOL NOT READY"
        elif not self._target_type_is_valid(_type):
            print "TARGET_TYPE_NOT_VALID"
        elif not self.user_has_energy():
            print "USER HAS NO ENERGY"
        elif not self._location_in_range(_t_x, _t_y):
            print "LOCATION NOT IN RANGE"
        elif not self._satisfies_LOS(_t_x, _t_y):
            print "DOES NOT SATISFY LOS"
        elif not self._user_has_moves():
            print "USER HAS NO MOVES"
        can_use = self.is_ready() and self._target_type_is_valid(_type) and self.user_has_energy() and \
                  self._location_in_range(_t_x, _t_y) and self._satisfies_LOS(_t_x, _t_y) and self._user_has_moves()
        return can_use