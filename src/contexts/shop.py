from math import sin, cos, pi
import pygame
from pygame import Rect
from pygame.transform import rotate, scale
from contexts import Context
from contexts.cardgroup import CardContext
from contexts.sell import SellContext
from cores.knight import KnightCore
from comps.control import Control
from comps.textbox import Textbox
from comps.card import Card
from hud import Hud
from assets import load as use_assets
from filters import replace_color, darken
from palette import BLACK, WHITE, RED, BLUE, GOLD
import keyboard
from anims import Anim
from anims.tween import TweenAnim
from easing.expo import ease_out
from easing.circ import ease_out as ease_out_circ
from lib.lerp import lerp
from portraits.mira import MiraPortrait

class CursorAnim(Anim): blocking = False
class BackgroundEnterAnim(TweenAnim): blocking = True
class PortraitEnterAnim(TweenAnim): blocking = True

class ShopContext(Context):
  def __init__(ctx, items):
    super().__init__()
    ctx.items = items
    ctx.hero = KnightCore()
    ctx.portraits = [MiraPortrait()]
    ctx.hud = Hud()
    ctx.anims = [CursorAnim()]
    ctx.textbox = Textbox((100, 72))
    ctx.controls = [
      Control(key=("X"), value="Menu")
    ]
    ctx.open(CardContext(pos=(16, 144), on_choose=ctx.handle_choose))

  def init(ctx):
    ctx.textbox.print("MIRA: What can I do you for?")

  def enter(ctx):
    ctx.anims += [
      BackgroundEnterAnim(duration=15),
      PortraitEnterAnim(duration=20, delay=10)
    ]

  def handle_choose(ctx, card):
    if card.name == "buy": return
    if card.name == "sell": ctx.handle_sell(card)
    if card.name == "exit": return

  def handle_sell(ctx, card):
    ctx.open(SellContext(
      items=ctx.items,
      card=card
    ))

  def update(ctx):
    super().update()
    # ctx.hand_index += (ctx.card_index - ctx.hand_index) / 4
    for anim in ctx.anims:
      if anim.done:
        ctx.anims.remove(anim)
      else:
        anim.update()

  def draw(ctx, surface):
    assets = use_assets()
    surface.fill(WHITE)
    pygame.draw.rect(surface, BLACK, Rect(0, 0, 256, 224))

    bg_image = assets.sprites["fortune_bg"]
    bg_anim = next((a for a in ctx.anims if type(a) is BackgroundEnterAnim), None)
    if bg_anim:
      t = ease_out(bg_anim.pos)
      bg_width = bg_image.get_width()
      bg_height = int(bg_image.get_height() * t)
      bg_image = scale(bg_image, (bg_width, bg_height))
    surface.blit(bg_image, (0, 128 / 2 - bg_image.get_height() / 2))

    for portrait in ctx.portraits:
      portrait_image = portrait.render()
      portrait_x = surface.get_width() - portrait_image.get_width()
      portrait_y = 0
      portrait_anim = next((a for a in ctx.anims if type(a) is PortraitEnterAnim), None)
      if portrait_anim:
        t = ease_out_circ(portrait_anim.pos)
        portrait_x = lerp(surface.get_width(), portrait_x, t)
      surface.blit(portrait_image, (portrait_x, portrait_y))

    MARGIN = 2

    bubble_image = assets.sprites["bubble_shop"]
    surface.blit(bubble_image, (0, 0))
    surface.blit(ctx.textbox.render(), (13, 26))

    hud_image = ctx.hud.update(ctx.hero)
    hud_x = MARGIN
    hud_y = surface.get_height() - hud_image.get_height() - MARGIN
    surface.blit(hud_image, (hud_x, hud_y))

    gold_image = assets.sprites["item_gold"]
    gold_image = replace_color(gold_image, BLACK, GOLD)
    gold_x = hud_x + hud_image.get_width() + 2
    gold_y = hud_y + hud_image.get_height() - gold_image.get_height() - 2
    surface.blit(gold_image, (gold_x, gold_y))

    goldtext_font = assets.ttf["roman"]
    goldtext_image = goldtext_font.render("500")
    goldtext_x = gold_x + gold_image.get_width() + 3
    goldtext_y = gold_y + gold_image.get_height() // 2 - goldtext_image.get_height() // 2
    surface.blit(goldtext_image, (goldtext_x, goldtext_y))

    if type(ctx.child) is CardContext:
      title_image = assets.ttf["english_large"].render("Fortune House")
      title_x = surface.get_width() - title_image.get_width() - 8
      title_y = surface.get_height() - title_image.get_height() - 7
      surface.blit(title_image, (title_x, title_y))

      subtitle_image = assets.ttf["roman"].render("Destiny written in starlight")
      subtitle_x = title_x + title_image.get_width() - subtitle_image.get_width()
      subtitle_y = title_y - title_image.get_height() + 2
      surface.blit(subtitle_image, (subtitle_x, subtitle_y))

    if type(ctx.child) is CardContext:
      sprites = ctx.child.view()
      for sprite in sprites:
        sprite.draw(surface)
    elif ctx.child:
      ctx.child.draw(surface)

    # hand_anim = next((a for a in ctx.anims if type(a) is CursorAnim), None)
    # hand_image = assets.sprites["hand"]
    # hand_image = rotate(hand_image, -90)
    # hand_x = cards_x
    # hand_x -= hand_image.get_width() // 2
    # hand_x += (32 + 2) * ctx.hand_index
    # hand_y = cards_y
    # hand_y += 48 // 2
    # hand_y += sin(hand_anim.time % 30 / 30 * 2 * pi) * 2
    # surface.blit(hand_image, (hand_x, hand_y))

    # controls_x = surface.get_width() - 8
    # controls_y = surface.get_height() - 12
    # for control in ctx.controls:
    #   control_image = control.render()
    #   control_x = controls_x - control_image.get_width()
    #   control_y = controls_y - control_image.get_height() // 2
    #   surface.blit(control_image, (control_x, control_y))
    #   controls_x = control_x - 8
