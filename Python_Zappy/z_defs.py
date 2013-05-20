__author__ = 'Travis Moy'


class direction(object):
    N, NE, E, SE, S, SW, W, NW = range(0, 8)

    def get_coords_in_direction_from(self, direction, x, y):
        if direction == self.N:
            return x, y + 1
        elif direction == self.NE:
            return x + 1, y + 1
        elif direction == self.E:
            return x + 1, y
        elif direction == self.SE:
            return x + 1, y - 1
        elif direction == self.S:
            return x, y - 1
        elif direction == self.SW:
            return x - 1, y - 1
        elif direction == self.W:
            return x - 1, y
        elif direction == self.NW:
            return x - 1, y + 1
        else:
            return x, y

DIR = direction()