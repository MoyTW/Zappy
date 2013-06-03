__author__ = 'Travis Moy'

import entity.actor.sense as senses
import Template
import entity.actor.Actor as Actor


class TemplateActor(Template.Template):

    # _tools are TemplateTool instances
    # _senses are Sense instances
    def __init__(self, _max_moves, _tools=None, _senses=None, _image_name=None):
        self._max_moves = _max_moves
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name

    def create_instance(self, level, entity_index):
        return Actor.Actor(level=level,
                           max_moves=self._max_moves,
                           tools=self._create_tool_list(level, entity_index),
                           senses=self._senses,
                           image_name=self._image_name)

    def _create_tool_list(self, level, entity_index):
        tool_list = list()
        for template_tool in self._tools:
            instance = template_tool.create_instance(level=level, entity_index=entity_index)
            if instance is not None:
                tool_list.append(instance)
        return tool_list
