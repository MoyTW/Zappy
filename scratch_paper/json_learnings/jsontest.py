__author__ = 'Travis Moy'

import ActorTemplate
import json


def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        print 'MODULE:', module
        class_ = getattr(module, class_name)
        print 'CLASS:', class_
        # Slight issue - everything INSIDE the data structure is going to be in unicode.
        # Important? Unsure. But it's a thing to note.
        args = dict((key.encode('ascii'), value) for key, value in d.items())
        print 'INSTANCE ARGS:', args
        # Note that my habit of underscores in the class not being equivalent to the parameter inputs bites me here,
        # if I want to do it this way, because...well, it looks to match them.
        # Solution? UNDERSCORES ON INPUT PARAMETERS! hahaha I'm terrible.
        inst = class_(**args)
    else:
        inst = d
    return inst


def convert_to_builtin_type(obj):
    # Convert objects to a dictionary of their representation using __dict__
    # Adds in the name of the class and module
    # For my purposes module's probably not necessary, but all right, fair's fair
    # NEVER MIND I EAT MY WORDS
    d = {'__class__': obj.__class__.__name__,
         '__module__': obj.__module__}
    d.update(obj.__dict__)
    return d

template = ActorTemplate.ActorTemplate(_max_moves=2, _tools=['Manipulator'], _senses=['Seismic'],
                                       _image_name='No_Image.png')

print "Template: {0}".format(template)

json_string = json.dumps(template, default=convert_to_builtin_type)
print "Json of template: {0}".format(json_string)

loaded_template = json.loads(json_string, object_hook=dict_to_object)
print "Loaded json template: {0}".format(loaded_template)

print loaded_template._senses, loaded_template._senses[0]