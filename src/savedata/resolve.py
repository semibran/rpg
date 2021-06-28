from items.ailment.antidote import Antidote
from items.ailment.amethyst import Amethyst
from items.sp.bread import Bread
from items.sp.cheese import Cheese
from items.sp.sapphire import Sapphire
from items.sp.fish import Fish
from items.materials.diamond import Diamond
from items.materials.angeltears import AngelTears
from items.materials.redferrule import RedFerrule
from items.hp.ankh import Ankh
from items.hp.ruby import Ruby
from items.hp.elixir import Elixir
from items.hp.potion import Potion
from items.dungeon.key import Key
from items.dungeon.emerald import Emerald
from items.dungeon.balloon import Balloon
from skills.ailment.virus import Virus
from skills.ailment.somnus import Somnus
from skills.ailment.exoculo import Exoculo
from skills.weapon.tackle import Tackle
from skills.weapon.stick import Stick
from skills.weapon.club import Club
from skills.weapon.rare import RareWeapon
from skills.weapon.longinus import Longinus
from skills.weapon.caladbolg import Caladbolg
from skills.weapon.mjolnir import Mjolnir
from skills.attack.shieldbash import ShieldBash
from skills.attack.helmsplitter import HelmSplitter
from skills.attack.blitzritter import Blitzritter
from skills.magic.vortex import Vortex
from skills.magic.hirudo import Hirudo
from skills.magic.ignis import Ignis
from skills.magic.fulgur import Fulgur
from skills.magic.glacio import Glacio
from skills.field.detectmana import DetectMana
from skills.support.anastasis import Anastasis
from skills.support.counter import Counter
from skills.support.sana import Sana
from skills.armor.hpup import HpUp
from dungeon.props.bag import Bag
from dungeon.props.treasuredoor import TreasureDoor
from dungeon.props.palm import Palm
from dungeon.props.battledoor import BattleDoor
from dungeon.props.coffin import Coffin
from dungeon.props.soul import Soul
from dungeon.props.pushblock import PushBlock
from dungeon.props.door import Door
from dungeon.props.pushtile import PushTile
from dungeon.props.puzzledoor import PuzzleDoor
from dungeon.props.chest import Chest
from dungeon.features.oasisroom import OasisRoom
from dungeon.features.elevroom import ElevRoom
from dungeon.features.pitroom import PitRoom
from dungeon.features.coffinroom import CoffinRoom
from dungeon.features.treasureroom import TreasureRoom
from dungeon.features.arena import BattleRoom
from dungeon.features.maze import Maze
from dungeon.features.vertroom import VerticalRoom
from dungeon.features.specialroom import SpecialRoom
from dungeon.features.exitroom import ExitRoom
from dungeon.features.room import Room
from dungeon.actors.genie import Genie
from dungeon.actors.npc import Npc
from dungeon.actors.skeleton import Skeleton
from dungeon.actors.mage import Mage
from dungeon.actors.eye import Eye
from dungeon.actors.mimic import Mimic
from dungeon.actors.knight import Knight
from dungeon.actors.mushroom import Mushroom
from dungeon.actors.soldier import Soldier

def resolve_item(key):
  if key == "Antidote": return Antidote
  if key == "Amethyst": return Amethyst
  if key == "Bread": return Bread
  if key == "Cheese": return Cheese
  if key == "Sapphire": return Sapphire
  if key == "Fish": return Fish
  if key == "Diamond": return Diamond
  if key == "AngelTears": return AngelTears
  if key == "RedFerrule": return RedFerrule
  if key == "Ankh": return Ankh
  if key == "Ruby": return Ruby
  if key == "Elixir": return Elixir
  if key == "Potion": return Potion
  if key == "Key": return Key
  if key == "Emerald": return Emerald
  if key == "Balloon": return Balloon

def resolve_skill(key):
  if key == "Virus": return Virus
  if key == "Somnus": return Somnus
  if key == "Exoculo": return Exoculo
  if key == "Tackle": return Tackle
  if key == "Stick": return Stick
  if key == "Club": return Club
  if key == "RareWeapon": return RareWeapon
  if key == "Longinus": return Longinus
  if key == "Caladbolg": return Caladbolg
  if key == "Mjolnir": return Mjolnir
  if key == "ShieldBash": return ShieldBash
  if key == "HelmSplitter": return HelmSplitter
  if key == "Blitzritter": return Blitzritter
  if key == "Vortex": return Vortex
  if key == "Hirudo": return Hirudo
  if key == "Ignis": return Ignis
  if key == "Fulgur": return Fulgur
  if key == "Glacio": return Glacio
  if key == "DetectMana": return DetectMana
  if key == "Anastasis": return Anastasis
  if key == "Counter": return Counter
  if key == "Sana": return Sana
  if key == "HpUp": return HpUp

def resolve_elem(key):
  if key == "Bag": return Bag
  if key == "TreasureDoor": return TreasureDoor
  if key == "Palm": return Palm
  if key == "BattleDoor": return BattleDoor
  if key == "Coffin": return Coffin
  if key == "Soul": return Soul
  if key == "PushBlock": return PushBlock
  if key == "Door": return Door
  if key == "PushTile": return PushTile
  if key == "PuzzleDoor": return PuzzleDoor
  if key == "Chest": return Chest
  if key == "OasisRoom": return OasisRoom
  if key == "ElevRoom": return ElevRoom
  if key == "PitRoom": return PitRoom
  if key == "CoffinRoom": return CoffinRoom
  if key == "TreasureRoom": return TreasureRoom
  if key == "BattleRoom": return BattleRoom
  if key == "Maze": return Maze
  if key == "VerticalRoom": return VerticalRoom
  if key == "SpecialRoom": return SpecialRoom
  if key == "ExitRoom": return ExitRoom
  if key == "Room": return Room
  if key == "Genie": return Genie
  if key == "Npc": return Npc
  if key == "Skeleton": return Skeleton
  if key == "Mage": return Mage
  if key == "Eye": return Eye
  if key == "Mimic": return Mimic
  if key == "Knight": return Knight
  if key == "Mushroom": return Mushroom
  if key == "Soldier": return Soldier

def resolve_material(material):
  if material is Diamond: return None
  if material is AngelTears: return Eye
  if material is RedFerrule: return Mushroom
