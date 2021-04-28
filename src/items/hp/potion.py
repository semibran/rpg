from dataclasses import dataclass
from items.hp import HpItem

@dataclass(frozen=True)
class Potion(HpItem):
  name: str = "Potion"
  desc: str = "Restores 20 HP."
  hp: int = 20
