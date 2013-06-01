__author__ = 'Travis Moy'


class DummyTemplate(object):

    def __init__(self, name, integer):
        self.name = name
        self.integer = integer

    def create_instance(self):
        return "Instance"

    def __repr__(self):
        return "Name: {0} Integer: {1}".format(self.name, self.integer)

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__