from dataclasses import dataclass
from skills import Skill

@dataclass
class WeaponSkill(Skill):
  cost: int = 1
  st: int = 0
