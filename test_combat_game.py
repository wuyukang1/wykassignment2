import pytest
from Field import Field
from Combatants import Combatant
from Ranger import Ranger
from Warrior import Warrior
from Mage import Mage
from PyroMage import PyroMage
from FrostMage import FrostMage
from Arena import Arena

def test_field_creation():
    field = Field()
    assert field.name in ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]

def test_combatant_creation():
    combatant = Combatant("Test", 100, 10, 10, 10, 10)
    assert combatant.name == "Test"
    assert combatant.health == 100

def test_ranger_attack():
    ranger = Ranger("Archer", 100, 10, 10, 10, 50)
    target = Combatant("Target", 100, 10, 10, 10, 10)
    ranger.attack(target)
    assert target.health < 100

def test_warrior_armor():
    warrior = Warrior("Knight", 100, 20, 20, 10, 10, 10)
    warrior.takeDamage(15)
    assert warrior.health == 100
    assert warrior.armourValue == 5

def test_pyromage_flame_boost():
    pyromage = PyroMage("Fire Wizard", 100, 15, 10, 50, 10)
    initial_damage = pyromage.castSpell()
    pyromage.castSpell()  # Cast SuperHeat
    boosted_damage = pyromage.castSpell()
    assert boosted_damage > initial_damage

def test_frostmage_ice_block():
    frostmage = FrostMage("Ice Wizard", 100, 10, 10, 50, 10)
    frostmage.castSpell()  # Cast Ice Block
    frostmage.takeDamage(50)
    assert frostmage.health == 100

def test_arena_duel():
    arena = Arena("Test Arena")
    fighter1 = Warrior("Warrior", 100, 20, 20, 10, 10, 10)
    fighter2 = Ranger("Ranger", 100, 10, 10, 10, 50)
    arena.addCombatant(fighter1)
    arena.addCombatant(fighter2)
    arena.duel(fighter1, fighter2)
    assert fighter1.health < 100 or fighter2.health < 100
