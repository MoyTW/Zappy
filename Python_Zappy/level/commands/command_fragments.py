__author__ = 'Travis Moy'

import warnings
import Command as cmd


##########==========----------IMEPLEMENTED----------==========##########

class LevelPlaceAndAssignEntityID(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, new_entity, x, y):
        """
        :type new_entity: entity.Entity.Entity
        :type x: int
        :type y: int
        """
        warnings.warn("LevelPlaceAndAssignEntityID.execute() is not yet implemented!")
        desc = "A new {0} has appeared at ({1}, {2})!".format(new_entity.entity_name, x, y)
        super(LevelPlaceAndAssignEntityID, self).__init__(desc)

        self.new_entity = new_entity
        self.x = x
        self.y = y

    def execute(self, lvl):
        """:type lvl: level.Level.Level"""
        if lvl.place_entity_at(self.new_entity, self.x, self.y):
            self.new_entity.eid = lvl.max_eid
            lvl.max_eid += 1
        else:
            warnings.warn("Cannot place entity {0} at ({1}, {2})!".format(self.new_entity, self.x, self.y))


class EnvironmentalTrigger(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        """
        warnings.warn("EnvironmentalTrigger.execute() is not yet implemented!")
        desc = "{0} has been triggered!".format(lvl_view.ent_name(eid))
        super(EnvironmentalTrigger, self).__init__(desc)

        self.eid = eid

    def execute(self, lvl):
        """:type lvl: level.Level.Level"""
        env = lvl.get_entity_by_id(self.eid)
        """:type: entity.environmentals.Environmental.Environmental"""
        try:
            env.trigger()
        except AttributeError:
            warnings.warn("Entity {0} is not an Environmental! Cannot execute EnvironmentalTrigger!".format(env))


class ActorApplyStatusEffect(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, target_eid, lvl_view, effect, duration, *args, **kwargs):
        """
        :type target_eid: int
        :type lvl_view: level.LevelView.LevelView
        :type effect: entity.actor.effects.Effect
        """
        warnings.warn("ActorApplyStatusEffect.execute() is not yet implemented!")
        desc = "{0} has been afflicted with {1}!".format(lvl_view.ent_name(target_eid), effect.EFFECT_NAME)
        super(ActorApplyStatusEffect, self).__init__(desc)

        self.target_eid = target_eid
        self.effect = effect
        self.duration = duration
        self.args = args
        self.kwargs = kwargs

    def execute(self, lvl):
        """:type lvl: level.Level.Level"""
        actor = lvl.get_entity_by_id(self.target_eid)
        """:type: entity.actor.Actor.Actor"""
        effect = self.effect(_duration=self.duration, _target=lvl.get_entity_by_id(self.target_eid),
                             *self.args, **self.kwargs)
        try:
            actor.apply_status_effect(effect)
        except AttributeError:
            warnings.warn("Entity {0} is not an Actor! Cannot execute ActorApplyStatusEffect!".format(actor))


class EntityDealDamage(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view, damage):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        :type damage: int
        """
        warnings.warn("EntityDealDamage.execute() is not yet implemented!")
        desc = "{0} has taken {1} damage!".format(lvl_view.ent_name(eid), damage)
        super(EntityDealDamage, self).__init__(desc)

        self.eid = eid
        self.damage = damage

    def execute(self, lvl):
        """:type lvl: level.Level.Level"""
        destructible = lvl.get_entity_by_id(self.eid)
        """:type: entity.Destructible.Destructible"""
        try:
            destructible.deal_damage(self.damage)
        except AttributeError:
            warnings.warn("Entity {0} is not Destructible! Cannot execute EntityDealDamage!".format(destructible))


class EntityUseMoves(cmd.Command):
    wordiness = cmd.PRINT_VERBOSE

    def __init__(self, eid, lvl_view, cost):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        :type cost: int
        """
        desc = "{0} has spent {1} moves!".format(lvl_view.ent_name(eid), cost)
        super(EntityUseMoves, self).__init__(desc)

        self.eid = eid
        self.cost = cost

    def execute(self, lvl):
        """:type lvl: level.Level.Level"""
        actor = lvl.get_entity_by_id(self.eid)
        """:type: entity.actor.Actor.Actor"""
        try:
            actor.use_moves(self.cost)
        except AttributeError:
            warnings.warn("Entity {0} is an Entity, not an Actor! Cannot execute EntityUseMoves!".format(actor))


class LevelMoveEntity(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view, origin_x, origin_y, target_x, target_y):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        :type origin_x: int
        :type origin_y: int
        :type target_x: int
        :type target_y: int
        """
        desc = "{0} has moved from ({1}, {2}) to ({3}, {4})!".format(lvl_view.ent_name(eid), origin_x, origin_y,
                                                                     target_x, target_y)
        super(LevelMoveEntity, self).__init__(desc)

        self.eid = eid
        self.origin = (origin_x, origin_y)
        self.target = (target_x, target_y)
        self.ori_to_tar = self.origin + self.target

    def execute(self, lvl):
        """:type lvl: level.Level.Level"""
        lvl.move_entity_from_to(lvl.get_entity_by_id(self.eid), *self.ori_to_tar)


class LevelRemoveEntity(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, eid, lvl_view):
        """
        :type eid: int
        :type lvl_view: level.LevelView.LevelView
        """
        desc = "{0} has been removed from the level!".format(lvl_view.ent_name(eid))
        super(LevelRemoveEntity, self).__init__(desc)

        self.eid = eid

    def execute(self, lvl):
        """:type lvl: level.Level.Level"""
        print "Attempting to remove", self.eid
        removed = lvl.remove_entity(self.eid)
        print "Removed:", removed


# An example of a fragment
class CellSetPassable(cmd.Command):
    wordiness = cmd.PRINT_NORMAL

    def __init__(self, is_passable, x, y):
        """
        :type is_passable: bool
        :type x: int
        :type y: int
        """
        if is_passable:
            description = "({0}, {1}) is now passable!".format(x, y)
        else:
            description = "({0}, {1}) is now impassable!".format(x, y)
        super(CellSetPassable, self).__init__(description)

        self.is_passable = is_passable
        self.x = x
        self.y = y

    def execute(self, lvl):
        """:type lvl: level.Level.Level"""
        lvl.set_passable(self.x, self.y, self.is_passable)