# Mostly cribbed from http://pymotw.com/2/json/

__author__ = 'Travis Moy'

import json


class JsonConverter(object):
    def simple_to_json(self, object):
        return json.dumps(object, default=object_to_dict)

    def simple_to_custom_object(self, json_string):
        return json_string.loads(json_string, object_hook=dict_to_object)


def object_to_dict(obj):
    d = {'__class__': obj.__class__.__name__,
         '__module__': obj.__module__}
    d.update(obj.__dict__)
    return d


def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items())
        inst = class_(**args)
    else:
        raise IOError("Cannot determine the class of the following dict: {0}".format(d))
    return inst