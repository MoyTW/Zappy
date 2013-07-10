__author__ = 'Travis Moy'

import math
import algorithms.RestrictivePreciseAngleShadowcasting as RPAS
import algorithms.AStar as AStar


class ZappyAlgs(object):
    rpas = RPAS.RestrictivePreciseAngleShadowcasting()

    def a_star_from_to(self, origin, destination, level):
        self.level = level
        path = AStar.find_path(origin, destination,
                               func_list_adjacent_nodes=self._list_adjacent_nodes,
                               func_calculate_move_cost=self._calculate_move_cost,
                               func_node_is_passable=self._is_passable,
                               func_estimate_cost=self._estimate_cost)
        self.level = None
        return path

    def _list_adjacent_nodes(self, coords):
        return [(coords[0]+1, coords[1]), (coords[0], coords[1]+1), (coords[0]-1, coords[1]), (coords[0], coords[1]-1)]

    def _calculate_move_cost(self, origin, destination):
        return 1

    def _is_passable(self, coords):
        return self.level.cell_is_passable(*coords)

    def _estimate_cost(self, origin, destination):
        return math.sqrt(((destination[0] - origin[0]) * (destination[0] - origin[0])) +
                         ((destination[1] - origin[1]) * (destination[1] - origin[1])))

    # Takes a function with the sig: boolean f(x, y) as func_transparent.
    # Returns a set of (x, y) tuples, indicating the coordinates of all visible cells from the (x_center, y_center).
    def calc_visible_cells_from(self, x_center, y_center, radius, func_transparent):
        return self.rpas.calc_visible_cells_from(x_center, y_center, radius, func_transparent)

    # LOS is mutal - that is, if the target has LOS to the origin, the origin has LOS to the target.
    # However, the origin always has LOS to itself. Therefore, it does matter which order the coordinates are given.
    def check_los(self, target_x, target_y, origin_x, origin_y, radius, func_transparent):
        return self.rpas.check_los(target_x, target_y, origin_x, origin_y, radius, func_transparent)

    def calc_coords_in_range(self, _range, x_center, y_center):
        coords = set()
        for i in range(_range + 1):
            self._get_coords_in_outer_shell(i, x_center, y_center, coords)
        return coords

    # Internal functions to calc_coords_in_range
    def _get_coords_in_outer_shell(self, _range, x_center, y_center, set_coords):
        for i in range(_range + 1):
            x_alg = i
            y_alg = _range - i
            set_coords.add((x_center + x_alg, y_center + y_alg))
            set_coords.add((x_center + x_alg, y_center - y_alg))
            set_coords.add((x_center - x_alg, y_center + y_alg))
            set_coords.add((x_center - x_alg, y_center - y_alg))

Z_ALGS = ZappyAlgs()