from loader.templates import Template

__author__ = 'Travis Moy'

import level.Cell as Cell


class TemplateCell(Template.Template):
    DEFAULT_IMAGE_PATH = 'images/defaults/defaultcell.png'

    def __init__(self, _image_location=DEFAULT_IMAGE_PATH, _passable=True, _transparent=True, _entity_files=None):
        self._image_location = _image_location
        self._passable = _passable
        self._transparent = _transparent

        if _entity_files is None:
            self._entity_files = list()
        else:
            self._entity_files = _entity_files

    # This is kind of awkward; we're jumping up and down levels, here.
    # I mean, we're not placing the entity in the cell - we're placing it at _x, _y, which we're *hoping* but can't be
    # assured corresponds to this particular cell.

    # NOTE: This behaves radically differently from the other Templates, in that it DOES NOT RETURN, and it places the
    # Cell directly into the level! That may potentially be confusing down the line (or if somebody else happens to
    # look at this - ha! not likely...) - is it worth it to disambiguate, or is a long note enough?
    def create_instance(self, level, entity_index, _x, _y):
        cell = Cell.Cell(image_location=self._image_location,
                         passable=self._passable,
                         transparent=self._transparent)
        level._cells[_x][_y] = cell
        for entity_file in self._entity_files:
            entity = entity_index.create_entity_by_name(entity_file, level)
            level.place_entity_at(entity, _x, _y)
        return cell

    def __eq__(self, other):
        try:
            return self._image_location == other._image_location and self._passable == other._passable and \
                   self._transparent == other._transparent and sorted(self._entity_files) == sorted(other._entity_files)
        except AttributeError:
            return False