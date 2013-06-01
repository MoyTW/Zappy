__author__ = 'Travis Moy'

import entity.actor.sense as senses
import Template
import entity.actor.Actor as Actor


class TemplateActor(Template.Template):

    def __init__(self, _max_moves, _tools=None, _senses=None, _image_name=None):
        self._max_moves = _max_moves
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name

    def create_instance(self, level, entity_index):
        pass

    def _create_tool(self, template_tool):
        pass

    def _create_sense(self, template_sense):
        pass