"""
https://finalfantasy.fandom.com/wiki/Final_Fantasy_VII_stats

Points, Primary Attributes (PA), Derived Attributes (DA)
Player = Points & PA to determine DA
Monster = Points & DA

Points: experience, level, hp, mp
    - HP and MP are increased by a percentage of the gradient
        - clue: equation for gradient is: m = rise/run
PA: strength, dexterity, vitality, magic, spirit, luck
    - PA on level up increases by 0 and 3
DA: attack, attack%, defense, defense %, magic attack, magic defense,magic defense %
    - attack, attack_percentage, defense, defense_percentage, magic_attack, magic_defense, magic_defense_percentage

For testing purposes, I am using Caith Sith's tables for this program.
I would use Cloud, but he doesn't have any stats between 2-5, and we're going from 1-10.

Refactoring will be later, just get it running.
"""
import random

class Points:
    def __init__(self, experience_points, level, hp, mp):
        self.experience_points = experience_points
        self.level = level
        self.hp = hp
        self.mp = mp

    def reference_table(self):
        """ level will always be key, values taken from Final Fantasy wiki"""
        experience_table = {
            1: 0,
            2: 6,
            3: 33,
            4: 95,
            5: 205,
            6: 377,
            7: 625,
            8: 963,
            9: 1404,
            10: 1962
        }
        base_health_table = {
            1: 224,
            2: (236, 250),
            3: (257, 274),
            4: (278, 298),
            5: (302, 322),
            6: (323, 346),
            7: (347, 370),
            8: (371, 394),
            9: (392, 418),
            10: (416,442)
        }
        base_mp_table = {
            1: 18,
            2: (19,24),
            3: (28,30),
            4: (34,36),
            5: (39,42),
            6: (45,48),
            7: (51,54),
            8: (56,60),
            9: (62,66),
            10: (68, 72)
        }


class Primary_Attributes:  # We're assuming Cait Sith level 1
    def __init__(self, name = None, strength=10, dexterity=5, vitality=11, magic=13, spirit=11, luck=14, attack_percent=0, defense_percent=0):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.magic = magic
        self.spirit = spirit
        self.luck = luck
        self.attack_percent = attack_percent
        self.defense_percent = defense_percent

class Derived_Attributes:
    def __init__(self, primary_attribute, level, equipment=None):
        self.primary_attribute = primary_attribute
        self.level = level
        self.equipment = equipment or Equipment()

    def calculate_physical_damage(self):
        attack = self.primary_attribute.strength + self.equipment.weapon_attack
        base_damage = attack + (((attack+self.level)/32)*((attack*self.level)/32))
        return base_damage
    
    def calculate_hit(self):
        """determines whether attack hits"""
        attacker_dexterity = self.primary_attribute.dexterity
        attack_percent = self.primary_attribute.attack_percent
        example_percent = random.randrange(1,20)

        hit_percent = (attacker_dexterity/4)+attack_percent+example_percent
        return hit_percent

class Equipment:
    def __init__(self, weapon=None, armor=None):
        self.weapon = weapon
        self.armor = armor
        self.weapon_attack = 0
        if weapon:
            self.weapon_attack = weapon.get_attack_value()
class Weapon:
    def __init__(self, name, attack_value):
        self.name = name
        self.attack_value = attack_value

    def get_attack_value(self):
        return self.attack_value
    
def placeholder():
    """I'll use this once I figure out how to apply it, or just delete"""
    yellow_mega_phone = {
        "attack": 36,
        "magic attack": 8,
        "attack percentage": 100,

    }
    silver_armlet = {
        "defense": 34,
        "defense percentage": 4,
        "magic defense": 22
    }

cait_sith_primary = Primary_Attributes(name='Cait Sith')
equipment = Equipment(weapon=Weapon('yellow mega phone', 36))
cait_sith_derived = Derived_Attributes(primary_attribute=cait_sith_primary, level=1, equipment=equipment)

target_defense = random.randint(1,10)
initiate_attack = cait_sith_derived.calculate_hit()
attack = round(cait_sith_derived.calculate_physical_damage())
if initiate_attack >= target_defense:
    print(f'You hit: {attack}')
else:
    print('miss')
