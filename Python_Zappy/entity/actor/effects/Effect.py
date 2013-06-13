__author__ = 'Travis Moy'


class Effect(object):
    EXTENDS, OVERWRITES, STACKS = range(0, 3)

    EFFECT_NAME = "Effect"

    # Note: We're probably not going to use the _application_behavior var for the forseeable future, but this is a
    # reminder, I suppose. Current behavior with the list is STACKS.
    def __init__(self, _duration, _target, _application_behavior=STACKS):
        self._duration = _duration
        self._target = _target
        self._application_behavior = _application_behavior

    def turn_passed(self):
        self._duration -= 1

    def get_duration(self):
        return self._duration

    def has_expired(self):
        return self._duration < 1

    # This function should be overridden in the child class!
    def apply(self):
        pass

    # This function should be overridden in the child class!
    def unapply(self):
        pass