__author__ = 'Travis Moy'

import warnings


class LevelView(object):
    def __init__(self, lvl):
        """
        :type lvl: level.Level.Level
        """
        self.lvl = lvl

    def player_coords(self):
        return self.lvl.player_actor.get_coords()

    def player_sight_range(self):
        return self.lvl.player_actor._senses[0].range

    def is_destructible(self, eid):
        entity = self._get_entity_by_id(eid)
        try:
            return callable(entity.deal_damage)
        except AttributeError:
            return False

    def is_triggerable(self, eid):
        entity = self._get_entity_by_id(eid)
        """:type: entity.environmentals.Environmental.Environmental"""
        try:
            return callable(entity.trigger)
        except AttributeError:
            return False

    def des_curr_hp(self, eid):
        entity = self._get_entity_by_id(eid)
        """:type: entity.Destructible.Destructible"""
        if entity is not None:
            return entity.current_hp
        else:
            return None

    def act_faction(self, eid):
        entity = self._get_entity_by_id(eid)
        """:type: entity.actor.Actor.Actor"""
        if entity is not None:
            return entity.faction
        else:
            return None

    def act_faction_name(self, eid):
        entity = self._get_entity_by_id(eid)
        """:type: entity.actor.Actor.Actor"""
        if hasattr(entity, 'get_faction_name') and callable(entity.get_faction_name):
            return entity.get_faction_name()
        else:
            return ''

    def act_threat(self, eid):
        entity = self._get_entity_by_id(eid)
        """:type: entity.actor.Actor.Actor"""
        if entity is not None:
            return entity.threat
        else:
            return -1

    def act_rank(self, eid):
        entity = self._get_entity_by_id(eid)
        """:type: entity.actor.Actor.Actor"""
        if entity is not None:
            return entity.rank
        else:
            return None

    def act_is_stunned(self, eid):
        entity = self._get_entity_by_id(eid)
        """:type: entity.actor.Actor.Actor"""
        if entity is not None:
            return entity.is_stunned
        else:
            return None

    def act_current_moves(self, eid):
        entity = self._get_entity_by_id(eid)
        """:type: entity.actor.Actor.Actor"""
        try:
            return entity.current_moves
        except AttributeError:
            return None

    def ent_coords(self, eid):
        entity = self._get_entity_by_id(eid)
        if entity is not None:
            return entity.get_coords()
        else:
            return None

    def ent_name(self, eid):
        entity = self._get_entity_by_id(eid)
        if entity is not None:
            return entity.entity_name
        else:
            return None

    def add_command(self, cmd):
        """
        :type cmd: level.commands.Command.Command
        """
        self.lvl.add_command(cmd)

    def get_display_images_at(self, x, y, _in_fow=False):
        """
        :type x: int
        :type y: int
        :type _in_fow: bool
        :rtype: dict
        """
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].get_display_images(_in_fow)
        return None

    def get_cell_at(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: level.Cell.Cell
        """
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y]
        return None

    def cell_is_passable(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].is_passable
        return False

    def cell_is_transparent(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].is_transparent
        return False

    # Horrifying, really. A more efficient (but more work-intensive) way would be to maintain an internal list, and to
    # update it each time an entity is placed or removed.
    #
    # However, until it becomes a problem performance-wise, just leave it at this.
    def get_all_eids(self):
        """
        :rtype: list
        """
        entities = list()
        for x in range(self.lvl.level_width):
            for y in range(self.lvl.level_height):
                entities.extend(self.get_eids_at(x, y))
        return entities

    def get_eids_at(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: list
        """
        if self.lvl.are_valid_coords(x, y):
            return [e.eid for e in self.lvl._cells[x][y].get_all_entities()]
        return None

    def _get_entity_by_id(self, eid):
        """
        :type eid: int
        :rtype: entity.Entity.Entity
        """
        return self.lvl.get_entity_by_id(eid)

    def _get_all_entities(self):
        """
        :rtype: list
        """
        return self.lvl.get_all_entities()