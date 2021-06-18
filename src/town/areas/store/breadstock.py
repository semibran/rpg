from town.topview.element import Element
from assets import load as use_assets
from sprite import Sprite

class BreadStock(Element):
  size = (32, 16)
  rect_offset = (-8, -8)

  def view(stock, sprites):
    stock_image = use_assets().sprites["store_breadstock"]
    stock_sprite = Sprite(
      image=stock_image,
      pos=stock.pos,
      origin=("center", "bottom"),
      layer="elems"
    )
    stock_sprite.move((8, 8))
    sprites.append(stock_sprite)