# what always bugged me in games is how opening a chest and finding loot work behind the scenes
# so I decided to write a simple chest loot generator
# each chest may contain a weapon, a shield, some potions and gold pieces
# it might also contain nothing and all the possible variations
# the whole code prints out what you found
# it asks you to press E and then enter as you would in a game to "open" the chest
# the code also allows you to open the chest only once, so it does not run indefinitely

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
