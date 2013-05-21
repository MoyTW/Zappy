# Query: Is Python doing something weird again with the default parameters if you call a function in the initializer to,
# you know, initialize? It's not like, running it once at the very start and then storing the result?

# Response: Yes, it is running it once at the start and storing the results, I thought we went over this last time.
# Shame on you for not remembering!

import random


def TEST_FUNC():
    return random.randint(0, 100000)


class TestClass(object):
    def __init__(self, test_input=TEST_FUNC()):
        self._input = test_input


tc0 = TestClass()
tc1 = TestClass()
tc2 = TestClass()
print tc0._input, tc1._input, tc2._input, TEST_FUNC()