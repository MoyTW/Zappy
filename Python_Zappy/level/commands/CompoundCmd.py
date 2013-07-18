__author__ = 'Travis Moy'

import Command as cmd


class CompoundCmd(cmd.Command):
    wordiness = cmd.PRINT_BRIEF

    # CompoundCmd takes an arbitrary number of Command objects.
    def __init__(self, description, *args):
        super(CompoundCmd, self).__init__(description)
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

    def __getitem__(self, item):
        """:rtype: level.commands.Command"""
        return self.fragments[item]