__author__ = 'Travis Moy'


class LoaderCellDefinition(object):
    def __init__(self, image_location, passable, entity_strings):
        self.image_location = image_location
        self.passable = passable
        self.entity_strings = entity_strings

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "(img_loc: {0} | passable: {1} | entity_strs: {2})".format(self.image_location, self.passable,
                                                                          self.entity_strings)