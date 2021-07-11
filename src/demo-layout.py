import sys
from contexts.app import App
from contexts.game import GameContext
from savedata import load

if len(sys.argv) != 2:
  print("usage: demo-layout.py src/example.json")
  exit()

App(title="layout demo",
  context=GameContext(
    savedata=load("src/data00.json", sys.argv[1])
  )
).init()
