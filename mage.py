from combatant import Combatant

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
