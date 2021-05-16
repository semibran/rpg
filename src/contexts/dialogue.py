from math import pi, sin
import pygame
from pygame import Rect
import config
import keyboard
from contexts import Context
from assets import load as use_assets
from comps.log import Log
from hud import Hud
from palette import BLACK
from anims.tween import TweenAnim
from easing.expo import ease_out
# from comps.previews import Previews
# from comps.minimap import Minimap
# from comps.spmeter import SpMeter
# from comps.floorno import FloorNo

class EnterAnim(TweenAnim): pass
class ExitAnim(TweenAnim): pass

class DialogueContext(Context):
  effects = [Hud] # , Previews, Minimap, SpMeter, FloorNo]
  BAR_HEIGHT = 24
  BAR_ENTER_DURATION = 15
  BAR_EXIT_DURATION = 7

  def __init__(ctx, script, on_close=None):
    super().__init__(on_close=on_close)
    ctx.script = list(script)
    ctx.index = 0
    ctx.name = None
    ctx.log = Log(autohide=False)
    ctx.enter()

  def enter(ctx):
    ctx.anim = EnterAnim(duration=ctx.BAR_ENTER_DURATION, on_end=ctx.print)

  def exit(ctx):
    ctx.anim = ExitAnim(duration=ctx.BAR_EXIT_DURATION, on_end=ctx.close)
    ctx.log.exit()

  def print(ctx, item=None):
    if item is None:
      item = ctx.script[min(len(ctx.script) - 1, ctx.index)]
    if callable(item):
      item = item()
    if isinstance(item, Context):
      ctx.name = None
      ctx.log.exit()
      return ctx.open(item, on_close=lambda next: (
        ctx.script.extend(next),
        ctx.handle_next()
      ))
    ctx.log.clear()
    if type(item) is tuple:
      name, page = item
    else:
      name, page = None, item
    if callable(page):
      page = page()
    if name and name != ctx.name:
      ctx.name = name
      ctx.log.print((name.upper(), ": ", page))
    else:
      ctx.log.print(page)

  def handle_keydown(ctx, key):
    if ctx.child:
      return ctx.child.handle_keydown(key)
    if keyboard.get_pressed(key) != 1:
      return
    if key in (pygame.K_SPACE, pygame.K_RETURN):
      ctx.handle_next()

  def handle_next(ctx):
    if not ctx.log.clean:
      return ctx.log.skip()
    ctx.index += 1
    if ctx.index == len(ctx.script):
      return ctx.exit()
    if not ctx.script[ctx.index]:
      return ctx.handle_next()
    ctx.print()

  def draw(ctx, surface):
    assets = use_assets()
    sprite_arrow = assets.sprites["arrow_dialogue"]

    bar_height = ctx.BAR_HEIGHT
    if ctx.anim:
      anim = ctx.anim
      if anim.done:
        ctx.anim = None
      anim.update()
      t = anim.pos
      if type(anim) is EnterAnim:
        t = ease_out(t)
      elif type(anim) is ExitAnim:
        t = 1 - t
      bar_height *= t
    pygame.draw.rect(surface, BLACK, Rect(0, 0, surface.get_width(), bar_height))
    pygame.draw.rect(surface, BLACK, Rect(0, surface.get_height() - bar_height + 1, surface.get_width(), bar_height))

    ctx.log.update()
    sprite = ctx.log.box
    if sprite:
      x = config.WINDOW_WIDTH // 2 - sprite.get_width() // 2
      y = surface.get_height() - ctx.log.y
      surface.blit(sprite, (x, y))
      if ctx.log.clean:
        t = ctx.log.clean % 30 / 30
        offset = sin(t * 2 * pi) * 1.25
        x += -sprite_arrow.get_width() + sprite.get_width() - Log.PADDING_X - 8
        y += -sprite_arrow.get_height() + sprite.get_height() - Log.PADDING_Y + 4 + offset
        surface.blit(sprite_arrow, (x, y))

    super().draw(surface)
