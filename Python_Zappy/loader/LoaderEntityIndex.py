__author__ = 'Travis Moy'

import warnings


class LoaderEntityIndex(object):
    def __init__(self):
        pass

    def create_entity_by_name(self, name):
        if name == 'TestObj':
            return 'TestStringEntity'
        else:
            pass

    def _load_entity_by_name(self, name):
        pass