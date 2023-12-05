class Stat_Block:
    def __init__(self, strength = 10, dexterity = 10, constitution = 10, intelligence = 10, wisdom = 10, charisma = 10, level=None, name = None):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.level = level
        self.name = name
        
        self.str_bonus = 0
        self.dex_bonus = 0
        self.con_bonus = 0
        self.int_bonus = 0
        self.wis_bonus = 0
        self.char_bonus = 0
        
    def apply_modifier(self):
        self.str_bonus = self.mod_value(self.strength)
        self.dex_bonus = self.mod_value(self.dexterity)
        self.con_bonus = self.mod_value(self.constitution)
        self.int_bonus = self.mod_value(self.intelligence)
        self.wis_bonus = self.mod_value(self.wisdom)
        self.char_bonus = self.mod_value(self.charisma)
        
    def mod_value(self, stat_value):
        return stat//2-5

    def initiative(self):
        initiative_roll = random.randint(1,20)
        self.apply_modifier()
        initiative_bonus = self.dex_bonus
        initiative = initiative_roll+initiative_bonus
        return initiative
        
    def armor_class(self):
        self.apply_modifier
        armor_class = 10 + self.dex_bonus
        return armor_class
        
    def __str__(self) -> str:
        return f"Strength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"
    
class Player(Stat_Block):
    def __init__(self, strength=12, dexterity=12, constitution=10, intelligence=12, wisdom=12, charisma=12, level=None, name=None, experience=0):
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

player = Player(strength=12, dexterity=12, constitution=12, intelligence=12, wisdom=12, charisma=12, level=1, name=name, experience=start_experience)
player.level_up()
