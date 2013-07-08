__author__ = 'Travis Moy'


class Faction(object):
    RELATION_FRIENDLY, RELATION_NEUTRAL, RELATION_HOSTILE = range(0, 3)

    def __init__(self, _name, _names_friendly_to=None, _names_neutral_to=None, _names_hostile_to=None):
        self._name = _name
        self._names_friendly_to = list()
        self._names_neutral_to = list()
        self._names_hostile_to = list()

        if _names_friendly_to is None:
            _names_friendly_to = list()
        if _names_neutral_to is None:
            _names_neutral_to = list()
        if _names_hostile_to is None:
            _names_hostile_to = list()

        for name in _names_friendly_to:
            self.add_faction_name(name, self.RELATION_FRIENDLY)
        for name in _names_neutral_to:
            self.add_faction_name(name, self.RELATION_NEUTRAL)
        for name in _names_hostile_to:
            self.add_faction_name(name, self.RELATION_HOSTILE)

    def get_faction_name(self):
        return self._name

    def is_friendly_to(self, faction_name):
        return faction_name in self._names_friendly_to

    def is_neutral_to(self, faction_name):
        return faction_name in self._names_neutral_to

    def is_hostile_to(self, faction_name):
        return faction_name in self._names_hostile_to

    # If the faction already exists, choose the more antagonistic relationship to keep.
    # For example, if the faction is friendly to Robots, and add_faction(Robots, HOSTILE) is added, it will register it
    # as hostile to Robots and remove the friendly relationship.
    # This will also spout off a warning.
    def add_faction_name(self, faction_name, relationship):
        # Brute Force as all hell, here.
        if relationship == self.RELATION_FRIENDLY:
            if faction_name not in self._names_friendly_to:
                self._names_friendly_to.append(faction_name)
        if relationship == self.RELATION_NEUTRAL:
            if faction_name in self._names_friendly_to:
                self._names_friendly_to.remove(faction_name)
            if faction_name not in self._names_neutral_to:
                self._names_neutral_to.append(faction_name)
        if relationship == self.RELATION_HOSTILE:
            if faction_name in self._names_friendly_to:
                self._names_friendly_to.remove(faction_name)
            if faction_name in self._names_neutral_to:
                self._names_neutral_to.remove(faction_name)
            if faction_name not in self._names_hostile_to:
                self._names_hostile_to.append(faction_name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        try:
            return self._name == other._name and sorted(self._names_friendly_to) == sorted(other._names_friendly_to) \
                       and sorted(self._names_hostile_to) == sorted(other._names_hostile_to) and \
                       sorted(self._names_neutral_to) == sorted(other._names_neutral_to)
        except AttributeError:
            return False


class Factions(object):
    DEFAULT = Faction('Default Faction')
    PLAYER = Faction('Player')
    ADVERSARY = Faction('Adversaries', _names_hostile_to=['Player'])
    CAVE_MONSTERS = Faction('Cave Monsters', _names_hostile_to=['Player', 'Robots'])
    ROBOTS = Faction('Robots', _names_friendly_to=['Engineers'], _names_hostile_to=['Player', 'Robots'])
    ENGINEERS = Faction('Engineers', _names_friendly_to=['Robots'], _names_hostile_to=['Cave Monsters'])
    TEST_0 = Faction('Test 0', _names_hostile_to=['Test 1', 'Player'])
    TEST_1 = Faction('Test 1', _names_hostile_to=['Test 0', 'Player'])

FACTIONS = Factions()