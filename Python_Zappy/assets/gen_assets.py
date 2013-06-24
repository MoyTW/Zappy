__author__ = 'Travis Moy'

from loader.templates.TemplateActor import TemplateActor
from loader.templates.TemplateTool import TemplateTool
from loader.templates.TemplateAdversary import TemplateAdversary
from z_json import JSONCONVERTER
from entity.actor.senses import *
from entity.actor.behaviors import *
from z_defs import RANK
from entity.actor.Faction import FACTIONS
from level.LevelInfo import LevelInfo


def convert_and_write_to_file(object, filename):
    json_string = JSONCONVERTER.simple_to_json(object)
    f = open(filename, 'w')
    f.write(json_string)
    f.close()

zappy_basic_template = TemplateActor(_senses=[SenseSight.SenseSight(9)],
                                     _tools=[TemplateTool('zap_gun', _entity_name='Zap Gun', _range=99, _cooldown=0,
                                                          _energy_cost=5),
                                             TemplateTool('holoprojector', _entity_name='Holoprojector', _range=99),
                                             TemplateTool('doom_gun', _entity_name='Doom Gun', _range=99, _cooldown=1,
                                                          _energy_cost=1)],
                                     _max_hp=10,
                                     _image_name='boxydrone.png',
                                     _faction=FACTIONS.PLAYER,
                                     _base_threat=3)
convert_and_write_to_file(zappy_basic_template, 'entities/zappy/ZappyBasic.json')

stupid_seismic_enemy = TemplateAdversary(_entity_name='StupidSeismic',
                                         _behaviors=[BehaviorAttackRanged.BehaviorAttackRanged(_strength=1, _range=3),
                                                     BehaviorMoveStupid.BehaviorMoveStupid(),
                                                     BehaviorAttackMelee.BehaviorAttackMelee(_strength=2)],
                                         _max_moves=1,
                                         _senses=[SenseSeismic.SenseSeismic(9)],
                                         _rank=RANK.WEAK)
convert_and_write_to_file(stupid_seismic_enemy, 'entities/adversaries/FastStupidSeismic.json')

stupid_sight_enemy = TemplateAdversary(_entity_name='StupidSight',
                                       _behaviors=[BehaviorMoveStupid.BehaviorMoveStupid(),
                                                   BehaviorAttackMelee.BehaviorAttackMelee(_strength=2)],
                                       _max_moves=2,
                                       _senses=[SenseSeismic.SenseSeismic(9)],
                                       _rank=RANK.WEAK)
convert_and_write_to_file(stupid_sight_enemy, 'entities/adversaries/FastStupidSight.json')

zap_gun_tool = TemplateTool('zap_gun', _entity_name='Floor Gun')
convert_and_write_to_file(zap_gun_tool, 'entities/tools/ZapGunTool.json')

linfo = LevelInfo(_name='TestInfo', _number=0, _width=5, _height=5, _levels_folder='')
linfo_json = JSONCONVERTER.simple_to_json(linfo)
print linfo_json