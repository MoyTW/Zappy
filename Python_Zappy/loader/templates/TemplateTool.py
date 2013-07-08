from loader.templates import Template

__author__ = 'Travis Moy'

import warnings
import entity.tool.Tool as Tool
import entity.tool.ToolZapGun as ToolZapGun
import entity.tool.ToolDoomGun as ToolDoomGun
import entity.tool.ToolHoloprojector as ToolHoloprojector
import entity.tool.ToolSamplingLaser as ToolSamplingLaser
import entity.tool.ToolManipulator as ToolManipulator


TOOL_NAMES_DICT = {
    'tool': Tool.Tool,
    'manipulator': ToolManipulator.ToolManipulator,
    'holoprojector': ToolHoloprojector.ToolHoloprojector,
    'sampling_laser': ToolSamplingLaser.ToolSamplingLaser,
    'zap_gun': ToolZapGun.ToolZapGun,
    'doom_gun': ToolDoomGun.ToolDoomGun
}


# What happens if we can't find the name in the dict?
# Return None.
class TemplateTool(Template.Template):

    def __init__(self, _tool_class='tool', _entity_name='Default Tool Name', _range=1, _cooldown=0, _energy_cost=0,
                 _image_name=None):
        self._tool_class = _tool_class
        self._entity_name = _entity_name
        self._range = _range
        self._cooldown = _cooldown
        self._energy_cost = _energy_cost
        self._image_name = _image_name

    def create_instance(self, eid, level, entity_index, user=None):
        _tool_class = None
        try:
            _tool_class = TOOL_NAMES_DICT[self._tool_class]
        except KeyError:
            warnings.warn('Cannot create tool! '
                          '{0} is not a recognized tool keyword! '
                          'Valid keywords are: {1}'.format(self._tool_class,
                                                           TOOL_NAMES_DICT.keys()))

        if _tool_class is None:
            warnings.warn("RETURNING NONE FROM TempalteTool.create_instance()")
            return None
        return _tool_class(_eid=eid,
                           _level=level,
                           _user=user,
                           _entity_name=self._entity_name,
                           _range=self._range,
                           _energy_cost=self._energy_cost,
                           _cooldown=self._cooldown,
                           _image_name=self._image_name)