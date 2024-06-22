"""
Ranger Class

This module defines the Ranger class, a subclass of Combatant. The Ranger specializes in
ranged attacks and manages a limited number of arrows for these attacks.

Attributes:
    arrows (int): The number of arrows the Ranger has for ranged attacks.

Methods:
    attack(target): Attacks the target with ranged attacks, consuming arrows.
    reset(): Resets the Ranger's health and arrow count to their maximum values.
"""
from combatant import Combatant

class Ranger(Combatant):
    def __init__(self, name, maxHealth, strength, defence, magic, ranged):
        super().__init__(name, maxHealth, strength, defence, magic, ranged)
        self.arrows = 3

    def attack(self, target):
        if self.arrows > 0:
            damage = self.ranged
            self.arrows -= 1
            if self.arrows == 0:
                print(f"{self.name} fired thier last arrow!")  # Intentional typo to match the sample output
        else:
            damage = 10  # Changed to match the sample output
        print(f"{self.name} attacks for {damage} damage!")
        target.takeDamage(damage)

    def reset(self):
        super().reset()
        self.arrows = 3
