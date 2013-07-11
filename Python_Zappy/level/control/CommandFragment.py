__author__ = 'Travis Moy'

import warnings
import Command


class CommandFragment(object):
    def __init__(self, wordiness=Command.PRINT_NORMAL):
        self.wordiness = wordiness

    def get_description(self, wordiness):
        warnings.warn("CommandFragment.get_description() has been called; a subclass has failed to override it!")

    def execute(self, _level):
        warnings.warn("CommandFragment.execute() has been called; a subclass has failed to override it!")