"""
Combatant Class

This class represents a basic combatant in the Combat Game. It serves as the foundation
for all fighter types in the game, providing core attributes and methods that are common
to all combatants.

Attributes:
    name (str): The name of the combatant.
    maxHealth (int): The maximum health points the combatant can have.
    health (int): The current health points of the combatant.
    strength (int): The strength attribute, affecting physical damage.
    defence (int): The defence attribute, reducing incoming damage.
    magic (int): The magic attribute, affecting magical abilities.
    ranged (int): The ranged attribute, affecting ranged attack damage.

Methods:
    takeDamage(damage): Calculates and applies damage to the combatant.
    attack(target): A placeholder method for the attack action (to be overridden).
    reset(): Restores the combatant's health to its maximum value.
    details(): Returns a string representation of the combatant's stats.

The Combatant class is designed to be subclassed by specific fighter types
(e.g., Warrior, Mage, Ranger) which will implement their own unique abilities
and characteristics while inheriting these basic attributes and methods.
"""
class Combatant:
    def __init__(self, name, maxHealth, strength, defence, magic, ranged):
        self.name = name
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.strength = strength
        self.defence = defence
        self.magic = magic
        self.ranged = ranged

    def takeDamage(self, damage):
        actualDamage = max(0, damage - self.defence)
        if actualDamage == 0:
            print(f"{self.name}'s defence level blocked {self.defence} damage")
            print("'TING' 0 damage!")
        else:
            self.health -= actualDamage
            print(f"{self.name} took {actualDamage} damage and has {self.health} health remaining")

    def attack(self, target):
        pass

    def reset(self):
        self.health = self.maxHealth

    def details(self):
        return f"{self.name} is a {self.__class__.__name__} and has the following stats:\n" \
               f"Health: {self.health}\n" \
               f"Strength: {self.strength}\n" \
               f"Defence: {self.defence}\n" \
               f"Magic: {self.magic}\n" \
               f"Ranged: {self.ranged}"
