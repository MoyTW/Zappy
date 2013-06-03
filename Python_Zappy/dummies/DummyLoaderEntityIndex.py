__author__ = 'Travis Moy'

import warnings


class DummyLoaderEntityIndex(object):
    def create_entity_by_name(self, name, level):
        if name == 'TestObj':
            return 'TestStringEntity'
        else:
            pass