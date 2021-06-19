from math import sin, pi
from dataclasses import dataclass
from assets import load as use_assets
from filters import stroke, replace_color
from palette import BLACK, WHITE, GRAY, BLUE
from config import TILE_SIZE, WINDOW_WIDTH
from sprite import Sprite
from town.actors.npc import Npc

def can_talk(hero, actor):
  if (not isinstance(actor, Npc)
  or not actor.messages
  or actor.core.faction == "player"):
    return False
  dist_x = actor.x - hero.x
  facing_x, _ = hero.facing
  return abs(dist_x) < TILE_SIZE * 1.5 and dist_x * facing_x >= 0

def find_nearby_link(hero, links):
  for link in links.values():
    dist_x = link.x - hero.x
    _, direction_y = link.direction
    if abs(dist_x) < TILE_SIZE // 2 and direction_y:
      return link

ARROW_PERIOD = 45
ARROW_BOUNCE = 2

@dataclass
class AreaLink:
  x: int
  direction: tuple[int, int]

class Area:
  bg_id = None
  width = WINDOW_WIDTH
  ACTOR_Y = 128
  HORIZON_NORTH = -40
  TRANSIT_NORTH = -20
  HORIZON_SOUTH = 60
  TRANSIT_SOUTH = 30

  def __init__(area):
    area.actors = []
    area.camera = None
    area.draws = 0

  def init(area, town):
    assets = use_assets()
    area.width = assets.sprites[area.bg_id].get_width()

  def view(area, sprites, hero):
    assets = use_assets().sprites
    bg_image = assets[area.bg]
    area.width = bg_image.get_width()
    hero_x, _ = hero.pos
    bg_x = max(0, min(area.width - WINDOW_WIDTH, hero_x - WINDOW_WIDTH / 2))
    sprites.append(Sprite(
      image=bg_image,
      pos=(-bg_x, 0)
    ))
    return bg_x

  def render(area, hero, can_mark=True):
    nodes = []
    assets = use_assets()
    bg_image = assets.sprites[area.bg_id]
    area.width = bg_image.get_width()
    hero_x, _ = hero.pos
    bg_x = -hero_x + WINDOW_WIDTH / 2
    if bg_x > 0:
      bg_x = 0
    if bg_x < -area.width + WINDOW_WIDTH:
      bg_x = -area.width + WINDOW_WIDTH
    if area.camera == None:
      area.camera = bg_x
    else:
      area.camera += (bg_x - area.camera) / 4
    bg_x = area.camera
    nodes.append(Sprite(
      image=bg_image,
      pos=(bg_x, 0),
      layer="bg"
    ))
    arrowup_image = assets.sprites["link_north"]
    arrowdown_image = assets.sprites["link_south"]
    bubble_image = assets.sprites["bubble_talk"]
    actors = sorted(area.actors, key=lambda actor: actor.y + 1 if actor is hero else actor.y)
    for actor in actors:
      sprite = actor.render()
      offset_x, offset_y = sprite.pos
      x = actor.x - TILE_SIZE // 2 + offset_x
      y = actor.y + Area.ACTOR_Y - 1 + offset_y
      if hero and can_mark and can_talk(hero, actor):
        bubble_x = x + TILE_SIZE * 0.75 + 4
        bubble_y = y - TILE_SIZE * 0.25
        nodes.append(Sprite(
          image=bubble_image,
          pos=(bubble_x + bg_x, bubble_y),
          layer="markers"
        ))
      link = find_nearby_link(hero, area.links)
      if hero and can_mark and link:
        arrow_x = link.x - TILE_SIZE // 2
        arrow_y = Area.ACTOR_Y + TILE_SIZE * 1.25
        arrow_y += sin(area.draws % ARROW_PERIOD / ARROW_PERIOD * 2 * pi) * ARROW_BOUNCE
        arrow_image = arrowup_image if link.direction == (0, -1) else arrowdown_image
        arrow_image = replace_color(arrow_image, BLACK, BLUE)
        nodes.append(Sprite(
          image=arrow_image,
          pos=(arrow_x + bg_x, arrow_y),
          layer="markers"
        ))
      nodes.append(Sprite(
        image=stroke(sprite.image, GRAY if actor.indoors else WHITE),
        pos=(x + bg_x, y),
        flip=sprite.flip,
        layer="elems"
      ))
    area.draws += 1
    return nodes
