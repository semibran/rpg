from dataclasses import dataclass
from pygame import Surface
from pygame.transform import flip, scale

@dataclass
class Sprite:
  image: Surface = None
  pos: tuple[int, int] = (0, 0)
  size: tuple[int, int] = None
  flip: tuple[bool, bool] = (False, False)
  origin: tuple[str, str] = ("top", "left")
  offset: int = 0
  layer: str = None

  def copy(sprite):
    return Sprite(
      image=sprite.image,
      pos=sprite.pos,
      size=sprite.size,
      flip=sprite.flip,
      origin=sprite.origin,
      offset=sprite.offset,
      layer=sprite.layer
    )

  def draw(sprite, surface, offset=(0, 0), origin=None):
    image = sprite.image
    flip_x, flip_y = sprite.flip
    if flip_x or flip_y:
      image = flip(image, flip_x, flip_y)
    if sprite.size:
      width, height = sprite.size
      scaled_image = scale(image, (int(width), int(height)))
    else:
      scaled_image = image

    x, y = sprite.pos

    origin_x, origin_y = sprite.origin
    if origin_x == "center":
      x -= scaled_image.get_width() // 2
    if origin_y == "center":
      y -= scaled_image.get_height() // 2
    if origin_y == "bottom":
      y -= scaled_image.get_height()

    if origin:
      origin_x, origin_y = origin
      if origin_x == "left":
        x += image.get_width() // 2
      if origin_y == "top":
        y += image.get_height() // 2
      elif origin_y == "bottom":
        y -= image.get_height() // 2

    offset_x, offset_y = offset
    surface.blit(scaled_image, (x + offset_x, y + offset_y))

  def depth(sprite, layers):
    _, y = sprite.pos
    try:
      depth = layers.index(sprite.layer)
    except ValueError:
      depth = 0
    return depth * 1000 + y + sprite.image.get_height() + sprite.offset
