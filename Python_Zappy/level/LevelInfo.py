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
        try:
            if self._name == other.get_name() and self._height == other.get_height() and \
                    self._number == other.get_number() and self._width == other.get_width() and \
                    self._height == other.get_height():
                try:
                    return self._preview.width == other.get_preview().width and \
                        self._preview.height == other.get_preview().height
                except AttributeError:
                    if self._preview is None and other.get_preview() is None:
                        return True
                    return False
        except AttributeError:
            return False