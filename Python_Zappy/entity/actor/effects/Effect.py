__author__ = 'Travis Moy'


class Effect(object):
    EXTENDS, OVERWRITES, STACKS = range(0, 3)

    EFFECT_NAME = "Effect"
    EFFECT_DESCRIPTION = "This is the base effect! If you're seeing this description, something has gone wrong!"

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

    def apply(self):
        print self._target, "has been afflicted with", self.EFFECT_NAME, "!"
        self._apply_effects()

    def unapply(self):
        print self.EFFECT_NAME, "on", self._target, "has expired!"
        self._unapply_effects()

    # This function should be overridden in the child class!
    def _apply_effects(self):
        pass

    # This function should be overridden in the child class!
    def _unapply_effects(self):
        pass