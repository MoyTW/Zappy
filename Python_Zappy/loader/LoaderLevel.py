__author__ = 'Travis Moy'

import warnings
import level.Level
import LoaderEntityIndex


class LoaderLevel(object):
    LEVEL_DIR = '\levels'

    def __init__(self):
        self.entity_index = LoaderEntityIndex()
        self.levels = dict()

    def get_level_info(self, level_number):
        pass

    def get_level(self, level_number):
        pass

    # For every level in the folder, load the level info (Name, number, how large it is, whatever else I later add).
    def load_all_levels_infos(self):
        pass

    # Normally levels are loaded by number - the file name should be the number.
    def _load_level(self, level_number):
        pass

    # Usage of this function is discouraged.
    def _load_level_by_file(self, file):
        pass