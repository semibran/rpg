from cores.biped import BipedCore, SpriteMap
from config import KNIGHT_NAME, KNIGHT_HP

class Knight(BipedCore):
  sprites = SpriteMap(
    face_right="knight",
    face_down="knight_down",
    face_up="knight_up",
    walk_right=("knight_walk", "knight", "knight_walk", "knight"),
    walk_down=("knight_walkdown0", "knight_down", "knight_walkdown1", "knight_down"),
    walk_up=("knight_walkup0", "knight_up", "knight_walkup1", "knight_up")
  )

  def __init__(knight, name=KNIGHT_NAME, faction="player", *args, **kwargs):
    super().__init__(
      name=name,
      faction=faction,
      hp=KNIGHT_HP,
      st=15,
      en=9,
      *args,
      **kwargs
    )
