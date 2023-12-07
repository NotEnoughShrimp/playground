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

a = Player("Hero", strength=100, dexterity=100, constitution=100)
b = Monster("BingBong", strength=100,dexterity=100,constitution=100)

def perform_attack(attacker, target):
    numbers = [1,2,3,4,5,6,7,8,9,10]
    hit = random.choice(numbers)
    if hit > 5:
        print(f"{attacker.name} attacked for: {attacker.attack}")
        target.health -= attacker.attack
        return True
    else:
        print("miss")
        return False
        
player_action = input("You see a suspicious clown, what do you do? ")
if player_action == 'attack':
    if perform_attack(a,b):
        print("good job, one less clown in the world")
    else:
        print("Oh he doesn't look happy")
        if perform_attack(b,a):
            print("uh oh, it's mad")
        else:
            print("nah you're good")
else:
    print("ok, let's keep moving")