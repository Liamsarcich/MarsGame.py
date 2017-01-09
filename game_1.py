import time
import random



def dohit(chance):
    ran = random.randint(0, 10)
    if ran < chance:
        return True
    else:
        return False

def wait():
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('..')
    time.sleep(1.5)
    print('...')
    time.sleep(3)
    print('....')

def die(msg):
    print(msg)
    wait()
    print('You find yourself in your bed with a fine mist of cold sweat on your skin')
    quit()

yes = {'yes', 'yea', 'yeah', 'ya', 'yep'}

fight = {'fight', 'attack', 'kill', 'murder', 'yes'}

weapons = {
    "axe": {'dmg':4, 'chance':8, 'text': "The axe takes a massive drawback and flies towards the ogre with incredible power!"},
    "shovel": {'dmg':2, 'chance':8, 'text': "YOU ATTEMPTED TO ATTACK WITH A SHOVEL?! WHAT IS WRONG WITH YOU?!"},
    "sword": {'dmg':3, 'chance':8, 'text': 'The sword takes a massive swing towards the orge!'},
    "bow": {'dmg':3, 'chance':6, 'text': 'You let loose your arrow!'},
    "fork": {'dmg':1, 'chance':2, 'text': 'your fork bounces off. You are stupid.'}
}

useables = {
    "HealingPotion": {'dmg':-4, 'chance':10, 'have':0, 'text': 'Ahh, refreshing and envigorating!'},
    "MysteryPotion": {'dmg':3, 'chance':5, 'have':0, 'text': "Don't trust potions that you don't know of..."}
}

npcs = {
    "ogre": {'hp':7, 'dmg':5, 'chance':3, 'text': "The ogre retaliates with a swipe from their club"}
}


print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=")
print("|                     GAME                  |")
print("|        By Master L and Master M, 2016     |")
print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=\n")



response = input("Start magnificent adventure? ").lower()

if response in yes:
    print("\nOkay, but first, riddle me this.")
else:
    print("\nUntil next time, then.")
    quit()

age_option = int(input("What is your age? "))
denied = "\nYe shall not embark on this dangerous adventure little one."

print(age_option)
if age_option >= 13:
    print('You are a wanderer')
else:
    print(denied)
    quit()

print("You have been following the a road, you don't know where it leads to but you have been following it")

select = input("There is a fork in the road, left or right? ").lower()
right = "right"
left = "left'"
safe = "You found a wonderful cache filled to the brim with weapons."
fail = "You tripped and fell into a spot of quicksand, you attempted to grasp a nearby branch and failed. After much effort you died a bitter death."
print('\n')
print(select)
if select == right:
    print(safe)
else:
    die(fail)
    quit()


print("You look inside the cache")
print("Inside the cache you find the following weapons, a sword, an axe and shovel.")
weapon_select = input("Which do you pick?").lower()

print(weapon_select)
if weapon_select == "shovel":
    print("HAHAHAHA")
    wait()
    print("Good luck, you'll need it")
elif weapon_select == "axe":
    print("A fine weapon indeed")
else:
    weapon_select == "sword"
    print("As noble as a knight!")

ogre_health = npcs["ogre"]['hp']
player_health = 6

alive = True

if input("\nOh no, an ogre! fight or run?").lower() == 'fight':
    while(alive):
        weapons[weapon_select]['dmg']
        print(weapons[weapon_select]['text'])
        if dohit(weapons[weapon_select]['chance']): #chance of hitting
            print("DMG to ogre: "+str(weapons[weapon_select]['dmg']))
            ogre_health -= weapons[weapon_select]['dmg']
        else:
            print("Your attack failed")
        if dohit(npcs["ogre"]['chance']): #3/10 chance of hitting
            player_health -= npcs["ogre"]['dmg']
            print(npcs["ogre"]['text'])
            print("DMG from ogre: "+str(npcs["ogre"]['dmg']))
        else:
            print("\nThe ogre attempted to attack you with a swipe but failed")
        print('\n')

        print("\nOgre health: "+str(ogre_health))
        print("\nYour health: "+str(player_health))
        if ogre_health < 0:
            print("\nYe hath felled the beast")
            alive = False
        if player_health < 0:
            die("\nYe hath been slain by the mighty ogre")
        print('\n')

else:
    print("\nYou run with your tail between your legs! You are scum.")
    die("\nYou trip over blades of glass and crack your head on a rock")

loot = 20
check = input("Do you wish to loot the body?")

print(check)
if check.lower() == "yes":
    print("\nYou have found twenty gold pieces!")
else:
    print("\nYou walk away, regretting not looting the body.")

direction = input("Wha  qt direction do you wish to travel in? north, south, east, or west?")

print(direction)
if direction.lower() == "north":
    if (input("\nYou have come across a travelling merchant, do you wish to browse his wares?")) == 'yes':
        print("\n1) Bow and Arrow - 17 Gold Pieces")
        print("\n2) A fork - 5 Gold Pieces")
        print("\n3) A potion mysterious powers - 20 Gold Pieces")
        print("\n4) A potion of healing - 15 Gold Pieces.")
        c = input("Choice: ")

        if c.lower() == "1":
          loot -= 17
          weapons["bow"] = 1
          print("\nYou have purchased a Bow and Arrow.")
          print("\nThe weapon of an archer.")
        elif c.lower() == "2":
          weapons["fork"] = 1
          loot -= 5
          print('\nYou have purchased a fork.')
          print('\nAre you stupid!!?')
        elif c.lower() == "3":
          loot -= 20
          useables["MysteryPotion"]["have"] = 1
          print('\nOooohhhh a mystery potion!')
          print('\nBe careful though, who knows what it could do...')
        elif c.lower() == "4":
          useables["HealingPotion"]["have"] = 1
          loot -= 15
          print('\nPerfect for if you are injured.')

if c.lower() == "1":

    potion_question = input("Do you want to use a potion?")

    print(potion_question)
    if potion_question.lower() == "yes":
        which_potion = input("Which potion do you wish to use? HealingPotion or MysteryPotion?")
        if "heal" in which_potion.lower():
            print('djaskdhjkasbfoweabfg')
            useables["HealingPotion"]["have"] = 0
            print(useables["HealingPotion"]['text'])
            print("Health gained from HealingPotion: "+str(useables["HealingPotion"]['dmg']))
            player_health -= useables["HealingPotion"]['dmg']
            print("\nYour health: "+str(player_health))
        elif "mystery" in which_potion.lower():
            print('djaskdhjkasbfoweabfg')
            useables["MysteryPotion"]["have"] = 0
            print(useables["MysteryPotion"]['text'])
            print("Health lost from MysteryPotion: "+str(useables["MysteryPotion"]['dmg']))
            player_health -= useables["MysteryPotion"]['dmg']
            print("\nYour health: "+str(player_health))
        else:
            print("Saving it for later eh? Good for you.")


elif direction.lower() == "south":
    print("\nYou come across another ogre! This one bigger than the last.")
    wait()
    print("\nHe has crushed you, you had no chance...")
    quit()
elif direction.lower() == "east":
    print("\nYou get mugged and lose all your gold pieces!")
    print("\nYou don't want to carry on in this wolrd.")
    die("\nYou commit suicide.")
    print('\n')
elif direction.lower() == "west":
    print("\nYou come across a pond of infinity")
    print("\nYou drink from it.")
    print("\nYou are now a god! You do not need this puny adventure")
    quit()
