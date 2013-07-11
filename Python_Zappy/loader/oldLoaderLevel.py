__author__ = 'Travis Moy'

import os
import warnings

import pyglet

import level.Level
import level.Cell
import level.LevelController
import LoaderEntityIndex
import oldLoaderCellDefinition


class oldLoaderLevel(object):
    def __init__(self, levels_folder='levels'):
        self._levels_folder = levels_folder
        self._levels_path = self._find_levels_path(levels_folder)
        self._preview_loader = pyglet.resource.Loader(script_home="{0}/preview_images".format(self._levels_path))

        self._entity_index = LoaderEntityIndex.LoaderEntityIndex()
        self._levels = dict()
        self._default_preview = self._return_default_preview()

        self._load_all_levels_infos()

    def get_num_levels(self):
        return len(self._levels)

    def get_level_info(self, level_number):
        level = self._levels.get(level_number)
        if level is None:
            return None
        return level.get_level_info()

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
            return level.LevelController.LevelController(temp_level)
        else:
            warnings.warn("LoaderLevel.get_level_controller is returning None!")
            return None

    def _return_default_preview(self):
        resource_loader = pyglet.resource.Loader('@assets')
        return resource_loader.image('images/defaults/default_preview.png')

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
        number = self._read_line_value(lines[1])
        info = level.LevelInfo.LevelInfo(_name=self._read_line_value(lines[0]), _number=number,
                                         _width=self._read_line_value(lines[2]),
                                         _height=self._read_line_value(lines[3]),
                                         _previews_folder=self._levels_folder)
        self._levels[info.info_number] = level.Level.Level(info)

    def _return_level_preview(self, level_number):
        path = "{0}.png".format(level_number)

        try:
            return self._preview_loader.image(path)
        except pyglet.resource.ResourceNotFoundException as e:
            warnstr = "There is no preview available for level {0}".format(level_number)
            warnings.warn(warnstr, RuntimeWarning)
            return self._default_preview

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
            cell_dict[line_fragments[0]] = oldLoaderCellDefinition.oldLoaderCellDefinition(image_location=line_fragments[2],
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
    def _build_cell_map_and_assign_to_level(self, cell_defs_dict, lines, index_begin_map, _level):
        cells = [[None for _ in range(0, _level.level_height)] for _ in range(0, _level.level_width)]
        _level.replace_cells(cells)

        for row_index in range(index_begin_map + 1, len(lines)):
            line = lines[row_index].strip()
            cols = line.split(',')
            for col in range(0, _level.level_width):
                x = col
                y = len(lines) - 1 - row_index
                cell_def = cell_defs_dict[cols[col]]
                self._build_cell_from_def_and_add_entities(x, y, cell_def, _level)

    # If it encounters an entity which is player controlled, sets the level.player_actor to that entity
    def _build_cell_from_def_and_add_entities(self, x, y, cell_def, _level):
        passable = cell_def.passable == 'True'
        _level._cells[x][y] = level.Cell.Cell(_image_location=cell_def.image_location, _passable=passable,
                                              _transparent=passable)
        if cell_def.entity_strings is not None:
            for entity_string in cell_def.entity_strings:
                entity = self._entity_index.create_entity_by_name(entity_string, _level)
                try:
                    if entity.is_player_controlled():
                        _level.player_actor = entity
                except AttributeError:
                    pass
                _level.place_entity_at(entity, x, y)

    # No unit test.
    def _find_levels_path(self, levels_folder):
        path = os.path.split(os.path.dirname(__file__))[0]
        return os.path.join(path, levels_folder)