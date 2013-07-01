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
    def __init__(self, _level, _capture_strength=1, **kwargs):
        kwargs['_list_target_types'] = [self.TYPE_ENTITY]
        kwargs['_requires_LOS'] = True
        self._capture_strength = _capture_strength
        super(ToolManipulator, self).__init__(_level, **kwargs)

        self._captured_actors = list()

    def _special_can_use_on_entity(self, _target):
        try:
            if isinstance(_target, Environmental.Environmental):
                return True
            elif _target.is_stunned() and (_target.get_rank() == RANK.WEAK or
                                          (_target.get_rank() == RANK.AVERAGE and
                                              _target.get_current_hp() <= self._capture_strength)):
                print "Your manipulator is rated to capture this creature!"
                return True
            else:
                print "The creature is not sufficiently weak to capture!"
        except AttributeError:
            return False

    def _effects_of_use_on_entity(self, _target):
        try:
            _target.trigger()
        except AttributeError:
            self._capture(_target)

    def _capture(self, _target):
        self._captured_actors.append(_target)
        self._level.remove_entity_from(_target, *_target.get_coords())