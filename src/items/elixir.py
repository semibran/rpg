from assets import load as use_assets

class Elixir:
  def __init__(elixir):
    elixir.name = "Elixir"
    elixir.kind = "hp"
    elixir.desc = "Restores all HP and SP."

  def effect(elixir, ctx):
    game = ctx.parent
    hero = game.hero
    ally = game.ally
    if (hero.get_hp() < hero.get_hp_max()
    or ally.get_hp() < ally.get_hp_max()
    or game.sp < game.sp_max):
      hero.set_hp(hero.get_hp_max())
      ally.set_hp(ally.get_hp_max())
      game.sp = game.sp_max
      return (True, "The party restored full HP and SP.")
    else:
      return (False, "Nothing to restore!")

  def render(elixir):
    return use_assets().sprites["icon_elixir"]
