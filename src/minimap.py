import pygame
from pygame import Surface, Rect, PixelArray
from stage import Stage
from actors.knight import Knight
from actors.mage import Mage
from actors.eye import Eye
from actors.chest import Chest

MARGIN_X = 8
MARGIN_Y = 6
SCALE = 2

class Minimap:
  def __init__(minimap, size):
    minimap.size = size

  def render(minimap, ctx):
    sprite_width, sprite_height = minimap.size
    scaled_size = (sprite_width * SCALE, sprite_height * SCALE)
    surface = Surface(scaled_size)
    surface.set_colorkey(0xFF00FF)
    surface.fill(0xFF00FF)
    temp_surface = Surface((sprite_width, sprite_height))
    temp_surface.set_colorkey(0xFF00FF)
    temp_surface.fill(0xFF00FF)
    pixels = PixelArray(temp_surface)

    hero = ctx.hero
    hero_x, hero_y = hero.cell
    floor = ctx.floor
    visible_cells = hero.visible_cells
    visited_cells = next((cells for floor, cells in ctx.memory if floor is ctx.floor), None)
    for cell in visited_cells:
      tile = ctx.floor.get_tile_at(cell)
      actor = ctx.floor.get_actor_at(cell)
      color = None
      if type(actor) is Knight or type(actor) is Mage and cell in visible_cells:
        color = 0x7F7FFF
      elif actor and actor.faction == "enemy" and cell in visible_cells:
        if actor.asleep:
          color = 0x7F007F
        else:
          color = 0xFF0000
      elif type(actor) is Chest:
        if cell in visible_cells:
          color = 0xFFFF00
        else:
          color = 0x7F7F00
      elif tile is Stage.WALL or tile is Stage.DOOR_HIDDEN or tile is Stage.DOOR_LOCKED:
        if cell in visible_cells:
          color = 0xFFFFFF
        else:
          color = 0x7F7F7F
      elif tile is Stage.DOOR:
        if cell in visible_cells:
          color = 0x00FFFF
        else:
          color = 0x007F7F
      elif tile is Stage.STAIRS_UP:
        if cell in visible_cells:
          color = 0x00FF00
        else:
          color = 0x007F00
      elif tile is Stage.STAIRS_DOWN:
        if cell in visible_cells:
          color = 0x00FF00
        else:
          color = 0x007F00
      else:
        color = 0x000000
      x, y = cell
      x = x - hero_x + sprite_width // 2
      y = y - hero_y + sprite_height // 2
      if x >= 0 and y >= 0 and x < sprite_width and y < sprite_height:
        pixels[x, y] = color
    pixels.close()
    surface.blit(pygame.transform.scale(temp_surface, scaled_size), (0, 0))
    return surface

  def draw(minimap, surface, ctx):
    window_width = surface.get_width()
    window_height = surface.get_height()
    sprite = minimap.render(ctx)
    surface.blit(sprite, (
      window_width - sprite.get_width() - MARGIN_X,
      MARGIN_Y
    ))