__author__ = 'Travis Moy'

from z_json import JSONCONVERTER
import loader.LoaderEntityIndex as LoaderEntityIndex
import os


class LoaderLevelV1(object):
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
        pass

    # This loads the rest of the level (the cells, entities)
    def _load_level(self, level_number):
        pass

    def _load_cell_templates(self):
        pass

    # This is where the actual cells for the level are built by calls to the Template
    def _load_level_cells(self):
        pass

    # Creates, places, and calls setup functions of the entities in question
    def _load_entity_list(self):
        pass

    def _find_levels_path(self, levels_folder):
        path = os.path.split(os.path.dirname(__file__))[0]
        return os.path.join(path, levels_folder)