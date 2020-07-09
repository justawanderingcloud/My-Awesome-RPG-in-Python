# gives you 10 Iron as a crafting resource
# asks your the name of your sword and then creates it with random attributes
# checks if you have enough Iron for another sword
# which you do not
# tells you that you do not have enough

import random

materials = 10

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

while materials > 8:
    print("You have", materials, "iron. Each sword costs 8.")
    swordname = input("Enter the name of your sword you would like to have forged with random attributes.")
    forgedsword = Sword(swordname, dice1, dice2, dice3, dice4)
    materials -= 8
    print(forgedsword)
else:
    print("You do not have enough materials to make another weapon. You have only", materials, "iron.")
