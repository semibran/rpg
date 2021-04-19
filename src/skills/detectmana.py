from skills import Skill
from anims.attack import AttackAnim
from anims.pause import PauseAnim
from stage import Stage
from actors.mage import Mage

class DetectMana(Skill):
  name = "Detect Mana"
  kind = "field"
  element = None
  desc = "Reveals hidden passages"
  cost = 1
  radius = 0
  users = (Mage,)
  blocks = (
    (0, 0),
  )

  def effect(game, on_end=None):
    user = game.hero
    floor = game.floor
    camera = game.camera

    def on_wait():
      for cell in user.visible_cells:
        if floor.get_tile_at(cell) is Stage.DOOR_HIDDEN:
          game.log.print("You sense a hidden passageway here!")
          camera.focus(cell)
          game.anims.append([PauseAnim(
            duration=75,
            on_end=on_end
          )])
          break
      else:
        game.log.print("There doesn't seem to be anything nearby.")
        if on_end:
          on_end()

    game.anims.append([PauseAnim(
      duration=30,
      on_end=on_wait
    )])
    return user.cell
