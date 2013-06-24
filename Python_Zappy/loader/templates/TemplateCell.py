from loader.templates import Template

__author__ = 'Travis Moy'


class TemplateCell(Template.Template):
    def __init__(self, _image_location=None, _passable=True, _transparent=True, _entity_files=None):
        self._image_location = _image_location
        self._passable = _passable
        self._transparent = _transparent

        if _entity_files is None:
            self._entity_files = list()
        else:
            self._entity_files = _entity_files