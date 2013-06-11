__author__ = 'Travis Moy'

import Tool


# How does the holoprojector work?
# We will need to change how the targeting works for the Adversaries.
#   First off, they can't just look for the player. They have to look for objects not aligned to themselves. That means
# adding in a faction-style system.
#   Secondly, they have to be able to evaluate targets over other targets. That is, have a method for choosing targets
# in a deterministic (sp?) manner. That would be something like a "targeting priority" embedded in Actor objects, or
# a "threat" counter that can go up and down based on actions.
#   The way the holoprojector would work would be to create a new Actor with a higher priority than Zappy, thereby
# distracting the enemies.
class ToolHoloprojector(Tool.Tool):
    pass
