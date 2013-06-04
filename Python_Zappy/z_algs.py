__author__ = 'Travis Moy'


class CellAngles(object):
    def __init__(self, near, center, far):
        self.near = near
        self.center = center
        self.far = far

    def __repr__(self):
        return "(near={0} center={1} far={2})".format(self.near, self.center, self.far)


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

    def calc_visible_cells_from(self, x_center, y_center, radius, func_transparent):
        pass

    def _visible_cells_in_quadrant_from(self, x_center, y_center, quad_x, quad_y, radius, func_transparent):
        pass

    def _visible_cells_in_vertical_octant_from(self, x_center, y_center, quad_x, quad_y, radius, func_transparent):
        iteration = 1
        visible_cells = list()
        obstructions = list()

        # End conditions: iteration <= radius and we do not have full obstruction coverage (indicated by one object
        # in the obstruction list covering the full angle from 0 to 1), keep going
        while iteration <= radius and not (len(obstructions) == 1 and
                                           obstructions[0].near == 0.0 and obstructions[0].far == 1.0):
            num_cells_in_row = iteration + 1
            angle_allocation = 1.0 / float(num_cells_in_row)

            for i in range(iteration + 1):
                cell = ((x_center + i) * quad_x, (y_center + iteration) * quad_y)
                cell_angles = CellAngles(near=(float(i) * angle_allocation),
                                         center=(float(i + .5) * angle_allocation),
                                         far=(float(i + 1) * angle_allocation))

                visible = self._cell_is_visible(cell_angles, obstructions)

                if visible:
                    visible_cells.append(cell)
                    if not func_transparent(*cell):
                        obstructions = self._add_obstruction(obstructions, cell_angles)

            iteration += 1

        return visible_cells

    def _cell_is_visible(self, cell_angles, obstructions):
        near_visible = True
        center_visible = True
        far_visible = True

        for obstruction in obstructions:
            if obstruction.near < cell_angles.near < obstruction.far:
                near_visible = False
            if obstruction.near < cell_angles.center < obstruction.far:
                center_visible = False
            if obstruction.near < cell_angles.far < obstruction.far:
                far_visible = False

        return (center_visible and near_visible) or (center_visible and far_visible)

    # Generates a new list by combining all old obstructions with the new one (removing them if they are combined) and
    # adding the resulting obstruction to the list
    def _add_obstruction(self, obstructions, new_obstruction):
        new_object = CellAngles(new_obstruction.near, new_obstruction.center, new_obstruction.far)
        new_list = [o for o in obstructions if not self._combine_obstructions(o, new_object)]
        new_list.append(new_obstruction)
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
            new.near = low.near
            new.far = high.far
            return True

        return False

Z_ALGS = ZappyAlgs()