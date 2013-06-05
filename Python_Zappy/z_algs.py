__author__ = 'Travis Moy'

import math


class CellAngles(object):
    def __init__(self, near, center, far):
        self.near = near
        self.center = center
        self.far = far

    def __repr__(self):
        return "(near={0} center={1} far={2})".format(self.near, self.center, self.far)


class ZappyAlgs(object):

    # Changing the radius-fudge changes how smooth the edges of the vision bubble are.
    #
    # RADIUS_FUDGE should always be a value between 0 and 1.
    RADIUS_FUDGE = 1.0 / 3.0

    # If this is False, some cells will unexpectedly be visible.
    #
    # For example, let's say you you have obstructions blocking (0.0 - 0.25) and (.33 - 1.0).
    # A far off cell with (near=0.25, center=0.3125, far=0.375) will have both its near and center unblocked.
    #
    # On certain restrictiveness settings this will mean that it will be visible, but the blocks in front of it will
    # not, which is unexpected and probably not desired.
    #
    # Setting it to True, however, makes the algorithm more restrictive.
    NOT_VISIBLE_BLOCKS_VISION = True

    # Determines how restrictive the algorithm is.
    #
    # 0 - if you have a line to the near, center, or far, it will return as visible
    # 1 - if you have a line to the center and at least one other corner it will return as visible
    # 2 - if you have a line to all the near, center, and far, it will return as visible
    #
    # If any other value is given, it will treat it as a 2.
    RESTRICTIVENESS = 1

    # If VISIBLE_ON_EQUAL is False, an obstruction will obstruct its endpoints. If True, it will not.
    #
    # For example, if there is an obstruction (0.0 - 0.25) and a square at (0.25 - 0.5), the square's near angle will
    # be unobstructed in True, and obstructed on False.
    #
    # Setting this to False will make the algorithm more restrictive.
    VISIBLE_ON_EQUAL = True

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

    # func_transparent is a function with the sig: boolean func(x, y)
    def calc_visible_cells_from(self, x_center, y_center, radius, func_transparent):
        cells = self._visible_cells_in_quadrant_from(x_center, y_center, 1, 1, radius, func_transparent)
        cells.update(self._visible_cells_in_quadrant_from(x_center, y_center, 1, -1, radius, func_transparent))
        cells.update(self._visible_cells_in_quadrant_from(x_center, y_center, -1, -1, radius, func_transparent))
        cells.update(self._visible_cells_in_quadrant_from(x_center, y_center, -1, 1, radius, func_transparent))
        cells.add((x_center, y_center))
        return cells

    # Parameters quad_x, quad_y should only be 1 or -1. The combination of the two determines the quadrant.
    def _visible_cells_in_quadrant_from(self, x_center, y_center, quad_x, quad_y, radius, func_transparent):
        cells = self._visible_cells_in_octant_from(x_center, y_center, quad_x, quad_y, radius, func_transparent, True)
        cells.update(self._visible_cells_in_octant_from(x_center, y_center, quad_x, quad_y, radius, func_transparent,
                                                        False))

        return cells

    def _visible_cells_in_octant_from(self, x_center, y_center, quad_x, quad_y, radius, func_transparent, is_vertical):
        iteration = 1
        visible_cells = set()
        obstructions = list()

        # End conditions:
        #   iteration > radius
        #   Full obstruction coverage (indicated by one object in the obstruction list covering the full angle from 0
        #      to 1)
        while iteration <= radius and not (len(obstructions) == 1 and
                                           obstructions[0].near == 0.0 and obstructions[0].far == 1.0):
            num_cells_in_row = iteration + 1
            angle_allocation = 1.0 / float(num_cells_in_row)

            # Start at the center (vertical or horizontal line) and step outwards
            for step in range(iteration + 1):
                cell = self._cell_at(x_center, y_center, quad_x, quad_y, step, iteration, is_vertical)

                if self._cell_in_radius(x_center, y_center, cell, radius):
                    cell_angles = CellAngles(near=(float(step) * angle_allocation),
                                             center=(float(step + .5) * angle_allocation),
                                             far=(float(step + 1) * angle_allocation))

                    if self._cell_is_visible(cell_angles, obstructions):
                        visible_cells.add(cell)
                        if not func_transparent(*cell):
                            obstructions = self._add_obstruction(obstructions, cell_angles)
                    elif self.NOT_VISIBLE_BLOCKS_VISION:
                        obstructions = self._add_obstruction(obstructions, cell_angles)

            iteration += 1

        return visible_cells

    def _cell_at(self, x_center, y_center, quad_x, quad_y, step, iteration, is_vertical):
        if is_vertical:
            cell = (x_center + step * quad_x, y_center + iteration * quad_y)
        else:
            cell = (x_center + iteration * quad_x, y_center + step * quad_y)
        return cell

    def _cell_in_radius(self, x_center, y_center, cell, radius):
        cell_distance = math.sqrt((x_center - cell[0]) * (x_center - cell[0]) +
                                  (y_center - cell[1]) * (y_center - cell[1]))
        return cell_distance <= float(radius) + self.RADIUS_FUDGE

    def _cell_is_visible(self, cell_angles, obstructions):
        near_visible = True
        center_visible = True
        far_visible = True

        for obstruction in obstructions:
            if self.VISIBLE_ON_EQUAL:
                if obstruction.near < cell_angles.near < obstruction.far:
                    near_visible = False
                if obstruction.near < cell_angles.center < obstruction.far:
                    center_visible = False
                if obstruction.near < cell_angles.far < obstruction.far:
                    far_visible = False
            else:
                if obstruction.near <= cell_angles.near <= obstruction.far:
                    near_visible = False
                if obstruction.near <= cell_angles.center <= obstruction.far:
                    center_visible = False
                if obstruction.near <= cell_angles.far <= obstruction.far:
                    far_visible = False

        if self.RESTRICTIVENESS == 0:
            return center_visible or near_visible or far_visible
        elif self.RESTRICTIVENESS == 1:
            return (center_visible and near_visible) or (center_visible and far_visible)
        else:
            return center_visible and near_visible and far_visible

    # Generates a new list by combining all old obstructions with the new one (removing them if they are combined) and
    # adding the resulting obstruction to the list
    def _add_obstruction(self, obstructions, new_obstruction):
        new_object = CellAngles(new_obstruction.near, new_obstruction.center, new_obstruction.far)
        new_list = [o for o in obstructions if not self._combine_obstructions(o, new_object)]
        new_list.append(new_object)
        return new_list

    # Returns True if you combine, False otherwise
    def _combine_obstructions(self, old, new):
        # Pseudo-sort; if their near values are equal, they overlap
        if old.near < new.near:
            low = old
            high = new
        elif new.near < old.near:
            low = new
            high = old
        else:
            new.far = max(old.far, new.far)
            return True

        # If they overlap, combine and return True
        if low.far >= high.near:
            new.near = min(low.near, high.near)
            new.far = max(low.far, high.far)
            return True

        return False

Z_ALGS = ZappyAlgs()