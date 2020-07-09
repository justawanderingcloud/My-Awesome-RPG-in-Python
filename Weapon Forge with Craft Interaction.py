# TO DO
# min and max sword stats scale with the skill level of generated craft

import random

materials = 10

class Craft:
    def __init__(self, name, profession, skill):
        self.name = name
        self.profession = profession
        self.skill = skill

    def __str__(self):
        return f"Hello adventurer. My name is {self.name} and I am a {self.profession}."

    def skilllevel(self):
        global craftcost
        craftcost = 10
        if self.skill == 1 and self.skill < 2:
            craftcost -= 0
            return "I am at your service. I am a journeyman blacksmith."
        elif self.skill > 3 and self.skill < 5:
            craftcost -= 2
            return "I am at your service. I am a journeyman blacksmith."
        elif self.skill > 6 and self.skill <= 8:
            craftcost -= 4
            return "I am at your service. I am a master blacksmith."
        elif self.skill >= 9:
            craftcost -= 6
            return "I am a grandmaster blacksmith."
        else:
            return "Something Went Wrong"


craftnpc = Craft("Honza", "blacksmith", 8)

print(craftnpc, craftnpc.skilllevel())


class Sword:
    itemtype = "weapon"

    def __init__(self, name, attack, defense, speed, reqstrength):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.reqstrength = reqstrength

    def __str__(self):
        return f"This {self.name} sword requires {self.reqstrength} of Strength points. " \
               f"Its attack is {self.attack} points, {self.defense} defense points " \
               f"and has the speed of {self.speed} points. "


dice1 = random.randint(1, 20)
dice2 = random.randint(1, 20)
dice3 = random.randint(1, 20)
dice4 = random.randint(1, 20)

while materials > 8:
    print("You have", materials, "iron. Each sword costs", craftcost, "iron.")
    swordname = input("Enter the name of your sword you would like to have forged with random attributes.")
    forgedsword = Sword(swordname, dice1, dice2, dice3, dice4)
    materials -= craftcost
    print(forgedsword)
else:
    print("You do not have enough materials to make another weapon. You have", materials, "iron.")
