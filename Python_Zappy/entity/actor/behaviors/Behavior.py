__author__ = 'Travis Moy'


class Behavior(object):

    # If _can_execute(), _execute()
    def attempt_to_execute(self, level, adversary):
        pass

    # Checks all preconditions
    def _can_execute(self, level, adversary):
        pass

    def _execute(self, level, adversary):
        pass