__author__ = 'Travis Moy'

import warnings
import level.control.CommandFragment as CommandFragment
import Command


class DamageEntity(CommandFragment.CommandFragment):
    def __init__(self, source, damage, target, wordiness=Command.PRINT_NORMAL):
        super(DamageEntity, self).__init__(wordiness=wordiness)
        self.source = source
        self.damage = damage
        self.target = target

    def get_description(self, wordiness):
        if self.wordiness >= wordiness:
            return "{0} dealt {1} damage to {2}!".format(self.source, self.damage, self.target)

    def execute(self, _level):
        try:
            self.target.deal_damage(self.damage)
        except AttributeError as e:
            warnings.warn(e)


class DamageLocation(CommandFragment.CommandFragment):
    pass


class MoveEntity(CommandFragment.CommandFragment):
    pass


class CreateEntity(CommandFragment.CommandFragment):
    pass


class RemoveEntityFromLevel(CommandFragment.CommandFragment):
    pass