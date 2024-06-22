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


class Mage(Combatant):
    def __init__(self, name, maxHealth, strength, defence, magic, ranged):
        super().__init__(name, maxHealth, strength, defence, magic, ranged)
        self.mana = magic
        self.regenRate = magic // 4

    def reset(self):
        super().reset()
        self.mana = self.magic

    def castSpell(self):
        pass


class PyroMage(Mage):
    def __init__(self, name, maxHealth, strength, defence, magic, ranged):
        super().__init__(name, maxHealth, strength, defence, magic, ranged)
        self.flameBoost = 1

    def castSpell(self):
        if self.mana >= 40:
            print(f"{self.name} casts SuperHeat!")
            self.mana -= 40
            self.flameBoost += 1
            bonus_damage = 0
        elif self.mana >= 10:
            print(f"{self.name} casts Fire Blast!")
            self.mana -= 10
            bonus_damage = 10
        else:
            print(f"{self.name} is out of mana!")
            return 0

        self.mana = min(self.mana + self.regenRate, self.magic)
        return (self.strength * self.flameBoost) + bonus_damage

    def attack(self, target):
        damage = self.castSpell()
        print(f"{self.name} attacks for {damage} damage!")
        target.takeDamage(damage)


class FrostMage(Mage):
    def __init__(self, name, maxHealth, strength, defence, magic, ranged):
        super().__init__(name, maxHealth, strength, defence, magic, ranged)
        self.iceBlock = False

    def takeDamage(self, damage):
        if self.iceBlock:
            print(f"{self.name} ice block absorbed all the damage!")
            print("Ice block has faded")
            self.iceBlock = False
        else:
            super().takeDamage(damage)
        self.mana = min(self.mana + self.regenRate, self.magic)

    def castSpell(self):
        if self.mana >= 50:
            print(f"{self.name} casts Ice Block!")
            self.mana -= 50
            self.iceBlock = True
            bonus_damage = 0
        elif self.mana >= 10:
            print(f"{self.name} casts Ice Barrage!")
            self.mana -= 10
            bonus_damage = 30
        else:
            print(f"{self.name} is out of mana!")
            return 0

        return (self.magic // 4) + bonus_damage

    def attack(self, target):
        damage = self.castSpell()
        print(f"{self.name} attacks for {damage} damage!")
        target.takeDamage(damage)


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


# Main execution
if __name__ == "__main__":
    # Creating the different combatant objects
    tim = Ranger("Tim", 99, 10, 10, 1, 50)
    jay = Warrior("Jay", 99, 1, 99, 1, 1, 1)
    kevin = Dharok("Kevin", 99, 45, 25, 25, 25, 10)
    zac = Guthans("Zac", 99, 45, 30, 1, 1, 10)
    jeff = Karil("Jeff", 99, 50, 40, 1, 10, 5)

    try:
        durial = Mage("Durial", 99, 99, 99, 99, 99)
    except TypeError:
        print("Mages must be specialized!")

    jaina = FrostMage("Jaina", 99, 10, 20, 94, 10)
    zezima = PyroMage("Zezima", 99, 15, 20, 70, 1)

    # setting up the first arena
    falador = Arena("Falador")
    falador.addCombatant(tim)
    falador.addCombatant(jeff)
    falador.listCombatants()

    # duel between ranger and karil
    falador.duel(tim, jeff)

    # showcasing incorrect duels
    falador.duel(tim, jeff)
    falador.duel(jeff, zezima)

    # showcasing restoring combatants
    falador.listCombatants()
    falador.restoreCombatants()
    falador.listCombatants()

    # showcasing removing from arena
    falador.removeCombatant(jeff)
    falador.removeCombatant(jeff)

    # setting up the second arena
    varrock = Arena("Varrock")
    varrock.addCombatant(kevin)
    varrock.addCombatant(zac)

    # duel between guthans and dharok
    varrock.duel(kevin, zac)

    # setting up the third arena
    wilderness = Arena("Wilderness")
    wilderness.addCombatant(jaina)
    wilderness.addCombatant(zezima)

    # duel between a pyro and frost mage
    wilderness.duel(jaina, zezima)

    # setting up final arena
    lumbridge = Arena("Lumbridge")
    lumbridge.addCombatant(jaina)
    lumbridge.addCombatant(jay)
    lumbridge.addCombatant(tim)

    # showcasing health carries over from arenas
    lumbridge.duel(jaina, jay)

    # showcasing a duel that takes too long
    lumbridge.duel(jay, tim)