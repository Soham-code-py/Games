#Dungeon Run.
#Objective: get out of the Dungeon ALIVE.

#Gems: You can get gems by defeating a monseter
#depending on the monster, is the gems power.

#Monsters: There are 3 types of monsters, Zombie (easy),
#Goblin (Medium), Wizard (Hard).


# Classes and Funcitons
from random import randint

class monster:
    def __init__(self):
        monsterType = randint(0, 100)

        if monsterType <= 70:
            self.type = 'Zombie'
        elif monsterType > 70 and monsterType <= 90:
            self.type = 'Goblin'
        else:
            self.type = 'Wizard'

        if self.type == 'Goblin':
            self.hp = randint(200, 350)
            self.Str = randint(300, 450)
        elif self.type == 'Wizard':
            self.hp = randint(300, 520)
            self.Str = randint(400, 430)
        else:
            self.hp = randint(10, 150)
            self.Str = randint(30, 100)

class character:
    def Warrior(self):
        self.hp = 100
        self.Str = 140
        self.stl = 30
        return self

    def Ninja(self):
        self.hp = 200
        self.Str = 240
        self.stl = 80
        return self
    
    def noob(self):
        self.hp = 50
        self.Str = 60
        self.stl = 30
        return self
    
    def Blaze(self):
        self.hp = 100
        self.Str = 120
        self.stl = 20
        return self

    def Aria(self):
        self.hp = 300
        self.Str = 80
        self.stl = 50
        return self

def gemGenerater(monstertype, character1):
    if monstertype == 'Zombie':
        hp = randint(-20, 30)
        Str = randint(-10, 20)
        stl = randint(-20, 5)
    elif monstertype == 'Goblin':
        hp = randint(-50, 70)
        Str = randint(-30, 50)
        stl = randint(-30, 10)
    else:
        hp = randint(-50, 150)
        Str = randint(-50, 100)
        stl = randint(-50, 20)
    print('You got a gem!')
    print('HP:', hp)
    print('Str:', Str)
    print('Stl:', stl)
    yn = input('Would you like to equip it?')
    if 'y' in yn.lower():
        character1.hp += hp
        character1.Str += Str
        character1.stl += stl
        print('Gem equipped!')
        print('\t', player)
        print('HP:', character1.hp)
        print('Str:', character1.Str)
        print('Stl:', character1.stl)


#----------------------------------------------------#
# Game code

print("""
Welcome to Dungeon Run!
      
Objective: Get out of the Dungeon ALIVE.
      
Gems: You can get gems by defeating a monster
depending on the monster, is how powerful the gem is.
      
Monsters: There are 3 types of monsters, Zombie (easy),
Goblin (Medium), Wizard (Hard).
      
Depending on the character you choose, you will have
different stats and abillitys.
      
Characters:
""")

print("""1. Warrior
      [HP: 100, STR: 140, STL: 30]
      """)
print("""2. Ninja
      [HP: 200, STR: 240, STL: 80]
      """)
print("""3. Noob
      [HP: 50, STR: 60, STL: 30]
      """)
print("""4. Blaze
      [HP: 100, STR: 120, STL: 20]
      """)
print("""5. Aria
      [HP: 300, STR: 80, STL: 50]
      """)
player = input("Choose your character: ")

character_instance = character()

if '1' in player or 'warrior' in player.lower():
    player = character_instance.Warrior()
elif '2' in player or 'ninja' in player.lower():
    player = character_instance.Ninja()
elif '3' in player or 'noob' in player.lower():
    player = character_instance.noob()
elif '4' in player or 'blaze' in player.lower():
    player = character_instance.Blaze()
elif '5' in player or 'aria' in player.lower():
    player = character_instance.Aria()

gemGenerater('Wizard', player)