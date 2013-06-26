__author__ = 'Travis Moy'

import Template
import entity.environmentals.Environmental as Environmental
import entity.environmentals.EnvCollapsible as EnvCollapsible
import warnings


ENV_NAMES_DICT = {
    'environmental': Environmental.Environmental,
    'collapsible': EnvCollapsible.EnvCollapsible

}


class TemplateEnvironmental(Template.Template):

    def __init__(self, _env_class='environmental', _entity_name='Unnamed Envrionmental Template', _image_name=None,
                 _max_hp=1, **kwargs):
        self._env_class = _env_class
        self._entity_name = _entity_name
        self._image_name = _image_name
        self._max_hp = _max_hp
        self._extra_args = kwargs

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
        return _env_class(_level=level,
                          _entity_name=self._entity_name,
                          _image_name=self._image_name,
                          _map_hp=self._max_hp,
                          **self._extra_args)