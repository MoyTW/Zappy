__author__ = 'Travis Moy'

import Template
import warnings
import entity.tool.Tool as Tool
import entity.tool.ToolZapGun as ZapGun


TOOL_NAMES_DICT = {'tool': Tool.Tool,
                   'manipulator': None,
                   'holoprojector': None,
                   'sampling_laser': None,
                   'zap_gun': ZapGun.ToolZapGun}


# What happens if we can't find the name in the dict?
# Return None.
class TemplateTool(Template.Template):

    def __init__(self, _tool_name='tool', _range=1, _cooldown=0, _energy_cost=0, _image_name=None):
        self._tool_name = _tool_name
        self._range = _range
        self._cooldown = _cooldown
        self._energy_cost = _energy_cost
        self._image_name = _image_name

    def create_instance(self, level, entity_index):
        _tool_class = None
        try:
            _tool_class = TOOL_NAMES_DICT[self._tool_name]
        except KeyError:
            warnings.warn('Cannot create tool! '
                          '{0} is not a recognized tool keyword! '
                          'Valid keywords are: {1}'.format(self._tool_name,
                                                           TOOL_NAMES_DICT.keys()))

        if _tool_class is None:
            print "RETURNING NONE FROM TempalteTool.create_instance()"
            return None
        return _tool_class(_level=level,
                                # These two should be decided on a class-by-class basis!
                                #_requires_LOS=self._requires_LOS
                                #_list_target_types=self._list_target_types,
                                _range=self._range,
                                _energy_cost=self._energy_cost,
                                _cooldown=self._cooldown,
                                _image_name=self._image_name)