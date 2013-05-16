__author__ = 'Travis Moy'

import level.Level
import LoaderEntityIndex
import os
import LoaderCellDefinition


class LoaderLevel(object):
    def __init__(self, levels_folder='levels'):
        self._levels_path = self._find_levels_path(levels_folder)

        self._entity_index = LoaderEntityIndex.LoaderEntityIndex()
        self._levels = dict()

        self._load_all_levels_infos()

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
    # Should this be called in the constructor?
    def _load_all_levels_infos(self):
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

    def _load_level(self, level_number):
        level = self._levels.get(level_number)

        filepath = os.path.join(self._levels_path, (str(level_number) + ".lvl"))
        file = open(filepath, 'r')
        lines = file.readlines()

        # Is there a more elegant way to do this? PROBABLY. Searching for the indicated indices in the lines list.
        index_begin_definitions = [i for i, x in enumerate(lines) if x.strip() == '!DEFINITIONS!'][0]
        index_begin_map = [i for i, x in enumerate(lines) if x.strip() == '!MAP!'][0]

        cell_defs_dict = self._build_cell_defs_dict(lines, index_begin_definitions)
        self._build_cell_map_and_assign_to_level(cell_defs_dict, lines, index_begin_map, level)

    # No unit test (under _load_level).
    def _build_cell_defs_dict(self, lines, index_begin_definitions):
        current_index = index_begin_definitions + 1
        cell_dict = dict()

        # For each Cell Def
        while lines[current_index] != '\n':
            entity_strings = None

            line_fragments = lines[current_index].split(',')

            # If you have objects assigned to the cell, create a list for entity_string
            if line_fragments[3].strip() != '[]':
                entity_strings = line_fragments[3:len(line_fragments)]
                for i in range(0, len(entity_strings)):
                    entity_strings[i] = entity_strings[i].strip().strip('[]')

            # Add the cell def to the dict
            cell_dict[line_fragments[0]] = LoaderCellDefinition.LoaderCellDefinition(image_location=line_fragments[2],
                                                                                     passable=line_fragments[1],
                                                                                     entity_strings=entity_strings)
            current_index += 1

        return cell_dict

    # No unit test (under _load_level).
    # Returns a populated two-dimensional list.
    # First, set up a dummy list of Nones.
    # Assign the dummy list of Nones to the Level object in question.
    # Iterate through the lines, adding cells as instructed by cell_defs_dict.
    # If entities, use Level.place_entity_at(), using self._entity_index to create them.
    def _build_cell_map_and_assign_to_level(self, cell_defs_dict, lines, index_begin_map, level):
        cells = [[None for _ in range(0, level.get_height())] for _ in range(0, level.get_width())]
        level.set_cells(cells)

        for row_index in range(index_begin_map + 1, len(lines)):
            line = lines[row_index].strip()
            cols = line.split(',')
            for col in range(0, level.get_width()):
                # ...I have no idea what I was doing with my other project.
                x = col
                y = row_index - index_begin_map - 1 # going from the top - wait, why did this work in my other project?
                cell_def = cell_defs_dict[cols[col]]
                self._build_cell_from_def_and_add_entities(x, y, cell_def, level)
                # Ok I should stop and figure out how it worked.

    def _build_cell_from_def_and_add_entities(self, x, y, cell_def, level):
        pass

    # No unit test.
    def _find_levels_path(self, levels_folder):
        return os.path.join(os.path.dirname(__file__), "..", levels_folder)