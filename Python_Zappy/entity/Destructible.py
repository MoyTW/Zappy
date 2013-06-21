__author__ = 'Travis Moy'


class Destructible(object):

    def __init__(self, _max_hp=10, *args, **kwargs):
        super(Destructible, self).__init__(*args, **kwargs)
        self._max_hp = _max_hp
        self._current_hp = _max_hp

    def get_max_hp(self):
        return self._max_hp

    def get_current_hp(self):
        return self._current_hp

    def deal_damage(self, _damage):
        self._current_hp -= _damage

    def is_destroyed(self):
        return self._current_hp <= 0