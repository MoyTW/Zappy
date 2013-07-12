__author__ = 'Travis Moy'

import warnings
import level.Record as Record


class RecordEntry(object):
    def __init__(self, wordiness=Record.PRINT_NORMAL):
        self.wordiness = wordiness
        self._description = "This is a base RecordEntry! I don't know how it got here, but it shouldn't be here."

    def get_description(self, wordiness):
        if self.wordiness >= wordiness:
            return self._description


class CustomEntry(RecordEntry):
    def __init__(self, description, wordiness):
        super(CustomEntry, self).__init__(wordiness)
        self._description = description


class EntityDamaged(RecordEntry):
    def __init__(self, target, damage, wordiness=Record.PRINT_NORMAL):
        super(EntityDamaged, self).__init__(wordiness)
        self.damage = damage
        self.target = target
        self._description = "{0} has taken {1} damage!".format(self.target, self.damage)


class LocationDamaged(RecordEntry):
    pass


class EntityMoved(RecordEntry):
    pass


class EntityCreated(RecordEntry):
    pass


class EntityRemoved(RecordEntry):
    pass