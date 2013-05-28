__author__ = 'Travis Moy'

import pyglet
from zappyui.UIController import UIController
from zappyui.FactoryScreens import FactoryScreens
from loader.LoaderLevel import LoaderLevel

width = 1920
height = 1080
#width = 640 * 2
#height = 480 * 2

window = pyglet.window.Window(width=width, height=height)

level_loader = LoaderLevel()
factory = FactoryScreens(window)

uicontrol = UIController(window, factory.create_ScreenMenuBase())

pyglet.app.run()