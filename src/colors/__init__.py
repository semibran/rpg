WHITE = 0xFFFFFF
BLACK = 0x000000
RED = 0xE64646
DARKRED = 0x951F45
VIOLET = 0x8F3ECA
DARKVIOLET = 0x4B238A
YELLOW = 0xFBF236
DARKYELLOW = 0xBA9335
GREEN = 0x2EC169
DARKGREEN = 0x25755F
GRAY = 0x7B748A
DARKGRAY = 0x5A555C
BLUE = 0x3C59E3
DARKBLUE = 0x5130A6
CYAN = 0x64ABFF
GOLD = 0xFCBC82
DARKGOLD = 0xB16B5A
PINK = 0xDB4EDF
DARKPINK = 0x761BA6
SAFFRON = 0xA97352
DARKSAFFRON = 0x4A2044
ORANGE = 0xF99F4C
DARKORANGE = 0x915071
CHARCOAL = 0x2C273C
MINTGREEN = 0x3DE7B8
PURPLE = 0xBA78EE
CORAL = 0xE6A8A8
SEAGREEN = 0x3A827E
COLOR_TILE = SAFFRON

minus_map = {
  WHITE: GRAY,
  GRAY: DARKGRAY,
  DARKGRAY: CHARCOAL,
  RED: DARKRED,
  VIOLET: DARKVIOLET,
  YELLOW: DARKYELLOW,
  GOLD: DARKGOLD,
  SAFFRON: DARKSAFFRON,
  ORANGE: DARKORANGE,
  GREEN: DARKGREEN,
  BLUE: DARKBLUE,
  PINK: DARKPINK,
}

def hexify(color):
  r, g, b = color
  return (r << 16) + (g << 8) + b

def rgbify(color):
  return (
    (color & 0xFF0000) >> 16,
    (color & 0xFF00) >> 8,
    color & 0xFF
  )

def darken_color(color):
  if type(color) is tuple:
    return rgbify(minus_map[hexify(color)]) if hexify(color) in minus_map else rgbify(BLACK)
  if type(color) is int:
    color = color & 0x00FFFFFF
    return rgbify(minus_map[color]) if color in minus_map else rgbify(BLACK)
