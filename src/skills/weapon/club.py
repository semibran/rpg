from skills.weapon import Weapon
from cores import Core
from cores.knight import KnightCore
from assets import load as use_assets

class Club(Weapon):
  name = "Club"
  desc = "A makeshift weapon."
  element = "axe"
  st = 2
  users = (KnightCore,)
  blocks = (
    (0, 0),
    (1, 0),
  )
