__author__ = 'Travis Moy'

import Sense
from z_algs import Z_ALGS


class SenseSeismic(Sense.Sense):

    def __init__(self, _range, level):
        super(SenseSeismic, self).__init__(_range=_range, level=level)

    def detect_entities(self, x_pos, y_pos):
        detected = list()
        coords = Z_ALGS.calc_coords_in_range(self._range, x_pos, y_pos)

        for coord in coords:
            entities = self._level.get_all_entities_at(coord[0], coord[1])
            if entities is not None:
                for entity in entities:
                    detected.append(entity)

        return detected