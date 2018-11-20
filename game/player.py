import os
import random

class PlayerStart(object): 
    'Create a player'

    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

    def getHealth(self):
        return "health: ", self.health

    def getHealthValue(self):
        return self.health
        
    def getAttack(self):
        return "attack: ", self.attack
    
    def getAttackValue(self):
        return self.attack

    def getDefence(self):#what is self?
        return "defence: ", self.defence

    def getDefenceValue(self):
        return self.defence

    def getAllStats(self):
        return "health: ", self.health, "attack: ", self.attack, "defence: ", self.defence
        # return "attack: ", self.attack
        # return "defence: ", self.defence

    def lvlup(self):
        print ("***LEVEL UP***")
        randomNumHealth = random.randint(1,9)
        randomNumAttack = random.randint(1,9)
        randomNumDefence = random.randint(1,9)
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumHealth):
            print ("health++")
            self.health += randomNumHealth
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumAttack):
            print ("attack++")
            self.attack += randomNumAttack
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumDefence):
            print ("defence++")
            self.defence += randomNumDefence


    # sdef game():
        
	# def prompt(self):
	# 	choice = input("what to do ")
	# 	if int(choice) == 1:
	# 		Player.lvlup(self)
	# 	else:
	# 		print("nothing to do")
