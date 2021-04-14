from skills import Skill
from anims.attack import AttackAnim
from anims.pause import PauseAnim

class DetectMana(Skill):
  def __init__(skill):
    super().__init__(
      name="Detect Mana",
      kind="support",
      element=None,
      desc="Reveals hidden passages",
      cost=1,
      radius=0
    )

  def effect(skill, game, on_end=None):
    game.log.print("But nothing happened...")