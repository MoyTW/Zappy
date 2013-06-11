__author__ = 'Travis Moy'

import Template
import entity.actor.Actor as Actor
from z_defs import RANK


class TemplateActor(Template.Template):

    # _tools are TemplateTool instances
    # _senses are Sense instances
    def __init__(self, _max_moves=1, _max_hp=1, _tools=None, _senses=None, _image_name=None, _rank=RANK.AVERAGE,
                 _player_controlled=False):
        self._max_moves = _max_moves
        self._max_hp = _max_hp
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name
        self._rank = _rank
        self._player_controlled = _player_controlled

    def create_instance(self, level, entity_index):
        return Actor.Actor(level=level,
                           max_moves=self._max_moves,
                           max_hp=self._max_hp,
                           tools=self._create_tool_list(level, entity_index),
                           senses=self._senses,
                           image_name=self._image_name,
                           rank=self._rank,
                           player_controlled=self._player_controlled)