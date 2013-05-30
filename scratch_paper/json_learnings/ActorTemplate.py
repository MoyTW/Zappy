__author__ = 'Travis Moy'


class ActorTemplate(object):
    def __init__(self, _max_moves, _tools, _senses, _image_name):
        self._max_moves = _max_moves
        self._tools = _tools
        self._senses = _senses
        self._image_name = _image_name

    def __repr__(self):
        return "Moves: {0} Tools: {1} Senses: {2} Image: {3}".format(self._max_moves, self._tools, self._senses,
                                                                     self._image_name)