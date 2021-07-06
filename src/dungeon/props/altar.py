from dungeon.element import DungeonElement
from assets import load as use_assets
from filters import replace_color
from palette import WHITE, GOLD
from sprite import Sprite

class Altar(DungeonElement):
  def view(altar, anims):
    return super().view(Sprite(
      image=replace_color(use_assets().sprites["altar"], WHITE, GOLD),
      layer="elems"
    ), anims)
