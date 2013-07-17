__author__ = 'Travis Moy'

from level.commands.command_fragments import EntityUseMoves


class Behavior(object):

    def __init__(self, _move_cost=1):
        self._move_cost = _move_cost

    @property
    def move_cost(self):
        return self._move_cost

    # If _can_execute(), _execute()
    # Returns True on successful execution, False otherwise
    def attempt_to_execute(self, _target_eid, _level_view, _user_eid):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user_eid: int
        :rtype: bool
        """
        if self._can_execute(_target_eid, _level_view, _user_eid):
            return self._execute(_target_eid, _level_view, _user_eid)
        else:
            return False

    def _can_execute(self, _target_eid, _level_view, _user_eid):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user_eid: int
        :rtype: bool
        """
        return self._general_can_execute(_target_eid, _level_view, _user_eid) and \
            self._special_can_execute(_target_eid, _level_view, _user_eid)

    def _execute(self, _target_eid, _level_view, _user_eid):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user_eid: int
        :rtype: bool
        """
        if self._execute_effects(_target_eid, _level_view, _user_eid):
            self._on_execute_pay_costs(_user_eid, _level_view)
            return True
        else:
            return False

    # This should be overridden in child classes to add special constraints
    def _special_can_execute(self, _target_eid, _level_view, _user_eid):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user_eid: int
        :rtype: bool
        """
        return True

    # This should be overridden in child classes to add the actual effects
    def _execute_effects(self, _target_eid, _level_view, _user_eid):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user_eid: int
        :rtype: bool
        """
        return False

    def _general_can_execute(self, _target_eid, _level_view, _user_eid):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user_eid: int
        :rtype: bool
        """
        if _target_eid is not None and _user_eid.current_moves >= self._move_cost:
            return True
        else:
            return False

    def _on_execute_pay_costs(self, _user_eid, _level_view):
        """
        :type _user_eid: int
        :type _level_view: level.LevelView.LevelView
        """
        _level_view.add_command(EntityUseMoves(_user_eid, _level_view, self._move_cost))