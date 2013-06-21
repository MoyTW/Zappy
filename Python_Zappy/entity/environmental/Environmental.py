__author__ = 'Travis Moy'

import entity.Destructible as Destructible
import entity.Entity as Entity


class Environmental(Entity.Entity, Destructible.Destructible):
    _priority = 1

    def __init__(self, _level, _entity_name='Default Envrionmental', _image_name=None, _max_hp=100, *args, **kwargs):
        super(Environmental, self).__init__(_level=_level, _entity_name=_entity_name, _image_name=_image_name,
                                            _max_hp=_max_hp, *args, **kwargs)

    # Should be overridden in each individual Environmental to add the actual functionality.
    def trigger(self):
        pass

    # Should be overridden in each individual Environmental to add the actual functionality.
    def destroy(self):
        print self._entity_name, 'was destroyed!'
        self._level.remove_entity_from(self, *self.get_coords())