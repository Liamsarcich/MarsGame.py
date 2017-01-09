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
    print('You have died, you are lost forever')
    quit()

yes = {'yes', 'yea', 'yeah', 'ya', 'yep'}

fight = {'fight', 'attack', 'kill', 'murder', 'yes'}

weapons = {
    "laser_rifle": {'dmg':25, 'chance':8, 'text': "You take a shot and view a large bright light head towards your target"}
    "survival_knife": {'dmg':10, 'chance':10, 'text': "You bring the knife down on your target"}
    "shotgun": {'dmg':75, 'chance':5, 'text': "A powerful blast erupts from the barrel scattering shot everywhere"}
}

useables = {
    "Health_Pack": {'dmg':-50, 'chance':10, 'have':0, 'text': 'You feel a lot better and are ready to get back to foraging'}
    "Oxygen_Bottle": {'oxygen':100, 'chance':10, 'have':1, 'text': "You have replenished your oxygen and have another hour of breath"}
}

npc = {
    "space_pirate": {'hp':100, 'dmg':15, 'chance':4, 'text': "The space pirate took a shot at you"}
}

print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=")
print("|                    MARSGAME               |")
print("|        By Master L and Master M, 2017     |")
print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=\n")

wait()

print("System Failure")

wait()

print("Initiate Emergency Eject Sequence")

wait()

print("5,4,3,2,1")
