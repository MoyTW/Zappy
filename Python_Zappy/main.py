__author__ = 'Travis Moy'

import pyglet
from zappyui.UIScreens.UIScreenMenuBase import UIScreenMenuBase
from zappyui.UIController import UIController

#width = 1920
#height = 1080
width = 640 * 2
height = 480 * 2
window = pyglet.window.Window(width=width, height=height)
print width, height


class Viewport(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

menu = UIScreenMenuBase(Viewport(width, height))
uicontrol = UIController(window, menu)

'''
@window.event
def on_draw():
    window.clear()
    menu.draw()
'''

pyglet.app.run()