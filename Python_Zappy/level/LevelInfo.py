__author__ = 'Travis Moy'


class LevelInfo:
    def __init__(self, name, number, width, height, preview):
        self._name = name
        self._number = number
        self._width = width
        self._height = height
        self._preview = preview

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_preview(self):
        return self._preview

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__