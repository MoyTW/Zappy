__author__ = 'Travis Moy'

PRINT_BRIEF, PRINT_NORMAL, PRINT_VERBOSE, PRINT_DEBUG = range(0, 4)


class CompoundCmd(object):
    wordiness = PRINT_BRIEF

    # CompoundCmd takes an arbitrary number of CommandFragment objects.
    def __init__(self, description, *args):
        self.description = description
        self.fragments = args

    # Executes the fragments in order.
    def execute(self, lvl):
        for fragment in self.fragments:
            fragment.execute(lvl)

    def get_description(self, wordiness):
        ret_desc = self.description
        for fragment in self.fragments:
            desc = fragment.get_description(wordiness)
            if desc is not None:
                ret_desc += "\n\t{0}".format(desc)
        return ret_desc