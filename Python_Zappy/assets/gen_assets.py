__author__ = 'Travis Moy'

from loader.TemplateActor import TemplateActor
from z_json import JSONCONVERTER


def convert_and_write_to_file(object, filename):
    json_string = JSONCONVERTER.simple_to_json(object)
    f = open(filename, 'w')
    f.write(json_string)
    f.close()

zappy_basic_template = TemplateActor(_max_moves=1, _image_name='boxydrone.png', _player_controlled=True)
convert_and_write_to_file(zappy_basic_template, 'entities/zappy/ZappyBasic.json')