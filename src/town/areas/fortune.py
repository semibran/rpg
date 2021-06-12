from town.topview.stage import Stage, Link
from town.topview.actor import Actor
from town.topview.fortunedesk import FortuneDesk
from contexts.prompt import PromptContext, Choice
from contexts.shop import ShopContext
from cores.mage import MageCore
from cores.rogue import RogueCore
from savedata.resolve import resolve_item
from palette import ORANGE, GREEN

class FortuneArea(Stage):
  bg_id = "fortune"
  scale = 16
  links = {
    "entrance": Link(cell=(2, 6), direction=(0, 1))
  }
  layout = [
    "################",
    "################",
    "################",
    "################",
    "###..........###",
    "###....1.....###",
    "###...2......###",
    "###...#####..###",
    "###..........###",
    "##............##",
    "##.....0......##",
    "##....#..#....##",
    "################",
    "################",
  ]

  def __init__(stage, hero):
    super().__init__()
    stage.use(stage.layout, {
      "0": hero,
      "1": Actor(
        core=MageCore(name="Mira"),
        facing=(0, 1),
        color=ORANGE,
        moving=True,
        move_period=45,
        is_shopkeep=True,
        message=lambda talkee, ctx: [
          "{}: Welcome...".format(talkee.get_name().upper()),
          lambda: ShopContext(
            hud=ctx.hud,
            items=list(map(resolve_item, [
              "Potion",
              "Potion",
              "Ankh",
              "Elixir",
              "Cheese",
              "Cheese",
              "Cheese",
              "Bread",
              "Fish",
              "Fish",
              "Balloon",
              "Emerald",
              "Antidote",
              "Antidote",
              "Antidote",
              "Antidote",
              "Amethyst",
              "AngelTears",
              "AngelTears",
              "RedFerrule",
              "Diamond"
            ]))
          )
        ]
      ),
      "2": FortuneDesk()
    })
