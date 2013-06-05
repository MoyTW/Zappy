__author__ = 'Travis Moy'

import Sense
from z_algs import Z_ALGS


class SenseSight(Sense.Sense):

    def __init__(self, _range):
        super(SenseSight, self).__init__(_range=_range)

    def detect_entities(self, x_pos, y_pos, level):
        detected = list()
        coords = Z_ALGS.calc_visible_cells_from(x_pos, y_pos, self._range, level.cell_is_transparent)

        for coord in coords:
            entities = level.get_all_entities_at(coord[0], coord[1])
            if entities is not None:
                for entity in entities:
                    detected.append(entity)

        return detected