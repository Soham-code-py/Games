from random import choice, randint

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
            self.hp = randint(100, 150)
            self.str = randint(100, 150)
        elif self.type == 'Wizard':
            self.hp = randint(80, 120)
            self.str = randint(100, 230)
        else:
            self.hp = randint(10, 50)
            self.str = randint(30, 50)
    
monster1 = monster()

print(monster1.type)
print(monster1.hp)
print(monster1.str)
