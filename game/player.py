import os
import random
import sys
import threading

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

    def setHealthValue(self, damage):
        tempHealth = self.health - damage
        self.health = tempHealth
        self.getHealth()
        
    def getAttack(self):
        return "attack: ", self.attack
    
    def getAttackValue(self):
        return self.attack

    def getDefence(self):
        return "defence: ", self.defence

    def getDefenceValue(self):
        return self.defence

    def getGameState(self):
        sys.exit(1)

    def getAllStats(self):
        if self.getHealthValue <= 0:
            print ("GAME OVER!\n")
            sys.exit(1)
        elif self.getHealthValue >= 1:
            return "health: {} - attack: {} - defence {}\n".format(self.health, self.attack,self.defence)

    def lvlup(self):
        print ("***   LEVEL UP   ***\n")
        randomNumHealth = random.randint(1, 9)
        randomNumAttack = random.randint(1, 3)
        randomNumDefence = random.randint(1, 3)
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumHealth):
            self.health += randomNumHealth
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumAttack):
            self.attack += randomNumAttack
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumDefence):
            self.defence += randomNumDefence
        self.getAllStats()
        
    def damageHealth(self):
        print ("spear incoming!\n")
        randomChance = random.randint(0,1)
        if randomChance == 1:
            print ("-----------> HIT!\n")
            randomNumDamage = random.randint(1, 10)
            print ("damage taken: {}!\n".format(randomNumDamage))
            self.setHealthValue(randomNumDamage)
            print (self.getAllStats())
        elif randomChance == 0:
            print ("---#|| MISS!\n")
        