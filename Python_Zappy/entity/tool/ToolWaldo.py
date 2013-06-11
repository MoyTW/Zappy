__author__ = 'Travis Moy'

import Tool


# What does a waldo do?
# It targets the following:
#   Environmentals (doors, traps, etc, etc)
#       -attempts to call the "trigger" function of the Environmental in question
#   Gettables (note: not necessarily the final class name) (Upgrades, Pickups, Consumables)
#       -attempts to call the "can pick up" function of the Gettable in question
#           -attempts to call the "apply to user" function (Upgrades == Pickups?)
#           -attempts to call the "store in inventory" function (Consumables)
class ToolWaldo(Tool.Tool):
    pass