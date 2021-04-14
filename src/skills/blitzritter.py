from skills import Skill
from anims.attack import AttackAnim
from anims.pause import PauseAnim
from anims.attack import AttackAnim
from config import ATTACK_DURATION

class Blitzritter(Skill):
  def __init__(skill):
    super().__init__(
      name="Blitzritter",
      kind="lance",
      element=None,
      desc="Pierces two squares ahead",
      cost=4,
      radius=2
    )

  def effect(skill, game, on_end=None):
    camera = game.camera
    floor = game.floor
    user = game.hero
    hero_x, hero_y = user.cell
    delta_x, delta_y = user.facing
    target_cell = (hero_x + delta_x, hero_y + delta_y)
    target_actor = floor.get_actor_at(target_cell)
    camera.focus(target_cell)
    game.anims.append([
      AttackAnim(
        duration=ATTACK_DURATION,
        target=user,
        src_cell=user.cell,
        dest_cell=target_cell,
        on_end=lambda: (game.anims[0].append(PauseAnim(
          duration=45,
          on_end=lambda: (
            game.log.print("But nothing happened..."),
            camera.blur(),
            on_end()
          )
        )))
      )
    ])