__author__ = 'Travis Moy'


class Destructible(object):

    def __init__(self, *args, **kwargs):
        self._max_hp = kwargs.pop('_max_hp', None)
        if self._max_hp is None:
            raise AttributeError('Destructible had no max hp passed into it!')

        super(Destructible, self).__init__()

        self._current_hp = self._max_hp

    def get_max_hp(self):
        return self._max_hp

    def get_current_hp(self):
        return self._current_hp

    def deal_damage(self, _damage):
        self._current_hp -= _damage

    def is_destroyed(self):
        return self._current_hp <= 0