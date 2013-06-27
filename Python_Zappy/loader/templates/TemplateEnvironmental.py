__author__ = 'Travis Moy'

import Template
import entity.environmentals.Environmental as Environmental
import entity.environmentals.EnvCollapsible as EnvCollapsible
import entity.environmentals.EnvDoor as EnvDoor
import warnings


ENV_NAMES_DICT = {
    'environmental': Environmental.Environmental,
    'collapsible': EnvCollapsible.EnvCollapsible,
    'door': EnvDoor.EnvDoor
}


class TemplateEnvironmental(Template.Template):

    def __init__(self, _env_class='environmental', _entity_name=None, _image_name=None, _max_hp=None, **kwargs):
        self._env_class = _env_class
        self._kwargs = kwargs
        if _entity_name is not None:
            self._kwargs['_entity_name'] = _entity_name
        if _image_name is not None:
            self._kwargs['_image_name'] = _image_name
        if _max_hp is not None:
            self._kwargs['_max_hp'] = _max_hp

    def create_instance(self, level, entity_index, user=None):
        _env_class = None
        try:
            _env_class = ENV_NAMES_DICT[self._env_class]
        except KeyError:
            warnings.warn('Cannot create environmental! '
                          '{0} is not a recognized environmental keyword! '
                          'Valid keywords are: {1}'.format(self._env_class,
                                                           ENV_NAMES_DICT.keys()))

        if _env_class is None:
            warnings.warn("RETURNING NONE FROM TempalteTool.create_instance()")
            return None
        print self._kwargs, self._env_class
        return _env_class(_level=level,
                          **self._kwargs['_kwargs'])