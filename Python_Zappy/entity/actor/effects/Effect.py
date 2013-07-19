__author__ = 'Travis Moy'

import warnings


class Effect(object):
    EXTENDS, OVERWRITES, STACKS = range(0, 3)

    EFFECT_NAME = "Effect"
    EFFECT_DESCRIPTION = "This is the base effect! If you're seeing this description, something has gone wrong!"

    # Note: We're probably not going to use the _application_behavior var for the forseeable future, but this is a
    # reminder, I suppose. Current behavior with the list is STACKS.
    def __init__(self, _duration, _target, _application_behavior=STACKS):
        """
        :type _duration: int
        :type _target: int
        :type _application_behavior: int
        """
        self._duration = _duration
        self._target = _target
        self._application_behavior = _application_behavior

    @property
    def duration(self):
        return self._duration

    def turn_passed(self):
        self._duration -= 1

    def get_duration(self):
        return self._duration

    def has_expired(self):
        return self._duration < 1

    @property
    def target(self):
        return self._target

    def apply(self):
        try:
            self._apply_effects()
            print self._target.ent_name, "has been afflicted with", self.EFFECT_NAME, "- ", self._duration, \
                "rounds remaining."
        except AttributeError as e:
            warnings.warn(e.message)

    def unapply(self):
        try:
            self._unapply_effects()
            print self.EFFECT_NAME, "on", self._target, "has expired!"
        except AttributeError as e:
            warnings.warn(e.message)

    # This function should be overridden in the child class!
    def _apply_effects(self):
        pass

    # This function should be overridden in the child class!
    def _unapply_effects(self):
        pass