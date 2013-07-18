__author__ = 'Travis Moy'

import entity.tool.Tool as Tool
import entity.environmentals.Environmental as Environmental
from z_defs import RANK

'''
    The primary purpose of the manipulator is to trigger environmentals.
    The manipulator may also be used to capture stunned enemies.
    The requirements for capture are:
        *Enemy is stunned
        *Enemy is weak OR (enemy is average and its hit points are lower than or equal to the tool's capture strength)
    Capture is functionally identical to death, in that it removes the entity from the level. However, the captured
enemy is 'stored' in the manipulator object instead of added to the level's dead list.
'''


class ToolManipulator(Tool.Tool):

    def __init__(self, _eid, _level, _capture_strength=1, **kwargs):
        """
        :type _eid: int
        :type _level: level.LevelView.LevelView
        :type _capture_strength: int
        """
        kwargs['_list_target_types'] = [self.TYPE_ENTITY]
        kwargs['_requires_LOS'] = True
        self._capture_strength = _capture_strength
        super(ToolManipulator, self).__init__(_eid=_eid, _level=_level, **kwargs)

        self._captured_actors = list()

    def _special_can_use_on_entity(self, _target_eid):
        """
        :type _target_eid: int
        :rtype: int
        """
        try:
            if isinstance(_target_eid, Environmental.Environmental):
                return True
            elif _target_eid.is_stunned and (_target_eid.rank == RANK.WEAK or
                                          (_target_eid.rank == RANK.AVERAGE and
                                              _target_eid.current_hp <= self._capture_strength)):
                print "Your manipulator is rated to capture this creature!"
                return True
            else:
                print "The creature is not sufficiently weak to capture!"
        except AttributeError:
            return False

    def _effects_of_use_on_entity(self, _target_eid):
        """
        :type _target_eid: int
        :rtype: bool
        """
        try:
            _target_eid.trigger()
        except AttributeError:
            self._capture(_target_eid)

    def _capture(self, _target):
        """
        :type _target: int
        :rtype: bool
        """
        self._captured_actors.append(_target)
        self._level.remove_entity_from(_target, *_target.get_coords())