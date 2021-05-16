from town.actors.npc import Npc
from cores.rogue import RogueCore
from sprite import Sprite
from assets import load as use_assets
from filters import replace_color
from palette import BLACK, GREEN

class Rogue(Npc):
  def __init__(rogue, name=None, messages=None):
    super().__init__(RogueCore(name), messages)
    rogue.draws = 0

  def render(rogue):
    sprites = use_assets().sprites
    image = (rogue.draws % 15 < 8
      and sprites["rogue"]
      or sprites["rogue_walk"])
    image = replace_color(image, BLACK, GREEN)
    rogue.sprite = Sprite(image=image)
    rogue.draws += 1
    return super().render()
