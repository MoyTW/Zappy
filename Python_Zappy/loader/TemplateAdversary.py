__author__ = 'Travis Moy'

import Template
import entity.actor.Adversary as Adversary


class TemplateActor(Template.Template):

    # _tools are TemplateTool instances
    # _senses are Sense instances
    def __init__(self, _behaviors, _max_moves, _tools=None, _senses=None, _image_name=None):
        self._behaviors = _behaviors
        self._max_moves = _max_moves
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name

    def create_instance(self, level, entity_index):
        return Adversary.Adversary(level=level,
                                   behaviors=self._behaviors,
                                   max_moves=self._max_moves,
                                   tools=self._create_tool_list(level, entity_index),
                                   senses=self._senses,
                                   image_name=self._image_name)