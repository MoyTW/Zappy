__author__ = 'Travis Moy'

import Template
import entity.actor.Adversary as Adversary


class TemplateAdversary(Template.Template):

    # _tools are TemplateTool instances
    # _senses are Sense instances
    def __init__(self, _behaviors=None, _max_moves=1, _max_hp=1, _tools=None, _senses=None, _image_name=None):
        self._behaviors = _behaviors
        self._max_hp = _max_hp
        self._max_moves = _max_moves
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name

    def create_instance(self, level, entity_index):
        return Adversary.Adversary(level=level,
                                   behaviors=self._behaviors,
                                   max_moves=self._max_moves,
                                   max_hp=self._max_hp,
                                   tools=self._create_tool_list(level, entity_index),
                                   senses=self._senses,
                                   image_name=self._image_name)