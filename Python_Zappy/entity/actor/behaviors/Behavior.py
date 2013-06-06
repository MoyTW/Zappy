__author__ = 'Travis Moy'


class Behavior(object):

    # If _can_execute(), _execute()
    # Returns True on successful execution, False otherwise
    def attempt_to_execute(self, level, adversary):
        if self._can_execute(level, adversary):
            return self._execute(level, adversary)
        else:
            return False

    # Checks all preconditions
    def _can_execute(self, level, adversary):
        pass

    def _execute(self, level, adversary):
        pass