class Stat_Block:
    def __init__(self, strength = 8, dexterity = 8, constitution = 8, intelligence = 8, wisdom = 8, charisma = 8, level=None, name = None):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.level = level
        self.name = name
    
    def __str__(self) -> str:
        return f"Strength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"

class Player(Stat_Block):
    def __init__(self, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8, level=None, name=None, experience=0):
        super().__init__(strength, dexterity, constitution,intelligence,wisdom,charisma,level,name)
        self.experience = experience
    
    def level_up(self):
        experience_to_level = {
            "1": 0,
            "2": 300,
            "3": 900,
            "4": 2700,
            "5": 6500
        }
        for level, required in experience_to_level.items():
            if self.experience >= required:
                self.level = int(level)
                print(f"Congratulations! You're now level {level}")
            else:
                remaining_experience = required - self.experience
                print(f"You require {remaining_experience} experience to reach {level}")
                break

start_experience = 0
name = input("what is your name? ").title()
start = input("Easy [1], Medium [2], Hard[3]: ")
if start == "1":
    start_experience = 6500
elif start  == "2":
    start_experience = 900
elif start == "3":
    start_experience = 0

player = Player(strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8, level=1, name=name, experience=start_experience)
player.level_up()