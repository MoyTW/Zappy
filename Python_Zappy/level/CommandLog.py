__author__ = 'Travis Moy'


class CommandLog(object):
    def __init__(self):
        self._entries = list()
        self._latest_unexecuted = 0

    @property
    def latest_unexecuted(self):
        return self._latest_unexecuted

    def add_command(self, cmd):
        """
        :type cmd: level.commands.CompoundCmd.CompoundCmd
        """
        self._entries.append(cmd)

    def execute_commands(self, num=-1):
        pass

    def get_command_descriptions(self, wordiness, num=10):
        if num <= 0:
            target_entries = self._entries
        else:
            target_entries = self._entries[max(len(self._entries) - num, 0):len(self._entries)]
        return [f.get_description(wordiness) for f in target_entries if f.get_description(wordiness) is not None]