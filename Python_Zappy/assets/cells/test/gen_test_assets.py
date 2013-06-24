__author__ = 'Travis Moy'

from z_json import JSONCONVERTER
from loader.templates.TemplateCell import TemplateCell


def convert_and_write_to_file(object, filename):
    json_string = JSONCONVERTER.simple_to_json(object)
    f = open(filename, 'w')
    f.write(json_string)
    f.close()

floor = TemplateCell(_image_location='images/floor.png', _passable=True, _transparent=True)
convert_and_write_to_file(floor, 'floor.json')

wall = TemplateCell(_image_location='images/wall.png', _passable=False, _transparent=True)
convert_and_write_to_file(wall, 'wall.json')

drone = TemplateCell(_image_location='images/floor.png', _passable=True, _transparent=True,
                     _entity_files=['zappy/ZappyBasic.json'])
convert_and_write_to_file(drone, 'drone.json')