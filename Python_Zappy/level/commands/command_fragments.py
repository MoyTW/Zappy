__author__ = 'Travis Moy'

import warnings
import Command as cmd


class EnvironmentalTrigger(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        """
        warnings.warn("EnvironmentalTrigger.execute() is not yet implemented!")
        desc = "{0} has been triggered!".format(lvl_view.entity_names(eid))
        super(EnvironmentalTrigger, self).__init__(desc)

        self.eid = eid

class EntityDealDamage(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view, damage):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        :type damage: int
        """
        warnings.warn("EntityDealDamage.execute() is not yet implemented!")
        desc = "{0} has taken {1} damage!".format(lvl_view.entity_name(eid), damage)
        super(EntityDealDamage, self).__init__(desc)

        self.eid = eid
        self.damage = damage


class EntityUseMoves(cmd.Command):
    wordiness = cmd.PRINT_VERBOSE

    def __init__(self, eid, lvl_view, cost):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        :type cost: int
        """
        warnings.warn("EntityUseMoves.execute() is not yet implemented!")
        desc = "{0} has spent {1} moves!".format(lvl_view.entity_name(eid), cost)
        super(EntityUseMoves, self).__init__(desc)

        self.eid = eid
        self.cost = cost


class LevelPlaceAndAssignEntityID(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, new_entity, x, y):
        """
        :type new_entity: entity.Entity.Entity
        :type x: int
        :type y: int
        """
        warnings.warn("LevelPlaceAndAssignEntityID.execute() is not yet implemented!")
        desc = "A new {0} has appeared at ({1}, {2})!".format(new_entity.entity_name, x, y)
        super(LevelPlaceAndAssignEntityID, self).__init__(desc)

        self.new_entity = new_entity
        self.x = x
        self.y = y


class LevelMoveEntity(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view, o_x, o_y, t_x, t_y):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        :type o_x: int
        :type o_y: int
        :type t_x: int
        :type t_y: int
        """
        warnings.warn("LevelMoveEntity.execute() is not yet implemented!")
        desc = "{0} has moved from ({1}, {2}) to ({3}, {4})!".format(lvl_view.entity_name(eid), o_x, o_y, t_x, t_y)
        super(LevelMoveEntity, self).__init__(desc)

        self.eid = eid
        self.origin = (o_x, o_y)
        self.target = (t_x, t_y)


class LevelRemoveEntity(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        """
        warnings.warn("LevelRemoveEntity.execute() is not yet implemented!")
        desc = "{0} has been removed from the level!".format(lvl_view.entity_name(eid))
        super(LevelRemoveEntity, self).__init__(desc)


# An example of a fragment
class CellSetPassable(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, is_passable, x, y):
        """
        :type is_passable: bool
        :type x: int
        :type y: int
        """
        warnings.warn("CellSetPassable.execute() is not yet implemented!")
        if is_passable:
            description = "({0}, {1}) is now passable!".format(x, y)
        else:
            description = "({0}, {1}) is now impassable!".format(x, y)
        super(CellSetPassable, self).__init__(description)

        self.is_passable = is_passable
        self.x = x
        self.y = y