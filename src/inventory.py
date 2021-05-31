class Inventory:
  tabs = ["consumables", "materials", "equipment"]

  def __init__(inv, size, items=[]):
    cols, rows = size
    inv.cols = cols
    inv.rows = rows
    inv.items = items

  def is_full(inv):
    return len(inv.items) == inv.cols * inv.rows

  def append(inv, item):
    if not inv.is_full():
      inv.items.append(item)
      return True
    else:
      return False
