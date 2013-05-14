__author__ = 'Travis Moy'


class Level:
    # cells is a rectangular grid of Cell objects.
    def __init__(self, info, cells=None):
        self._info = info
        self._cells = cells

    def cells_are_none(self):
        pass

    # Should throw some manner of exception if cells is not None
    def set_cells(self, cells):
        pass

    def get_level_info(self):
        pass

    def get_cell_at(self, x, y):
        pass

    def place_entity_at(self, entity, x, y):
        pass

    def remove_entity_from(self, entity, x, y):
        pass