"""
This is predominately a space for things I will revisit or do away with.
"""

"""
basic attack function
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def perform_attack(attacker, target):
    numbers = [1,2,3,4,5,6,7,8,9,10]
    hit = random.choice(numbers)
    if hit > 5:
        target.health -= attacker.attack
        return True
    else:
        print("miss")
        return False
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is for initiative. A lot of finetuning needed.
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
units = [a.core,b.monster_core,c.core]
turn_order = []
for unit in units:
    initiative_value = unit.get_initiative()
    turn_order.append(initiative_value)
    turn_order.sort(reverse=True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""


"""
experience table:
https://blog.jakelee.co.uk/converting-levels-into-xp-vice-versa/#:~:text=First%2C%20come%20up%20with%20a,%3D%20larger%20gaps%20between%20levels)
may follow this example as of 12-8-23
the formula goes: (level/x)^y
    x = amount of exp
    y = rate - 
        lower = slower exp(Maybe tweaking difficulty can be done with this?)
        higher = faster exp
"""

""""""
def level_requirements(retrieve_level_requirement=None):
    
    """ The empty level_table dictionary will be populated as this function executes"""
    level_table = {}
    
    """ base level 1 and experience 0"""
    level = 1
    experience = 0
    
    """ x affects the amount of experience. y determines the next level's experience 
        equirement.
        higher the value of y, the larger the gap"""
    x = 0.07
    y = 2

    """ 
    This For Loop just iterates over a range doing the following:
    - experience_to_level = round(1/0.07)**2 = 204 (Otherwise it'd be
        something along the lines of: 204.0816326530612, and that's just
        messy)
    - apply it to experience. Now, it goes from experience=0 to experience=204
    - the key value of "l", for level, is now assigned the value of experience
    - iterates until the range condition is satisfied.
    """
    for l in range(1, 10 + 1):
        experience_to_level = round((level / x) ** y)
        experience += experience_to_level
        level_table[l] = experience_to_level
        level += 1
        experience = 0
        
    """
    This For Loop is to make the level_table manageable to read. It
    iterates for every level, exp in a Tupled version of the level_tables
    dictionary. Which now will output the key and value inside the level_table
    for it to be more manageable to read.
    """
    # for lv, exp in level_table.items():
    #     print(f"level: {lv} | experience: {exp}")
    
    """ This is for allowing someone to check the specific level to experience"""
    if retrieve_level_requirement is not None and retrieve_level_requirement in level_table:
        print(f"experience required for level {retrieve_level_requirement}: {level_table[retrieve_level_requirement]}")
    elif retrieve_level_requirement is None:
        print("Level & Experience required")
        for lv, exp in level_table.items():
            print(f"Level: {lv}\nExperience required: \t{exp}")


search_for_level = input("What level do you want to see? ").strip()
if search_for_level:
    search_for_level = int(search_for_level)
    level_requirements(search_for_level)
else:
    level_requirements()

