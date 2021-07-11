from contexts.app import App
from contexts.game import GameContext
import savedata

App(title="puzzle demo",
  context=GameContext(savedata.load("src/data00.json", "src/data-puzzle.json"))
).init()
