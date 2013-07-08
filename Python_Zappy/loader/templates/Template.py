__author__ = 'Travis Moy'

import warnings


class Template(object):
    def create_instance(self, eid, level, entity_index):
        warnings.warn('Template.create_instance has been called! This should not happen!')

    '''
    def _create_tool_list(self, level, entity_index, user=None):
        warnings.warn("CREATE_TOOL_LIST_CREATES_TOOLS_WITHOUT_USING_ENTITY_INDEX!")
        tool_list = list()
        try:
            if self._tools is not None:
                for template_tool in self._tools:
                    instance = template_tool.create_instance(0, level=level, entity_index=entity_index)
                    if instance is not None:
                        tool_list.append(instance)
            return tool_list
        except AttributeError:
            return None
    '''