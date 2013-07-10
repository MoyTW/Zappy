__author__ = 'Travis Moy'

import warnings


class Template(object):
    def create_instance(self, eid, level, entity_index):
        warnings.warn('Template.create_instance has been called! This should not happen!')