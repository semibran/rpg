from random import choice
from math import ceil
from lib.cell import add
from dungeon.features import Feature
from dungeon.props.door import Door
from config import ROOM_WIDTHS, ROOM_HEIGHTS

class Room(Feature):
  EntryDoor = Door
  ExitDoor = Door

  def __init__(room, size=None, cell=None, *args, **kwargs):
    super().__init__(*args, **kwargs)
    room.size = size or (choice(ROOM_WIDTHS), choice(ROOM_HEIGHTS))
    room.cell = cell
    room.entered = False
    room.focused = False

  def get_width(room):
    width, _ = room.get_size()
    return width

  def get_height(room):
    _, height = room.get_size()
    return height

  def get_size(room):
    return room.size

  def get_center(room):
    width, height = room.get_size()
    x, y = room.cell or (0, 0)
    return (
      x + ceil(width / 2) - 1,
      y + ceil(height / 2) - 1
    )

  def get_cells(room):
    cells = []
    col, row = room.cell or (0, 0)
    width, height = room.get_size()
    for y in range(height):
      for x in range(width):
        cells.append((x + col, y + row))
    return cells

  def get_edges(room):
    room_width, room_height = room.size
    left, top = room.cell
    right = left + room_width
    bottom = top + room_height
    edges = []
    for x in range(left, right):
      edges.append((x, top - 2))
      edges.append((x, top - 1))
      edges.append((x, bottom))
      edges.append((x, bottom + 1))
    for y in range(top, bottom):
      edges.append((left - 1, y))
      edges.append((right, y))
    return edges

  def get_corners(room):
    x, y = room.cell or (0, 0)
    width, height = room.size
    return [
      (x, y),
      (x + width - 1, y),
      (x, y + height - 1),
      (x + width - 1, y + height - 1),
    ]

  def get_exits(room):
    return room.get_edges()

  def get_border(room):
    left, top = room.cell
    right = left + room.get_width()
    bottom = top + room.get_height()

    edges = []
    for x in range(left - 1, right + 1):
      edges.append((x, top - 2))
      edges.append((x, top - 1))
      edges.append((x, bottom))
      edges.append((x, bottom + 1))

    for y in range(top, bottom):
      edges.append((left - 1, y))
      edges.append((right, y))

    return edges

  def get_doors(room, stage):
    return [e for e in [stage.get_elem_at(c, superclass=Door) for c in room.get_border()] if e]

  def get_slots(room, cell=None):
    room_x, room_y = cell or room.cell or (0, 0)
    slots = []
    for y in range(room.get_height()):
      for x in range(room.get_width()):
        col, row = x + room_x, y + room_y
        if col % 2 == 1 and row % 3 == 1:
          slots.append((col, row))
    return slots

  def on_focus(room, game):
    room.focused = True
    for door in room.get_doors(game.floor):
      door.focus = game.hero.cell

  def on_blur(room, game):
    for door in room.get_doors(game.floor):
      door.focus = game.hero.cell

  def on_enter(room, game):
    room.entered = True

  def on_exit(room, game): pass
  def on_kill(room, game, target): pass

  def validate(room, cell, slots):
    for slot in room.get_slots(cell):
      if slot not in slots:
        return False
    return True

  def filter_slots(room, slots):
    return [s for s in slots if room.validate(s, slots)]

  def place(room, stage, *args, **kwargs):
    super().place(stage, *args, **kwargs)
    stage.rooms.append(room)
