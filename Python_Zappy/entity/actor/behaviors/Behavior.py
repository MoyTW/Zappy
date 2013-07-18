__author__ = 'Travis Moy'

from level.commands.command_fragments import EntityUseMoves


class Behavior(object):

    def __init__(self, _move_cost=1):
        """
        :type _move_cost: int
        """
        self.move_cost = _move_cost

    # If _can_execute(), _execute()
    # Returns True on successful execution, False otherwise
    def attempt_to_execute(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        if self._can_execute(_target_eid, _level_view, _user):
            return self._execute(_target_eid, _level_view, _user)
        else:
            return False

    def _can_execute(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        return self._general_can_execute(_target_eid, _level_view, _user) and \
            self._special_can_execute(_target_eid, _level_view, _user)

    def _execute(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        if self._execute_effects(_target_eid, _level_view, _user):
            self._on_execute_pay_costs(_user, _level_view)
            return True
        else:
            return False

    # This should be overridden in child classes to add special constraints
    def _special_can_execute(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        return True

    # This should be overridden in child classes to add the actual effects
    def _execute_effects(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        return True

    def _general_can_execute(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        if _target_eid is not None and _user.current_moves >= self.move_cost:
            return True
        else:
            return False

    def _on_execute_pay_costs(self, _user, _level_view):
        """
        :type _user: entity.actor.Adversary.Adversary
        :type _level_view: level.LevelView.LevelView
        """
        _level_view.add_command(EntityUseMoves(_user.eid, _level_view, self.move_cost))