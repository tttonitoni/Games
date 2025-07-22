import random

# Entity Class

class Entity :
    
    def __init__(self,name,health,baseattack) :
        self.name = name
        self.health = health
        self.baseattack = baseattack

    def baseattack(self,target) :
        target.health -= self.baseattack

# Player Role Selection

Role = input("Welcome!\n\n1 for meele\n2 for ranger\n3 for mage\n\nChoose your class: ")

if Role == "1" :
    Player = Entity("Meele", 200, 10)
    print(Player.name,Player.health,Player.baseattack)
elif Role == "2" :
    Player = Entity("Ranger", 150, 17)
    print(Player.name,Player.health,Player.baseattack)
elif Role == "3" : 
    Player = Entity("Mage", 100, 24)
    print(Player.name,Player.health,Player.baseattack)
else :
    print("invalid input")

# Fight

def Fight() :
    RandomEnemy = random.randint (0,2)
    if RandomEnemy == 0 :
        Enemy = Entity("tung tung tung sahur", 60, 5)
    elif RandomEnemy == 1 :
        Enemy = Entity("Mario", 80, 10)
    elif RandomEnemy == 2 :
        Enemy = Entity("Mytischer Herr Seiß", 100, 15)
    print(f"You encountered {Enemy.name}")
    
    while Player.health > 0 or Enemy.health > 0 :
        
        Action = int(input(f"What will you do?\n\nHealth : {Player.health}\nBase Attack : {Player.baseattack}\nEnemy's health : {Enemy.health}\nEnemy's attack : {Enemy.baseattack}\n\n1 for attacking\n2 for healing\n3 for escaping\n:"))

        if Action == 1 :
            print("\nYou attacked!")
            Enemy.health -= int(random.randint (-5,5) + Player.baseattack )
            print (f"Enemy's health at {Enemy.health}\n")
            if Enemy.health < -1:
                print("You smoked the enemy!")
                break
        elif Action == 2 :
            Player.health += 10
            print(f"\nYou healed yourself, health now at {Player.health}")
        elif Action == 3 :
            Success = random.randint (0,1)
            if Success == 0 :
                print("\nYou tried to escape but you failed!")
            elif Success == 1 :
                print("You escaped successfully!")
                break
  
# Enemy actions

        EnemyAction = random.randint (0,3)

        if EnemyAction == 3 :
            Enemy.health += 10
            print(f"The enemy has healed himself, enemy's health now at {Enemy.health}")
        else :
            Player.health -= int(random.randint (-5,5) + Enemy.baseattack) 
            print(f"The enemy has attacked, player's health is now at {Player.health}")
        if Player.health < 1 :
            print("-- You died --")
            break
        pass

# Main loop

while Player.health > 0 :
    Direction = input("Will you go (1)right or (2)left?")
    if Direction == "1" :
        print("You made a turn to the right")
    elif Direction == "2" :
        print("You made a turn to the left")
    else :
        print("Invalid, so you're just going to go to the right")
        print("Invalid, choose (1)right or (2)left")
    Event = random.randint(0,5)
    if Event in [0,1] :
        print("You found a healing fountain, you have been healed 25hp")
        Player.health += 25
    if Event in [2,3,4,5] :
        print("You entered a fight!")
        Fight()

print ("You died")
