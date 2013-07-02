__author__ = 'Travis Moy'


class Destructible(object):

    def __init__(self, _max_hp=1, **kwargs):
        self.max_hp = _max_hp
        if self.max_hp is None:
            raise AttributeError('Destructible had no max hp passed into it!')

        super(Destructible, self).__init__(**kwargs)

        self._current_hp = self.max_hp

    @property
    def current_hp(self):
        return self._current_hp

    # Override this in the child classes
    def destroy(self):
        pass

    def deal_damage(self, _damage):
        self._current_hp -= _damage

    def is_destroyed(self):
        return self._current_hp <= 0