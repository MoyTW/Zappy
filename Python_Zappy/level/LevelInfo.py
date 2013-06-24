__author__ = 'Travis Moy'


class LevelInfo:
    def __init__(self, _name, _number, _width, _height, _preview_location):
        self._name = _name
        self._number = _number
        self._width = _width
        self._height = _height
        self._preview_location = _preview_location
        self._preview_image = _preview_location

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_preview(self):
        return self._preview_image

    def __eq__(self, other):
        try:
            if self._name == other.get_name() and self._height == other.get_height() and \
                    self._number == other.get_number() and self._width == other.get_width() and \
                    self._height == other.get_height():
                try:
                    return self._preview_image.width == other.get_preview().width and \
                        self._preview_image.height == other.get_preview().height
                except AttributeError:
                    if self._preview_image is None and other.get_preview() is None:
                        return True
                    return False
        except AttributeError:
            return False