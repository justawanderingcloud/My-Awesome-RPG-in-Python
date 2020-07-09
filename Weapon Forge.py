# asks your the name of your sword and then creates it with random attributes

import random

class Sword:
    itemtype = "weapon"
    def __init__(self, name, attack, defense, speed, reqstrenght):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.reqstrenght = reqstrenght

    def __str__(self):
        return f"This {self.name} sword requires {self.reqstrenght} of Strength points. " \
               f"Its attack is {self.attack} points, {self.defense} defense points " \
               f"and has the speed of {self.speed} points. "

dice1 = random.randint(1, 20)
dice2 = random.randint(1, 20)
dice3 = random.randint(1, 20)
dice4 = random.randint(1, 20)

swordname = input("Enter the name of your sword you would like to have forged with random attributes.")

forgedsword = Sword(swordname, dice1, dice2, dice3, dice4)

print(forgedsword)
