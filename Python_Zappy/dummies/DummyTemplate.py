__author__ = 'Travis Moy'


class DummyTemplate(object):

    def __init__(self, name, integer):
        self.name = name
        self.integer = integer

    def create_instance(self, eid, level, entity_index):
        return self.__repr__()

    def __repr__(self):
        return "Name: {0} Integer: {1}".format(self.name, self.integer)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except AttributeError:
            return False