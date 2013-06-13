__author__ = 'Travis Moy'

import Template
import dummies.DummyTool
import warnings
import entity.tool.Tool as Tool


TOOL_NAMES_DICT = {'dummy': dummies.DummyTool.DummyTool,
                   'tool': Tool.Tool,
                   'manipulator': None,
                   'holoprojector': None,
                   'sampling_laser': None,
                   'zap_gun': None}


# What happens if we can't find the name in the dict?
# Return None.
class TemplateTool(Template.Template):

    def __init__(self, _tool_name='tool', _range=1, _cooldown=0, _energy_cost=0, _image_name=None):
        self._tool_name = _tool_name
        self._range = _range
        self._cooldown = _cooldown
        self._energy_cost = _energy_cost
        self._image_name = _image_name

        self._tool_class = None
        try:
            self._tool_class = TOOL_NAMES_DICT[self._tool_name]
        except KeyError:
            warnings.warn('Cannot create tool! '
                          '{0} is not a recognized tool keyword! '
                          'Valid keywords are: {1}'.format(self._tool_name,
                                                           TOOL_NAMES_DICT.keys()))

    def create_instance(self, level, entity_index):
        if self._tool_class is None:
            return None
        return self._tool_class(_range=self._range, _level=level, _cooldown=self._cooldown,
                                _energy_cost=self._energy_cost, _image_name=self._image_name)