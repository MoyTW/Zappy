__author__ = 'Travis Moy'

import entity.Destructible as Destructible
import entity.Entity as Entity


class Environmental(Entity.Entity, Destructible.Destructible):
    PRIORITY = 1

    def __init__(self, _level, _entity_name='Default Envrionmental', _image_name=None, _max_hp=100, **kwargs):
        super(Environmental, self).__init__(_level=_level, _entity_name=_entity_name, _image_name=_image_name,
                                            _max_hp=_max_hp, **kwargs)

    # Should be overridden in each individual Environmental to add the actual functionality.
    def trigger(self):
        pass

    # Should be overridden in each individual Environmental to add the actual functionality.
    def destroy(self):
        print self.entity_name, 'was destroyed!'
        self._level.remove_entity_from(self, *self.get_coords())

    def __eq__(self, other):
        try:
            self_dict = self.__dict__.copy()
            self_dict.pop('_image')
            other_dict = other.__dict__.copy()
            other_dict.pop('_image')
            return self_dict == other_dict
        except (AttributeError, KeyError):
            return False