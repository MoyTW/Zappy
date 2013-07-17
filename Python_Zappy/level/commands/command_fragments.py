__author__ = 'Travis Moy'

import warnings
import CompoundCmd as cmd


class CommandFragment(object):
    wordiness = cmd.PRINT_DEBUG

    def __init__(self, description):
        """
        :type description: str
        """
        self.description = description

    def execute(self, lvl):
        """
        :type lvl: level.Level.Level
        """
        pass

    def get_description(self, wordiness):
        """
        :type wordiness: int
        :rtype: str
        """
        if self.wordiness <= wordiness:
            return self.description


class LevelRemoveEntity(CommandFragment):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid):
        warnings.warn("LevelRemoveEntity.execute() is not yet implemented!")
        super(LevelRemoveEntity, self).__init__("{0} has been removed from the level!".format(eid))

    def execute(self, lvl):
        pass


# An example of a fragment
class CellSetPassable(CommandFragment):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, is_passable, x, y):
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