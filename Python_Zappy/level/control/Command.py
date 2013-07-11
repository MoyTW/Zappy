__author__ = 'Travis Moy'

PRINT_BRIEF, PRINT_NORMAL, PRINT_VERBOSE = range(0, 3)


class Command(object):
    def __init__(self, description, *args):
        self.description = description
        self._fragments = args

    def get_fragment_descriptions(self, wordiness):
        return [f.get_description(wordiness) for f in self._fragments if f.get_description(wordiness) is not None]

    def execute(self, _level):
        for fragment in self._fragments:
            fragment.execute(_level)