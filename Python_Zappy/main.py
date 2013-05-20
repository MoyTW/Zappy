__author__ = 'Travis Moy'

import pyglet


width = 1024
height = 768
window = pyglet.window.Window(width=width, height=height)

default_image_path = 'images/defaults/defaultcell.png'
image = pyglet.resource.image(default_image_path)

@window.event
def on_draw():
    sprite = pyglet.sprite.Sprite(image)
    sprite.set_position(width / 2, height / 2)
    sprite.draw()

pyglet.app.run()