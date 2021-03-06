class Vfx:
  def __init__(vfx, kind, pos, anim=None, color=None, vel=(0, 0)):
    vfx.kind = kind
    vfx.pos = pos
    vfx.anim = anim
    vfx.color = color
    vfx.vel = vel
    vfx.done = False

  def update(vfx):
    pos_x, pos_y = vfx.pos
    vel_x, vel_y = vfx.vel
    vfx.pos = (pos_x + vel_x, pos_y + vel_y)
    if vfx.anim:
      frame = vfx.anim.update()
      if vfx.anim.done:
        vfx.done = True
      return frame
