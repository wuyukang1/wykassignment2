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
