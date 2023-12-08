import random

class Core:
    def __init__(self, level=1, strength=10, dexterity=10, constitution=10):
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution

    def get_stats(self):
        health = 100+self.constitution
        attack = round(self.strength+(self.strength+self.level/32)*(self.strength*self.level/32))
        defense = 10+self.constitution*2
        return health, attack, defense

    def get_initiative(self):
        initiative = random.randint(1,20)+(self.dexterity//2)
        return initiative

class Player:
    def __init__(self, name, level=1, strength=10, dexterity=10, constitution=10):
        self.name = name
        self.core = Core(level,strength,dexterity,constitution)
        
        self.health, self.attack, self.defense = self.core.get_stats()
class Monster:
    def __init__(self, name, level=1, strength=10, dexterity=10, constitution=10):
        self.name = name
        self.monster_core = Core(level, strength, dexterity,constitution)
        
        self.health, self.attack, self.defense = self.monster_core.get_stats()

a = Player("Hero", strength=10, dexterity=10, constitution=10)
b = Monster("BingBong", strength=10,dexterity=10,constitution=10)
c = Player("Sidekick", strength=16,dexterity=14,constitution=18)


