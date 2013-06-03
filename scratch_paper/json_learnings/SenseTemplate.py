__author__ = 'Travis Moy'


class SenseTemplate(object):
    def __init__(self, _name, _range):
        self._name = _name
        self._range = _range

    def test_func(self):
        print "SenseTemplate.test_func() called!"

    def __repr__(self):
        return "Name: {0}, Range: {1}".format(self._name, self._range)