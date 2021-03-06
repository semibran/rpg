from dungeon.props.door import Door, SpriteMap
from contexts.prompt import PromptContext, Choice
from filters import replace_color
from colors.palette import SAFFRON, GOLD
from items.dungeon.key import Key

class TreasureDoor(Door):
  sprites = SpriteMap(
    closed="door_beetle",
    opened="door_beetle_open",
    opening_frames=[
      "door_beetle",
      "door_beetle_turn",
      "door_beetle_opening",
      "door_beetle_open"
    ]
  )

  def effect(door, game):
    effect = super().effect
    if door.opened:
      return
    inventory = game.get_inventory()
    if Key in inventory:
      game.open(PromptContext(("Use the ", Key().token(), "?"), [
        Choice("Yes"),
        Choice("No", default=True, closing=True)
      ], on_close=lambda choice: (
        choice and choice.text == "Yes" and (
          inventory.remove(Key),
          effect(game)
        )
      )))
    else:
      game.log.print("The door is locked...")

  def render(door, anims):
    sprite = super().render(anims)
    sprite.image = replace_color(sprite.image, SAFFRON, GOLD)
    return sprite
