# very early build
# this is what makes chests in my awesome RPG in Python full of loot
# well it might one day
# this is just a randomizer that outputs text of what the item will be

# when opened decide based on probabilities what loot to generate
# lists for each thing
# function for each thing
# roll dice and if value agreed upon then run function, else dont run function
# function rolls dice to see what loot comes out

import random

lootweapons = {
    "quality": ["common", "rare", "epic"],
    "weapons": ["dagger", "sword", "axe"]
}

lootshields = {
    "quality": ["common", "rare", "epic"],
    "shields": ["buckler", "kite", "heater"]
}

lootpotions = {
    "potionsquantity": ["one", "two", "three"],
    "potionssubject": "potion(s)",
    "potionsquality": ["weak", "strong", "fantastic"],
    "potioneffect": ["of strength", "of healing", "of mana"]
}

lootgold = {
    "goldquantity": "piece(s)"
}

selectweaponquality = random.choices(lootweapons["quality"], weights=[80, 15, 5], k=1)
selectweapontype = random.sample(lootweapons["weapons"], 1)

selectshieldquality = random.choices(lootshields["quality"], weights=[80, 15, 5], k=1)
selectshieldtype = random.sample(lootshields["shields"], 1)

selectpotionquantity = random.choices(lootpotions["potionsquantity"], weights=[80, 15, 5], k=1)
selectpotionquality = random.choices(lootpotions["potionsquality"], weights=[80, 15, 5], k=1)
selectpotions = random.sample(lootpotions["potioneffect"], 1)

selectgoldamount = random.randint(1, 20)

weaponitemgen = "You have found {} {}."
shielditemgen = "You have found {} {} shield."
potionitemgen = "You have found {} {} {} {}."
golditemgen = "You have found {} {} of gold."

weapon = weaponitemgen.format(selectweaponquality, selectweapontype)
shield = shielditemgen.format(selectshieldquality, selectshieldtype)
potion = potionitemgen.format(selectpotionquantity, selectpotionquality, lootpotions["potionssubject"], selectpotions)
gold = golditemgen.format(selectgoldamount, lootgold["goldquantity"])

counter = 0

while counter < 1:
    useraction = input("Press (e) to open chest in this dark dungeon you are in as a mighty hero.")
    if "e" in useraction:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        dice4 = random.randint(1, 6)
        if dice1 < 3:
            print(weapon)
        else:
            print("This chest had no weapon in it.")
        if dice2 < 3:
            print(shield)
        else:
            print("This chest had no shield in it.")
        if dice3 <3:
            print(potion)
        else:
            print("This chest had no potion in it.")
        if dice4 < 3:
            print(gold)
        else:
            print("This chest had no gold pieces in it.")
        counter+=1
    else:
        print("You did not press (e), so an enemy just escorted you out of his dungeon politely.")
print("You are out of the dungeon, in your favourite pub, sipping beer tea.")
