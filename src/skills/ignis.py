from skills import Skill
from anims.attack import AttackAnim
from anims.pause import PauseAnim

ATTACK_DURATION = 12

class Ignis(Skill):
  def __init__(skill):
    super().__init__(
      name="Ignis",
      kind="spell",
      desc="Burns target with flame",
      cost=3,
      radius=2
    )

  def effect(skill, game, on_end=None):
    if game.sp >= skill.cost:
      game.sp -= skill.cost
    game.log.print("But nothing happened...")