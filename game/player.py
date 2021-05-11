import os
import random

class PlayerStart(object): 
    'Create a player'
    
    healthLevel = 0
    attackLevel = 0
    defenceLevel = 0
    totalLvlUps = 0
    
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

    def getDefence(self):
        return "defence: ", self.defence

    def getDefenceValue(self):
        return self.defence

    def getAllStats(self):
        return "health: ", self.health, "attack: ", self.attack, "defence: ", self.defence

    def getNumberOfLevelUps():
        return totalLvlUps

    def lvlup(self):
        print ("*** LEVEL UP ***")
        self.totalLvlUps += 1
        randomNumHealth = random.randint(1,9)
        randomNumAttack = random.randint(1,9)
        randomNumDefence = random.randint(1,9)
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumHealth):
            self.health += randomNumHealth
            self.healthLevel += 1
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumAttack):
            self.attack += randomNumAttack
            self.attackLevel += 1
        if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumDefence):
            self.defence += randomNumDefence
            self.defenceLevel += 1
        
