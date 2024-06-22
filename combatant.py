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
