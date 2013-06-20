__author__ = 'Travis Moy'

import Template
import entity.actor.Adversary as Adversary
from z_defs import RANK
from entity.actor.Faction import FACTIONS


class TemplateAdversary(Template.Template):

    # _tools are TemplateTool instances
    # _senses are Sense instances
    def __init__(self, _entity_name='Default Adversary Template', _behaviors=None, _max_moves=1, _max_hp=1, _tools=None,
                 _senses=None, _image_name=None, _rank=RANK.AVERAGE, _faction=FACTIONS.ADVERSARY):
        self._entity_name = _entity_name
        self._behaviors = _behaviors
        self._max_hp = _max_hp
        self._max_moves = _max_moves
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name
        self._rank = _rank
        self._faction = _faction

    def create_instance(self, level, entity_index):
        adversary = Adversary.Adversary(_level=level,
                                        _entity_name=self._entity_name,
                                        behaviors=self._behaviors,
                                        _max_moves=self._max_moves,
                                        _max_hp=self._max_hp,
                                        _senses=self._senses,
                                        _image_name=self._image_name,
                                        _rank=self._rank,
                                        _faction=self._faction)
        tools = self._create_tool_list(level, entity_index, adversary)
        adversary.init_tool_list(tools)
        return adversary