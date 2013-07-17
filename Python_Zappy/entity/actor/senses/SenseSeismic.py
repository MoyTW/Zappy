__author__ = 'Travis Moy'

import Sense
from z_algs import Z_ALGS


class SenseSeismic(Sense.Sense):

    def __init__(self, _range):
        super(SenseSeismic, self).__init__(_range=_range)

    def detect_entities(self, x_pos, y_pos, level):
        """
        :type x_pos: int
        :type y_pos: int
        :type level: level.LevelView.LevelView
        """
        detected = list()
        coords = Z_ALGS.calc_coords_in_range(self._range, x_pos, y_pos)

        for coord in coords:
            entities = level.get_eids_at(coord[0], coord[1])
            if entities is not None:
                for entity in entities:
                    detected.append(entity)

        return detected