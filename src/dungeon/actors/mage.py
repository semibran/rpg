from random import randint, choice
import pygame
from dungeon.actors import DungeonActor
from cores.mage import Mage as MageCore
from assets import load as use_assets
from anims.move import MoveAnim
from anims.path import PathAnim
from anims.jump import JumpAnim
from anims.attack import AttackAnim
from anims.flinch import FlinchAnim
from anims.flicker import FlickerAnim
from anims.shake import ShakeAnim
from anims.drop import DropAnim
from anims.frame import FrameAnim
from sprite import Sprite
from skills.magic.glacio import Glacio
from skills.magic.congelatio import Congelatio
from skills.magic.accerso import Accerso
from skills.weapon.broadsword import BroadSword

class Mage(DungeonActor):
  drops = [BroadSword]

  class CastAnim(FrameAnim):
    def __init__(anim, *args, **kwargs):
      super().__init__(
        frames=use_assets().sprites["mage_cast"],
        frame_duration=10,
        *args, **kwargs
      )

  def __init__(mage, core=None, on_kill=None, *args, **kwargs):
    super().__init__(core=core or MageCore(skills=[Glacio, Accerso], *args, **kwargs))
    mage.on_kill = on_kill
    mage.chant_skill = None
    mage.chant_dest = None
    mage.chant_turns = 0

  def chant(mage, skill, dest=None):
    mage.chant_skill = skill
    mage.chant_dest = dest
    mage.chant_turns = skill.chant_turns
    mage.core.anims.append(Mage.CastAnim())

  def cast_spell(mage):
    if mage.chant_skill is None:
      return None
    command = ("use_skill", mage.chant_skill, mage.chant_dest)
    mage.chant_skill = None
    mage.chant_dest = None
    mage.chant_turns = 0
    mage.core.anims = []
    return command

  def step(mage, game):
    enemy = game.find_closest_enemy(mage)
    if enemy is None:
      return None

    if mage.chant_turns:
      mage.chant_turns -= 1
      if mage.chant_turns == 0:
        return mage.cast_spell()
      else:
        return None

    mage_x, mage_y = mage.cell
    enemy_x, enemy_y = enemy.cell
    dist_x = enemy_x - mage_x
    delta_x = dist_x // (abs(dist_x) or 1)
    dist_y = enemy_y - mage_y
    delta_y = dist_y // (abs(dist_y) or 1)

    mage.face(enemy.cell)
    if (delta_x == 0 and dist_y <= Glacio.range_max
    or delta_y == 0 and dist_x <= Glacio.range_max
    ) and not enemy.ailment == "freeze" and not abs(dist_x) + abs(dist_y) == 1:
      if mage.get_hp() < mage.get_hp_max() / 2:
        mage.chant(skill=Congelatio, dest=enemy.cell)
      else:
        mage.chant(skill=Glacio)
      return game.log.print((mage.token(), " is chanting."))

    has_allies = next((e for e in [game.floor.get_elem_at(c, superclass=DungeonActor) for c in game.room.get_cells()] if (
      e and e is not mage
      and e.get_faction() == mage.get_faction()
    )), None)

    if not has_allies:
      return ("use_skill", Accerso)

    delta = None
    if abs(dist_x) + abs(dist_y) == 1:
      if game.floor.is_cell_empty((mage_x - delta_x, mage_y - delta_y)):
        delta = (-delta_x, -delta_y)
      else:
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        deltas = [(dx, dy) for (dx, dy) in deltas if game.floor.is_cell_empty((mage_x + dx, mage_y + dy))]
        if deltas:
          delta = choice(deltas)
    elif abs(dist_x) + abs(dist_y) < 4:
      if delta_x and delta_y:
        delta = randint(0, 1) and (-delta_x, 0) or (0, -delta_y)
      elif delta_x:
        delta = (-delta_x, 0)
      elif delta_y:
        delta = (0, -delta_y)
    else:
      if delta_x and delta_y:
        delta = randint(0, 1) and (delta_x, 0) or (0, delta_y)
      elif delta_x:
        delta = (delta_x, 0)
      elif delta_y:
        delta = (0, delta_y)
    if delta:
      return ("move", delta)

  def view(mage, anims):
    sprites = use_assets().sprites
    anim_group = [a for a in anims[0] if a.target is mage] if anims else []
    for anim in anim_group:
      if type(anim) is MoveAnim or type(anim) is PathAnim:
        x4_idx = max(0, int((anim.time - 1) % anim.period // (anim.period / 4)))
        if mage.facing == (0, -1):
          sprite = [
            sprites["mage_up"],
            sprites["mage_walkup0"],
            sprites["mage_up"],
            sprites["mage_walkup1"]
          ][x4_idx]
          break
        elif mage.facing == (0, 1):
          sprite = [
            sprites["mage_down"],
            sprites["mage_walkdown0"],
            sprites["mage_down"],
            sprites["mage_walkdown1"]
          ][x4_idx]
          break
        elif anim.time % (anim.period // 2) >= anim.period // 4:
          sprite = sprites["mage_walk"]
          break
      elif type(anim) is JumpAnim:
        if mage.facing == (0, -1):
          sprite = sprites["mage_walkup"]
        elif mage.facing == (0, 1):
          sprite = sprites["mage_walkdown"]
        else:
          sprite = sprites["mage_walk"]
        break
      elif (type(anim) is AttackAnim
      and anim.time < anim.duration // 2):
        if mage.facing == (0, -1):
          sprite = sprites["mage_walkup"]
        elif mage.facing == (0, 1):
          sprite = sprites["mage_walkdown"]
        else:
          sprite = sprites["mage_walk"]
        break
      elif type(anim) in (FlinchAnim, FlickerAnim, DropAnim):
        sprite = sprites["mage_flinch"]
        break
      elif type(anim) is ShakeAnim:
        sprite = sprites["mage_shock"]
        break
    else:
      if mage.facing == (0, -1):
        sprite = sprites["mage_up"]
      elif mage.facing == (0, 1):
        sprite = sprites["mage_down"]
      else:
        sprite = sprites["mage"]
    return super().view(sprite, anims)
