__author__ = 'Travis Moy'

import warnings
import level.Level
import LoaderEntityIndex
import os


class LoaderLevel(object):
    def __init__(self, levels_folder='levels'):
        self._levels_path = self._find_levels_path(levels_folder)

        self._entity_index = LoaderEntityIndex.LoaderEntityIndex()
        self._levels = dict()

    def get_level_info(self, level_number):
        level = self._levels.get(level_number)
        if level is None:
            return None
        return level.get_level_info()

    def get_level(self, level_number):
        if self._levels.get(level_number) is None:
            self._load_level(level_number)
        return self._levels.get(level_number)

    # For every level in the folder, load the level info (Name, number, how large it is, whatever else I later add).
    def load_all_levels_infos(self):
        level_files = os.listdir(self._levels_path)
        for file in level_files:
            if file.endswith(".lvl"):
                self._load_level_info(file)

    def _load_level_info(self, filename):
        file = open(os.path.join(self._levels_path, filename), 'r')
        lines = file.readlines()
        info = level.LevelInfo.LevelInfo(name=self._read_line_value(lines[0]),
                                         number=self._read_line_value(lines[1]),
                                         width=self._read_line_value(lines[2]),
                                         height=self._read_line_value(lines[3]))
        self._levels[info.get_number()] = level.Level.Level(info)

    def _read_line_value(self, line):
        pair = line.split(',')
        if pair[0] == '!NAME!':
            return pair[1].strip()
        else:
            return int(pair[1].strip())

    # Normally levels are loaded by number - the file name should be the number.
    def _load_level(self, level_number):
        pass

    def _find_levels_path(self, levels_folder):
        return os.path.join(os.path.dirname(__file__), "..", levels_folder)