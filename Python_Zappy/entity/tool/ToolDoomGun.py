__author__ = 'Travis Moy'

import Tool


class ToolDoomGun(Tool.Tool):
    def __init__(self, *args, **kwargs):
        kwargs['_list_target_types'] = [self.TYPE_ACTOR]
        kwargs['_requires_LOS'] = True
        super(ToolDoomGun, self).__init__(*args, **kwargs)

    def _effects_of_use_on_entity(self, _target):
        _target.deal_damage(999)