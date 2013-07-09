__author__ = 'Travis Moy'

import entity.environmentals.Environmental as Environmental


# The unstable floor will collapse when destroyed, killing everything above it and leaving an impassable tile.
class EnvCollapsible(Environmental.Environmental):
    PIT_IMAGE_PATH = 'images/cells/pit.png'

    def __init__(self, _eid, _level, _entity_name='Collapsible', _image_name=None, _max_hp=5, _damage=50, **kwargs):
        super(EnvCollapsible, self).__init__(_eid=_eid, _level=_level, _entity_name=_entity_name,
                                             _image_name=_image_name, _max_hp=_max_hp, **kwargs)
        self._damage = _damage

    def trigger(self):
        self._collapse()

    def destroy(self):
        self._collapse()

    def _collapse(self):
        print self.entity_name, 'has collapsed, leaving a pit in its wake! All entities on tile take', self._damage,\
            "damage!"
        cell = self._level.get_cell_at(*self.get_coords())
        cell.is_passable = False
        cell.is_transparent = True
        entities = cell.get_all_entities()
        for entity in entities:
            try:
                entity.deal_damage(self._damage)
            except AttributeError:
                print entity, "is immune to collapse damage!"
        cell.change_cell_image_by_location(self.PIT_IMAGE_PATH)
        self._level.remove_entity_from(self, *self.get_coords())