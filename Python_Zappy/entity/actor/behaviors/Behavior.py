__author__ = 'Travis Moy'


class Behavior(object):

    def __init__(self, _move_cost=1):
        self._move_cost = _move_cost

    @property
    def move_cost(self):
        return self._move_cost

    # If _can_execute(), _execute()
    # Returns True on successful execution, False otherwise
    def attempt_to_execute(self, _target, _level, _user):
        if self._can_execute(_target, _level, _user):
            return self._execute(_target, _level, _user)
        else:
            return False

    def _can_execute(self, _target, _level, _user):
        return self._general_can_execute(_target, _level, _user) and \
               self._special_can_execute(_target, _level, _user)

    def _execute(self, _target, _level, _user):
        if self._execute_effects(_target, _level, _user):
            self._on_execute_pay_costs(_user)
            return True
        else:
            return False

    # This should be overridden in child classes to add special constraints
    def _special_can_execute(self, _target, _level, _user):
        return True

    # This should be overridden in child classes to add the actual effects
    def _execute_effects(self, _target, _level, _user):
        return False

    def _general_can_execute(self, _target, _level, _user):
        if _target is not None and _user.current_moves >= self._move_cost:
            return True
        else:
            return False

    def _on_execute_pay_costs(self, _user):
        _user.use_moves(self._move_cost)