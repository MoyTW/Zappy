__author__ = 'Travis Moy'


class LevelException(Exception):
    pass


class LevelCellsAlreadySetError(LevelException):
    pass


class LevelHeightNotMatchedByCells(LevelException):
    pass


class LevelWidthNotMatchedByCells(LevelException):
    pass