# Mostly cribbed from http://pymotw.com/2/json/

__author__ = 'Travis Moy'

import json


class JsonConverterException(Exception):
    pass


class JsonConverter(object):
    def simple_to_json(self, object):
        try:
            obj_func = object.to_json
            return json.dumps(object, default=obj_func, sort_keys=True, indent=4)
        except AttributeError:
            return json.dumps(object, default=object_to_dict, sort_keys=True, indent=4)

    def simple_to_custom_object(self, json_string):
        return json.loads(json_string, object_hook=dict_to_object)

JSONCONVERTER = JsonConverter()


def object_to_dict(obj):
    d = {'__class__': obj.__class__.__name__,
         '__module__': obj.__module__}
    d.update(obj.__dict__)
    return d


def recursive_unicode_conversion(value):
    if type(value) == list:
        for i in range(len(value)):
            value[i] = recursive_unicode_conversion(value[i])
    elif type(value) == dict:
        for k, v in value.items():
            value.pop(k, v)
            value[k.encode('ascii')] = recursive_unicode_conversion(v)
            pass
    elif type(value) == unicode:
        return value.encode('ascii')
    return value


def dict_to_object(d):
    if '__class__' in d:
        try:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name, fromlist=[class_name])
            class_ = getattr(module, class_name)

            args = dict()
            for key, value in d.items():
                args[key.encode('ascii')] = recursive_unicode_conversion(value)

            inst = class_(**args)
        except Exception as e:
            raise JsonConverterException(e.message)
    else:
        raise JsonConverterException("Cannot determine the class of the following dict: {0}".format(d))
    return inst