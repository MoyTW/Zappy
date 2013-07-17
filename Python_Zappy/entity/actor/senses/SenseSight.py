__author__ = 'Travis Moy'

import Sense
from z_algs import Z_ALGS


class SenseSight(Sense.Sense):

    def _detect_entities(self, x_pos, y_pos, level_view):
        """
        :type x_pos: int
        :type y_pos: int
        :type level_view: level.LevelView.LevelView
        """
        detected = list()
        coords = Z_ALGS.calc_visible_cells_from(x_pos, y_pos, self._range, level_view.cell_is_transparent)

        for coord in coords:
            entities = level_view.get_eids_at(coord[0], coord[1])
            if entities is not None:
                for entity in entities:
                    detected.append(entity)

        return detected