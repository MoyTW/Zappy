__author__ = 'Travis Moy'

import warnings
import Command as cmd


class EntityUseMoves(cmd.Command):
    wordiness = cmd.PRINT_VERBOSE

    def __init__(self, eid, lvl_view, cost):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        :type cost: int
        """
        warnings.warn("EntityUseMoves.execute() is not yet implemented!")
        desc = "{0} has spent {1} moves!".format(lvl_view.get_entity_name(eid), cost)
        super(EntityUseMoves, self).__init__(desc)

        self.cost = cost
        self.eid = eid

    def execute(self, lvl):
        pass


class LevelRemoveEntity(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        """
        warnings.warn("LevelRemoveEntity.execute() is not yet implemented!")
        desc = "{0} has been removed from the level!".format(lvl_view.get_entity_name(eid))
        super(LevelRemoveEntity, self).__init__(desc)

    def execute(self, lvl):
        pass


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

    def execute(self, lvl):
        pass