"""
Warrior and Subclasses

This module defines the Warrior class and its subclasses Dharok, Guthans, and Karil. Each class
inherits from the Combatant class and adds unique physical abilities and attributes.

Warrior Class:
    A basic warrior with enhanced defence through armour.

Attributes:
    armourValue (int): The value of the warrior's armour, reducing damage taken.

Methods:
    takeDamage(damage): Reduces damage taken based on the armour value.
    attack(target): Attacks the target with physical strength.
    reset(): Resets the warrior's health and armour value to their maximum values.

Dharok Class:
    A subclass of Warrior with increased damage based on missing health.

Methods:
    attack(target): Attacks the target with additional damage based on missing health.

Guthans Class:
    A subclass of Warrior with a healing ability during attacks.

Methods:
    attack(target): Attacks the target and heals the warrior for a portion of the strength attribute.

Karil Class:
    A subclass of Warrior with enhanced ranged damage.

Methods:
    attack(target): Attacks the target with additional ranged damage.
"""
from combatant import Combatant

class Warrior(Combatant):
    def __init__(self, name, maxHealth, strength, defence, magic, ranged, armourValue):
        super().__init__(name, maxHealth, strength, defence, magic, ranged)
        self.armourValue = armourValue

    def takeDamage(self, damage):
        if self.armourValue > 0:
            blocked = min(self.armourValue, damage)
            print(f"{self.name}'s armour blocked {blocked} damage")
            damage -= blocked
            self.armourValue -= 5
            if self.armourValue <= 0:
                print("Armour shattered!")
        super().takeDamage(damage)

    def attack(self, target):
        damage = self.strength
        print(f"{self.name} attacks for {damage} damage!")
        target.takeDamage(damage)

    def reset(self):
        super().reset()
        self.armourValue = 10

class Dharok(Warrior):
    def attack(self, target):
        bonus_damage = self.maxHealth - self.health
        damage = self.strength + bonus_damage
        print(f"The power of Dharok activates adding {bonus_damage} damage")
        print(f"{self.name} attacks for {damage} damage!")
        target.takeDamage(damage)

class Guthans(Warrior):
    def attack(self, target):
        heal = self.strength // 5
        self.health = min(self.health + heal, self.maxHealth)
        print(f"The power of Guthans activates healing {self.name} for {heal}")
        super().attack(target)

class Karil(Warrior):
    def attack(self, target):
        print(f"The power of Karil activates adding {self.ranged} damage!")
        damage = self.strength + self.ranged
        print(f"{self.name} attacks for {damage} damage!")
        target.takeDamage(damage)
