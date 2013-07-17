__author__ = 'Travis Moy'

PRINT_BRIEF, PRINT_NORMAL, PRINT_VERBOSE, PRINT_DEBUG = range(0, 4)


class Command(object):
    wordiness = PRINT_DEBUG

    def __init__(self, description):
        """
        :type description: str
        """
        self.description = description

    def execute(self, lvl):
        """
        :type lvl: level.Level.Level
        """
        pass

    def get_description(self, wordiness):
        """
        :type wordiness: int
        :rtype: str
        """
        if self.wordiness <= wordiness:
            return self.description