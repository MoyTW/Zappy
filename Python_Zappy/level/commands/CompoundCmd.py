__author__ = 'Travis Moy'

PRINT_BRIEF, PRINT_NORMAL, PRINT_VERBOSE, PRINT_DEBUG = range(0, 4)


class CompoundCmd(object):
    wordiness = PRINT_BRIEF

    # CompoundCmd takes an arbitrary number of CommandFragment objects.
    def __init__(self, description, *args):
        pass

    # Executes the fragments in order.
    def execute(self, lvl):
        pass

    def get_description(self, wordiness):
        pass