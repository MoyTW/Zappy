__author__ = 'Travis Moy'

import record_entries

PRINT_BRIEF, PRINT_NORMAL, PRINT_VERBOSE = range(0, 3)


class Record(object):
    def __init__(self):
        self._entries = list()
        self._entries.append(record_entries.CustomEntry("Recording started!", wordiness=PRINT_BRIEF))

    def add_entry(self, entry):
        self._entries.append(entry)

    def get_entries(self, wordiness):
        return [f.get_description(wordiness) for f in self._entries if f.get_description(wordiness) is not None]


# Normally I would not encourage these kinds of shenanigans, but it's a logging system. As such the data flow only goes
# one way, and it's therefore fine.
RECORD = Record()