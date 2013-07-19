__author__ = 'Travis Moy'

import Tool
import level.commands.CompoundCmd as cmpd
from level.commands.command_fragments import EntityDealDamage


class ToolDoomGun(Tool.Tool):
    def __init__(self, _eid, _level, **kwargs):
        kwargs['_list_target_types'] = [self.TYPE_ENTITY]
        kwargs['_requires_LOS'] = True
        super(ToolDoomGun, self).__init__(_eid=_eid, _level=_level, **kwargs)

    def _effects_of_use_on_entity(self, _target_eid):
        """
        :type _target_eid: int
        :rtype: bool
        """
        cmd_desc = "{0} is blasted for 9999 damage by the DOOM GUN!".format(self._level.entity_name(_target_eid))
        command = cmpd.CompoundCmd(cmd_desc, EntityDealDamage(_target_eid, self._level, 9999))
        self._level.add_command(command)
        return True