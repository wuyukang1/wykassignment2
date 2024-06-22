from field import Field

class Arena:
    def __init__(self, name):
        self.name = name
        self.combatants = []
        self.field = Field()

    def addCombatant(self, combatant):
        if combatant not in self.combatants:
            self.combatants.append(combatant)
            print(f"{combatant.name} was added to {self.name}")
        else:
            print(f"{combatant.name} is already in {self.name}")

    def removeCombatant(self, combatant):
        if combatant in self.combatants:
            self.combatants.remove(combatant)
            print(f"{combatant.name} was removed from {self.name}")
        else:
            print(f"{combatant.name} cannot be removed as they were not found in the arena")

    def listCombatants(self):
        for combatant in self.combatants:
            print(combatant.details())

    def restoreCombatants(self):
        print("----- RESTING -----")
        for combatant in self.combatants:
            combatant.reset()

    def duel(self, combatant1, combatant2):
        if combatant1 not in self.combatants or combatant2 not in self.combatants:
            print(f"One or both combatants are not in {self.name}'s list of fighters")
            return

        if combatant1.health <= 0:
            print(f"{combatant1.name} has no health to battle")
            return

        if combatant2.health <= 0:
            print(f"{combatant2.name} has no health to battle")
            return

        print(
            f"----- Battle has taken place in {self.name} on the {self.field.name} between {combatant1.name} and {combatant2.name} -----")

        for round in range(1, 11):
            print(f"Round {round}")
            self.field.applyFieldEffect(combatant1, combatant2)

            combatant1.attack(combatant2)
            if combatant2.health <= 0:
                print(f"{combatant2.name} has been knocked out!")
                break

            combatant2.attack(combatant1)
            if combatant1.health <= 0:
                print(f"{combatant1.name} has been knocked out!")
                break

        if combatant1.health > 0 and combatant2.health > 0:
            print("The battle ran out of time!")

        print("---------- END BATTLE ----------")
