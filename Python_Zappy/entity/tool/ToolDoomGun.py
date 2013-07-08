__author__ = 'Travis Moy'

import Tool


class ToolDoomGun(Tool.Tool):
    def __init__(self, _eid, _level, **kwargs):
        kwargs['_list_target_types'] = [self.TYPE_ENTITY]
        kwargs['_requires_LOS'] = True
        super(ToolDoomGun, self).__init__(_eid=_eid, _level=_level, **kwargs)

    def _effects_of_use_on_entity(self, _target):
        _target.deal_damage(999)