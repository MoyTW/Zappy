__author__ = 'Travis Moy'

import pyglet
import warnings
import os


class LevelInfo:
    _path_top = os.path.split(os.path.dirname(__file__))[0]
    _preview_loader = pyglet.resource.Loader(script_home=_path_top)
    _default_loader = pyglet.resource.Loader('@assets')

    def __init__(self, _name, _number, _width, _height, _levels_folder):
        self._version = .1
        self._name = _name
        self._number = _number
        self._width = _width
        self._height = _height
        self._levels_folder = _levels_folder

        self._preview_image = self._return_preview_image()

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

    def to_json(self, obj):
        json_dict = self.__dict__.copy()
        json_dict.pop('_preview_image')
        json_dict.update({'__class__': self.__class__.__name__, '__module__': self.__module__})
        return json_dict

    def _return_default_preview(self):
        return self._default_loader.image('images/defaults/default_preview.png')

    def _return_preview_image(self):
        path = "{0}/preview_images/{1}.png".format(self._levels_folder, self._number)

        try:
            return self._preview_loader.image(path)
        except pyglet.resource.ResourceNotFoundException:
            warnstr = "There is no preview available for level {0}".format(self._number)
            warnings.warn(warnstr, RuntimeWarning)
            return self._return_default_preview()

    def __eq__(self, other):
        try:
            return self._name == other.get_name() and self._height == other.get_height() and \
                self._number == other.get_number() and self._width == other.get_width()
        except AttributeError:
            return False