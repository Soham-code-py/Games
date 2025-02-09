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

    def Ninja(self):
        self.hp = 200
        self.Str = 240
        self.stl = 80
    
    def noob(self):
        self.hp = 50
        self.Str = 60
        self.stl = 30
    
    def Blaze(self):
        self.hp = 100
        self.Str = 120
        self.stl = 20

    def Aria(self):
        self.hp = 300
        self.Str = 80
        self.stl = 50

def gemGenerater(monstertype, player):
    if monstertype == "Zombie":
        character
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

character = character()

if '1' in player or 'warrior' in player.lower():
    character.Warrior()
elif '2' in player or 'ninja' in player.lower():
    character.Ninja()
elif '3' in player or 'noob' in player.lower():
    character.noob()
elif '4' in player or 'blaze' in player.lower():
    character.Blaze()
elif '5' in player or 'aria' in player.lower():
    character.Aria()

