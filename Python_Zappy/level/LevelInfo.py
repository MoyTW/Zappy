__author__ = 'Travis Moy'

import pyglet
import warnings
import os


class LevelInfo:
    PATH_TOP = os.path.split(os.path.dirname(__file__))[0]
    PREVIEW_LOADER = pyglet.resource.Loader(script_home=PATH_TOP)
    DEFAULT_LOADER = pyglet.resource.Loader('@assets')

    def __init__(self, _name, _number, _width, _height, _previews_folder):
        """
        :type _name: str
        :type _number: int
        :type _width: int
        :type _height: int
        :type _previews_folder: str
        """
        self.info_version = .1
        self.info_name = _name
        self.info_number = _number
        self.info_width = _width
        self.info_height = _height
        self._previews_folder = _previews_folder

        self.info_preview_image = self._return_preview_image()

    def to_json(self, obj):
        json_dict = self.__dict__.copy()
        json_dict.pop('preview_image')
        json_dict.pop('level_version')
        json_dict.update({'__class__': self.__class__.__name__, '__module__': self.__module__})
        return json_dict

    def _return_default_preview(self):
        return self.DEFAULT_LOADER.image('images/defaults/default_preview.png')

    def _return_preview_image(self):
        path = "{0}/preview_images/{1}.png".format(self._previews_folder, self.info_number)

        try:
            return self.PREVIEW_LOADER.image(path)
        except pyglet.resource.ResourceNotFoundException:
            warnstr = "There is no preview available for level {0}".format(self.info_number)
            warnings.warn(warnstr, RuntimeWarning)
            return self._return_default_preview()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        """
        :type other: LevelInfo
        :rtype: bool
        """
        try:
            return sorted(self.__dict__) == sorted(other.__dict__)
        except AttributeError:
            return False