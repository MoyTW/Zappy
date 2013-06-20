__author__ = 'Travis Moy'

import Template
import entity.actor.Actor as Actor
from z_defs import RANK
from entity.actor.Faction import FACTIONS


class TemplateActor(Template.Template):

    # _tools are TemplateTool instances
    # _senses are Sense instances
    def __init__(self, _entity_name='Default Actor Name', _max_moves=1, _max_hp=1, _tools=None, _senses=None,
                 _image_name=None, _rank=RANK.AVERAGE, _faction=FACTIONS.DEFAULT, _base_threat=1):
        self._entity_name = _entity_name
        self._max_moves = _max_moves
        self._max_hp = _max_hp
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name
        self._rank = _rank
        self._faction = _faction
        self._base_threat = _base_threat

    def create_instance(self, level, entity_index):
        actor = Actor.Actor(_level=level,
                            _entity_name=self._entity_name,
                            _max_hp=self._max_hp,
                            _max_moves=self._max_moves,
                            _senses=self._senses,
                            _image_name=self._image_name,
                            _rank=self._rank,
                            _faction=self._faction,
                            _base_threat=self._base_threat)
        tools = self._create_tool_list(level, entity_index, actor)
        actor.init_tool_list(tools)
        return actor