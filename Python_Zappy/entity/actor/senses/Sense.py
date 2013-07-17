__author__ = 'Travis Moy'


class Sense(object):

    def __init__(self, _range):
        """:type _range: int"""
        self._range = _range

        self.is_active = True
        """:type: bool"""

    def detect_entities(self, x_pos, y_pos, level_view):
        """
        :type x_pos: int
        :type y_pos: int
        :type level_view: level.LevelView.LevelView
        :rtype: list
        """
        if self.is_active:
            return self._detect_entities(x_pos, y_pos, level_view)
        else:
            return []

    def _detect_entities(self, x_pos, y_pos, level_view):
        pass