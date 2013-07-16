__author__ = 'Travis Moy'


class CommandLog(object):
    def __init__(self):
        self._entries = list()

    def add_command(self, entry):
        self._entries.append(entry)

    def get_commands(self, wordiness, num=10):
        if num <= 0:
            target_entries = self._entries
        else:
            target_entries = self._entries[max(len(self._entries) - num, 0):len(self._entries)]
        return [f.get_description(wordiness) for f in target_entries if f.get_description(wordiness) is not None]