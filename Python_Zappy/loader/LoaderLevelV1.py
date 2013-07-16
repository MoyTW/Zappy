__author__ = 'Travis Moy'

import warnings
import os

import pyglet

import level.LevelController as LevelController
import level.Level as Level
from z_json import JSONCONVERTER
import loader.LoaderEntityIndex as LoaderEntityIndex


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
        if level_number in self._levels:
            return self._levels[level_number].get_level_info()
        return None

    def get_level(self, level_number):
        try:  # Okay what's this try/except block for? Oh! If it's None - and therefore not a valid level.
            if self._levels.get(level_number).cells_are_none():
                self._load_level(level_number)
        except AttributeError:
            warnings.warn('{0} is not a valid level number!'.format(level_number))
        return self._levels.get(level_number)

    def regen_level(self, level_number):
        try:
            self._load_level(level_number)
        except AttributeError:
            warnings.warn('{0} is not a valid level number!'.format(level_number))

    def get_level_controller(self, level_number):
        temp_level = self.get_level(level_number)
        if temp_level is not None:
            return LevelController.LevelController(temp_level)
        else:
            warnings.warn("LoaderLevel.get_level_controller is returning None!")
            return None

    # For each level, call _load_level_info
    def _load_all_levels_infos(self):
        level_files = os.listdir(self._levels_path)
        for file in level_files:
            if file.endswith(".lvlV1"):
                warnings.warn("LoaderLevelV1 will load all files ending with .lvlV1 into info!")
                self._load_level_info(file)

    def _read_until_blank(self, _file):
        line = _file.readline()
        text = ''
        while line != '\n' and line != '':
            if not (line[0] == '#' and line[1] == '-'):
                text += line
            line = _file.readline()
        return text

    # You can just grab this from the json
    def _load_level_info(self, _filename):
        f = open(os.path.join(self._levels_path, _filename), 'r')

        info_json = self._read_until_blank(f)

        info = JSONCONVERTER.simple_to_custom_object(info_json)
        self._levels[info.info_number] = Level.Level(info)

        f.close()

    # This loads the rest of the level (the cells, entities)
    def _load_level(self, _level_number):
        target_level = self._levels.get(_level_number)

        f = open(os.path.join(self._levels_path, (str(_level_number) + ".lvlV1")), 'r')
        self._read_until_blank(f)  # This is to remove the info section
        cell_defs = self._read_until_blank(f)
        map_layout = self._read_until_blank(f)
        ent_list = self._read_until_blank(f)
        f.close()

        templates = self._load_return_cell_templates(cell_defs)
        self._load_level_cells(templates, map_layout, target_level)
        self._load_entity_list(ent_list, target_level)
        self._find_and_assign_player_actor(target_level)

    # Takes the json of the dict, and loads the templates into a dict mapping to characters, returns
    def _load_return_cell_templates(self, _json):
        templates = JSONCONVERTER.load_simple(_json)
        keys = templates.keys()
        for key in keys:
            file_location = templates[key]
            text = self.CELL_LOADER.text("{0}{1}".format(self.PATH_TO_CELL_TEMPLATES, file_location))
            templates[key] = JSONCONVERTER.simple_to_custom_object(text.text)
        return templates

    # This is where the actual cells for the level are built by calls to the Template
    def _load_level_cells(self, _templates, _layout_string, _level):
        width = _level.level_width
        height = _level.level_height
        _level.replace_cells([[None for _ in range(0, height)] for _ in range(0, width)])

        i = 0
        x = 0
        y = height - 1
        while y >= 0:
            while x < width:
                _templates[_layout_string[i]].create_instance(_level, self._entity_index, _x=x, _y=y)
                i += 1
                while i < len(_layout_string) and (_layout_string[i] == ' ' or _layout_string[i] == '\n'):
                    i += 1
                x += 1
            x = 0
            y -= 1

    # Creates, places, and calls setup functions of the entities in question
    def _load_entity_list(self, _json, _level):
        entity_list = JSONCONVERTER.load_simple(_json)
        self._entity_index.lvl = _level

        for entry in entity_list:
            entity = self._entity_index.create_entity_by_name(entry['_entity'], _level.view)
            if '_orders' in entry:
                for order in entry['_orders']:
                    self._execute_entity_order(order, entity, _level)

    def _find_and_assign_player_actor(self, _level):
        entities = _level.view.get_all_entities()
        for entity in entities:
            try:
                if entity.is_player_controlled():
                    _level.player_actor = entity
            except AttributeError:
                pass

    def _execute_entity_order(self, _order, _entity, _level):
        if _order['_order'] == 'place':
            _level.place_entity_at(_entity, x=_order['_x'], y=_order['_y'])

    def _find_levels_path(self, _levels_folder):
        path = os.path.split(os.path.dirname(__file__))[0]
        return os.path.join(path, _levels_folder)