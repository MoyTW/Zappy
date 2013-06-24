__author__ = 'Travis Moy'

import level.Level as Level
from z_json import JSONCONVERTER
import loader.LoaderEntityIndex as LoaderEntityIndex
import os
import pyglet


class LoaderLevelV1(object):
    PATH_TO_CELL_TEMPLATES = 'cells/'
    CELL_LOADER = pyglet.resource.Loader('@assets')

    def __init__(self, levels_folder='levels'):
        self._levels_folder = levels_folder
        self._levels_path = self._find_levels_path(levels_folder)

        self._entity_index = LoaderEntityIndex.LoaderEntityIndex()
        self._levels = dict()

        self._load_all_levels_infos()

    def get_num_levels(self):
        return len(self._levels)

    def get_level_info(self, level_number):
        pass

    def get_level(self, level_number):
        pass

    def regen_level(self, level_number):
        pass

    def get_level_controller(self, level_number):
        pass

    # For each level, call _load_level_info
    def _load_all_levels_infos(self):
        level_files = os.listdir(self._levels_path)
        for file in level_files:
            if file.endswith(".lvlV1"):
                self._load_level_info(file)

    # You can just grab this from the json
    def _load_level_info(self, filename):
        file = open(os.path.join(self._levels_path, filename), 'r')

        line = file.readline()
        info_json = ''
        while line != '\n':
            info_json += line  # Is this an efficient way? Am I creating a zillion tiny strings and tossing them away?
            # Just a thing to note, in case I have to come back and look for ways to speed it up.
            line = file.readline()

        info = JSONCONVERTER.simple_to_custom_object(info_json)
        self._levels[info.get_number()] = Level.Level(info)

    # This loads the rest of the level (the cells, entities)
    def _load_level(self, level_number):
        pass

    # Takes the json of the dict, and loads the templates into a dict mapping to characters, returns
    def _load_return_cell_templates(self, json):
        templates = JSONCONVERTER.load_simple(json)
        keys = templates.keys()
        for key in keys:
            file_location = templates[key]
            text = self.CELL_LOADER.text("{0}{1}".format(self.PATH_TO_CELL_TEMPLATES, file_location))
            templates[key] = JSONCONVERTER.simple_to_custom_object(text.text)
        return templates

    # This is where the actual cells for the level are built by calls to the Template
    def _load_level_cells(self):
        pass

    # Creates, places, and calls setup functions of the entities in question
    def _load_entity_list(self):
        pass

    def _find_levels_path(self, levels_folder):
        path = os.path.split(os.path.dirname(__file__))[0]
        return os.path.join(path, levels_folder)