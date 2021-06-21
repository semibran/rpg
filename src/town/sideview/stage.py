from math import sin, pi
from dataclasses import dataclass
from assets import load as use_assets
from filters import stroke, replace_color, darken
from palette import BLACK, WHITE, GRAY, BLUE
from config import TILE_SIZE, WINDOW_WIDTH
from sprite import Sprite

@dataclass
class AreaLink:
  x: int
  direction: tuple[int, int]

class Area:
  ACTOR_Y = 136
  NPC_Y = 120
  DOOR_Y = 116
  HORIZON_NORTH = -40
  TRANSIT_NORTH = -20
  HORIZON_SOUTH = 60
  TRANSIT_SOUTH = 30
  width = WINDOW_WIDTH
  bg = None

  def __init__(area):
    area.actors = []
    area.camera = None
    area.draws = 0

  def init(area, ctx):
    pass

  def spawn(area, actor, pos):
    area.actors.append(actor)
    actor.pos = pos

  def view(area, hero, link):
    sprites = []
    assets = use_assets().sprites
    bg_image = assets[area.bg]
    hero_x, _ = hero.pos
    area.width = bg_image.get_width()
    area.camera = min(0, max(-area.width + WINDOW_WIDTH, -hero_x + WINDOW_WIDTH / 2))
    sprites.append(Sprite(
      image=bg_image,
      pos=(area.camera, 0)
    ))
    if link:
      link_name = next((link_name for link_name, l in area.links.items() if l is link), None)
    else:
      link_name = None
    for actor in sorted(area.actors, key=lambda actor: 1 if actor is hero else 0):
      for sprite in actor.view():
        y = Area.ACTOR_Y if actor.get_faction() == "player" else Area.NPC_Y
        sprite.move((area.camera, y))
        sprite.target = actor
        _, sprite_y = sprite.pos
        if actor is hero and link_name and link_name.startswith("door") and sprite_y < Area.DOOR_Y:
          sprite.image = darken(sprite.image)
        sprites.append(sprite)
    if link_name and link_name.startswith("door"):
      link_pos = (link.x + area.camera, 96)
      sprites += [
        Sprite(
          image=assets["door_open"],
          pos=link_pos,
          origin=("center", "top"),
          layer="tiles"
        ),
        Sprite(
          image=assets["roof"],
          pos=link_pos,
          origin=("center", "bottom"),
          layer="fg"
        )
      ]
    sprites.sort(key=lambda sprite: sprite.depth(["bg", "tiles", "elems", "fg", "markers"]))
    return sprites
