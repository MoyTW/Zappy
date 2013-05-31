__author__ = 'Travis Moy'

import entity.actor.sense as senses
import Template


class TemplateActor(Template.Template):
    SENSES = {'seismic': senses.SenseSeismic}

    def __init__(self, _max_moves, _tools=None, _senses=None, _image_name=None):
        self._max_moves = _max_moves
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name

    def create_instance(self, level, entity_index):
        pass