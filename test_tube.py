"""
This is predominately a space for things I will revisit or do away with.
"""

"""
This is a function to do attacks, very basic.
I added the random for fun.

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
"""