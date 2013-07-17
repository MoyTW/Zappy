__author__ = 'Travis Moy'


class CommandLog(object):
    def __init__(self):
        self._entries = list()
        self._latest_unexecuted = 0

    @property
    def latest_unexecuted(self):
        return self._latest_unexecuted

    def add_command(self, cmd):
        """:type cmd: level.commands.Command.Command"""
        self._entries.append(cmd)

    def execute_commands(self, n=-1):
        """:type n: int"""
        pass

    def get_command_descriptions(self, wordiness, n=10):
        """
        :type wordiness: int
        :type n: int
        :rtype: list
        """
        if n <= 0:
            target_entries = self._entries
        else:
            target_entries = self._entries[max(len(self._entries) - n, 0):len(self._entries)]
        return [f.get_description(wordiness) for f in target_entries if f.get_description(wordiness) is not None]

    def __getitem__(self, item):
        """:rtype: level.commands.CompoundCmd.CompoundCmd"""
        return self._entries[item]

    def __len__(self):
        return len(self._entries)