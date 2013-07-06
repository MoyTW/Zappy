__author__ = 'Travis Moy'

from loader.templates.TemplateActor import TemplateActor
from loader.templates.TemplateTool import TemplateTool
from loader.templates.TemplateAdversary import TemplateAdversary
from z_json import JSONCONVERTER
from entity.actor.senses import *
from entity.actor.behaviors import *
from z_defs import RANK
from entity.actor.Faction import FACTIONS
from loader.templates.TemplateCell import TemplateCell
from loader.templates.TemplateEnvironmental import TemplateEnvironmental


def convert_and_write_to_file(object, filename):
    json_string = JSONCONVERTER.simple_to_json(object)
    f = open(filename, 'w')
    f.write(json_string)
    f.close()

#####=====----- Entities -----=====#####

zappy_basic_template = TemplateActor(_senses=[SenseSight.SenseSight(9)],
                                     _tools=[TemplateTool('manipulator',
                                                          _image_name='tools/waldo.png',
                                                          _entity_name='Manipulator',
                                                          _range=1,
                                                          _cooldown=0,
                                                          _energy_cost=1),
                                             TemplateTool('sampling_laser',
                                                          _image_name='tools/sampling_laser.png',
                                                          _entity_name='Sampling Laser',
                                                          _range=99),
                                             TemplateTool('holoprojector',
                                                          _image_name='tools/holoprojector.png',
                                                          _entity_name='Holoprojector',
                                                          _range=99),
                                             TemplateTool('zap_gun',
                                                          _image_name='tools/zap_gun.png',
                                                          _entity_name='Zap Gun',
                                                          _range=99,
                                                          _cooldown=0,
                                                          _energy_cost=5)],
                                     _max_hp=10,
                                     _image_name='boxydrone.png',
                                     _faction=FACTIONS.PLAYER,
                                     _base_threat=3)
convert_and_write_to_file(zappy_basic_template, 'entities/zappy/ZappyBasic.json')

stupid_seismic_enemy = TemplateAdversary(_entity_name='StupidSeismic',
                                         _image_name='fire_breathing_snake.png',
                                         _behaviors=[BehaviorAttackRanged.BehaviorAttackRanged(_strength=1, _range=3),
                                                     BehaviorMoveStupid.BehaviorMoveStupid(),
                                                     BehaviorAttackMelee.BehaviorAttackMelee(_strength=2)],
                                         _max_moves=1,
                                         _senses=[SenseSeismic.SenseSeismic(9)],
                                         _rank=RANK.WEAK)
convert_and_write_to_file(stupid_seismic_enemy, 'entities/adversaries/FastStupidSeismic.json')

stupid_sight_enemy = TemplateAdversary(_entity_name='StupidSight',
                                       _image_name='biting_snake.png',
                                       _behaviors=[BehaviorMoveStupid.BehaviorMoveStupid(),
                                                   BehaviorAttackMelee.BehaviorAttackMelee(_strength=1)],
                                       _max_moves=2,
                                       _senses=[SenseSight.SenseSight(9)],
                                       _rank=RANK.WEAK)
convert_and_write_to_file(stupid_sight_enemy, 'entities/adversaries/FastStupidSight.json')

stupid_sight_enemy_test = TemplateAdversary(_entity_name='StupidSightTest',
                                            _image_name='biting_snake.png',
                                            _behaviors=[BehaviorMoveStupid.BehaviorMoveStupid(),
                                                        BehaviorAttackMelee.BehaviorAttackMelee(_strength=1)],
                                            _max_moves=2,
                                            _senses=[SenseSight.SenseSight(9)],
                                            _rank=RANK.WEAK)
convert_and_write_to_file(stupid_sight_enemy_test, 'entities/adversaries/FastStupidSightTest.json')

zap_gun_tool = TemplateTool('zap_gun', _entity_name='Floor Gun')
convert_and_write_to_file(zap_gun_tool, 'entities/tools/ZapGunTool.json')

#####=====----- Environmentals -----=====#####
unstable_floor = TemplateEnvironmental(_env_class='collapsible', _entity_name='Unstable Floor', _max_hp=25)
convert_and_write_to_file(unstable_floor, 'entities/environmentals/UnstableFloor.json')

reinforced_door_env = TemplateEnvironmental(_env_class='door', _entity_name='Reinforced Door', _max_hp=99999,
                                            _is_open=False, _open_image_location='vault_door_open.png',
                                            _closed_image_location='vault_door_closed.png')
convert_and_write_to_file(reinforced_door_env, 'entities/environmentals/ReinforcedDoor.json')

weak_door_env = TemplateEnvironmental(_env_class='door', _entity_name='Weak Door', _max_hp=1,
                                      _is_open=False, _open_image_location='vault_door_open.png',
                                      _closed_image_location='vault_door_closed.png')
convert_and_write_to_file(weak_door_env, 'entities/environmentals/WeakDoor.json')

#####=====----- Cells -----=====#####

floor = TemplateCell(_image_location='images/cells/floor.png', _passable=True, _transparent=True)
convert_and_write_to_file(floor, 'cells/floor.json')

unstable_floor_cell = TemplateCell(_image_location='images/cells/floor.png', _passable=True, _transparent=True,
                                   _entity_files=['environmentals/UnstableFloor.json'])
convert_and_write_to_file(unstable_floor_cell, 'cells/unstable_floor.json')

wall = TemplateCell(_image_location='images/cells/wall.png', _passable=False, _transparent=False)
convert_and_write_to_file(wall, 'cells/wall.json')

drone = TemplateCell(_image_location='images/cells/floor.png', _passable=True, _transparent=True,
                     _entity_files=['zappy/ZappyBasic.json'])
convert_and_write_to_file(drone, 'cells/drone.json')

pit = TemplateCell(_image_location='images/cells/pit.png', _passable=False, _transparent=True)
convert_and_write_to_file(pit, 'cells/pit.json')

reinforced_door_cell = TemplateCell(_image_location='images/cells/floor.png', _passable=False, _transparent=False,
                                    _entity_files=['environmentals/ReinforcedDoor.json'])
convert_and_write_to_file(reinforced_door_cell, 'cells/reinforced_door.json')

weak_door_cell = TemplateCell(_image_location='images/cells/floor.png', _passable=False, _transparent=False,
                              _entity_files=['environmentals/WeakDoor.json'])
convert_and_write_to_file(weak_door_cell, 'cells/weak_door.json')