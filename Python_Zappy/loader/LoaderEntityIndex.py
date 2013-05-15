__author__ = 'Travis Moy'

import warnings


class LoaderEntityIndex(object):
    def __init__(self):
        pass

    # THIS IS HARDCODED FOR TESTING PURPOSES
    # When you ACTUALLY WRITE THIS FUNCTION, move the TestObj into the ACTUAL INDEX!
    def create_entity_by_name(self, name):
        if name == 'TestObj':
            return 'TestStringEntity'
        else:
            pass

    def _load_entity_by_name(self, name):
        pass