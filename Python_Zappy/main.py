__author__ = 'Travis Moy'

import pyglet
from zappyui.UIController import UIController
from zappyui.FactoryScreens import FactoryScreens
from loader.LoaderLevel import LoaderLevel

width = 1920
height = 1080

#width = 1280
#height = 1024

#width = 640
#height = 480
#height = 530

window = pyglet.window.Window(width=width, height=height)

loader_level = LoaderLevel()
factory = FactoryScreens(window, loader_level)

uicontrol = UIController(window, factory.create_ScreenMenuBase())

pyglet.app.run()