__author__ = 'Travis Moy'

from entity.actor.senses import *
from loader.TemplateActor import TemplateActor
from loader.TemplateAdversary import TemplateAdversary
from z_json import JSONCONVERTER
from entity.actor.behaviors import *


def convert_and_write_to_file(object, filename):
    json_string = JSONCONVERTER.simple_to_json(object)
    f = open(filename, 'w')
    f.write(json_string)
    f.close()

zappy_basic_template = TemplateActor(_senses=[SenseSight.SenseSight(9)], _image_name='boxydrone.png',
                                     _player_controlled=True)
convert_and_write_to_file(zappy_basic_template, 'entities/zappy/ZappyBasic.json')

stupid_seismic_enemy = TemplateAdversary(_behaviors=[BehaviorMoveStupid.BehaviorMoveStupid(),
                                                     BehaviorAttackMelee.BehaviorAttackMelee(_strength=2)],
                                         _max_moves=2,
                                         _senses=[SenseSeismic.SenseSeismic(9)])
convert_and_write_to_file(stupid_seismic_enemy, 'entities/adversaries/FastStupidSeismic.json')

stupid_sight_enemy = TemplateAdversary(_behaviors=[BehaviorMoveStupid.BehaviorMoveStupid(),
                                                   BehaviorAttackMelee.BehaviorAttackMelee(_strength=2)],
                                       _max_moves=2,
                                       _senses=[SenseSeismic.SenseSeismic(9)])
convert_and_write_to_file(stupid_sight_enemy, 'entities/adversaries/FastStupidSight.json')