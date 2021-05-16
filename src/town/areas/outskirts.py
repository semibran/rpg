from town.areas import Area
from town.actors.rogue import Rogue
from assets import load as use_assets
from sprite import Sprite
from config import ROGUE_NAME
from contexts.prompt import PromptContext, Choice

class OutskirtsArea(Area):
  TOWER_X = 224

  def __init__(area):
    super().__init__()
    rogue = Rogue(name=ROGUE_NAME, messages=[
      lambda town: (
        (ROGUE_NAME, "Yeah, baby!"),
        PromptContext(("I'm gettin' hard!\nSo hard for you, baby!"), (
          Choice("\"So true\""),
          Choice("\"....\"")
        ), on_close=lambda choice: (
          choice.text == "\"So true\"" and (
            (town.hero.core.name, "So true, bestie"),
            (ROGUE_NAME, "Oh baby, yes!"),
            (ROGUE_NAME, "Let's dance 'til the break of dawn!")
          ) or choice.text == "\"....\"" and (
            (town.hero.core.name, "...."),
            (town.ally.core.name, "Let's just leave him be...")
          )
        ))
      )
    ])
    rogue.x = 144
    rogue.facing = 1
    area.actors = [rogue]

  def render(area, hero):
    assets = use_assets()
    sprite_bg = assets.sprites["town_outskirts"]
    sprite_tower = assets.sprites["tower"]
    nodes = super().render(hero)
    nodes.insert(0, Sprite(
      image=sprite_bg,
      pos=(0, 0)
    ))
    nodes.append(Sprite(
      image=sprite_tower,
      pos=(OutskirtsArea.TOWER_X, Area.ACTOR_Y - 16)
    ))
    return nodes
