from contexts.app import App
from contexts.game import GameContext
from savedata import SaveData

App(title="dungeon demo",
  context=GameContext(SaveData(
    place="dungeon",
    sp=40,
    time=0,
    gold=100,
    items=["Potion", "Emerald"],
    skills=["Stick", "Blitzritter"],
    party=["knight"],
    chars={
      "knight": {
        "hp": 23,
        "skills": {
          "Stick": (0, 0),
          "Blitzritter": (1, 0)
        }
      }
    }
  ))
).init()
