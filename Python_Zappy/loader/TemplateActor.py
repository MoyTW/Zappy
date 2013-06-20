__author__ = 'Travis Moy'

import Template
import entity.actor.Actor as Actor
from z_defs import RANK
from entity.actor.Faction import FACTIONS


class TemplateActor(Template.Template):

    # _tools are TemplateTool instances
    # _senses are Sense instances
    def __init__(self, _entity_name='Default Actor Name', _max_moves=1, _max_hp=1, _tools=None, _senses=None,
                 _image_name=None, _rank=RANK.AVERAGE, _faction=FACTIONS.DEFAULT):
        self._entity_name = _entity_name
        self._max_moves = _max_moves
        self._max_hp = _max_hp
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name
        self._rank = _rank
        self._faction = _faction

    def create_instance(self, level, entity_index):
        actor = Actor.Actor(_level=level,
                            _entity_name=self._entity_name,
                            max_hp=self._max_hp,
                            max_moves=self._max_moves,
                            senses=self._senses,
                            _image_name=self._image_name,
                            rank=self._rank,
                            faction=self._faction)
        tools = self._create_tool_list(level, entity_index, actor)
        actor.init_tool_list(tools)
        return actor