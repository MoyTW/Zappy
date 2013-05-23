__author__ = 'Travis Moy'

import pyglet


#width = 1920
#height = 1080
width = 640 * 2
height = 480 * 2
window = pyglet.window.Window(width=width, height=height)
print width, height

pyglet.app.run()