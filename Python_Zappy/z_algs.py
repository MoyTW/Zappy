__author__ = 'Travis Moy'


class ZappyAlgs(object):
    def calc_coords_in_range(self, _range, x_center, y_center):
        coords = set()
        for i in range(_range + 1):
            self._get_coords_in_outer_shell(i, x_center, y_center, coords)
        return coords

    def _get_coords_in_outer_shell(self, _range, x_center, y_center, set_coords):
        for i in range(_range + 1):
            x_alg = i
            y_alg = _range - i
            set_coords.add((x_center + x_alg, y_center + y_alg))
            set_coords.add((x_center + x_alg, y_center - y_alg))
            set_coords.add((x_center - x_alg, y_center + y_alg))
            set_coords.add((x_center - x_alg, y_center - y_alg))

Z_ALGS = ZappyAlgs()