"""
Field Class

This class represents a combat field in the Combat Game. Each field has a name and can
affect combatants in unique ways depending on the type of field.

Attributes:
    name (str): The name of the field. It can be one of "Toxic Wasteland", "Healing Meadows",
                or "Castle Walls".

Methods:
    changeField(): Randomly selects and returns a field name from the predefined list of fields.
    applyFieldEffect(combatant1, combatant2): Applies the field's effect on two combatants based
                                              on the current field type.

The Field class is used to create an environment that can have positive, negative, or neutral
effects on the combatants engaged in a battle. The specific effects of each field are:

    - Toxic Wasteland: Reduces the health of both combatants by 5 points.
    - Healing Meadows: Increases the health of both combatants by 5 points, up to their maximum health.
    - Castle Walls: No effect.
"""

import random

class Field:
    def __init__(self):
        self.name = self.changeField()

    def changeField(self):
        fields = ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]
        return random.choice(fields)

    def applyFieldEffect(self, combatant1, combatant2):
        if self.name == "Toxic Wasteland":
            combatant1.health -= 5
            combatant2.health -= 5
            print(f"Toxic Wasteland damages both combatants for 5 health!")
        elif self.name == "Healing Meadows":
            combatant1.health = min(combatant1.health + 5, combatant1.maxHealth)
            combatant2.health = min(combatant2.health + 5, combatant2.maxHealth)
            print(f"Healing Meadows heals both combatants for 5 health!")
        # Castle Walls has no effect
