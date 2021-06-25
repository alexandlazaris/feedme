import os
import random
from datetime import datetime
class PlayerClass(object): 
    'Create a player'
    
    healthLevel = 0
    attackLevel = 0
    defenceLevel = 0
    totalLvlUps = 0
    totalExp = 0
    currentExp = 0
    nextLvlExp = 0
    numberOfHits = 0
    maxHP = 0
    startTime = 0
    playerIsAlive = False
    totalDamageTaken = 0
    

    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.calculateNextLevelForExp()
        self.startTime = datetime.now().strftime("%d %b %y, %H:%M:%S")
        self.maxHP = health
        self.playerIsAlive = True
    
    def getName(self):
        return self.name
    
    def calculateNextLevelForExp(self):
        self.nextLvlExp += 5
    
    def addExp(self, addAmount):
        print (f"Gained {addAmount} exp")
        self.currentExp += addAmount
        self.totalExp += addAmount

    def getTotalExp(self):
        return self.totalExp
    
    def getCurrentExp(self):
        return self.currentExp
        
    def getNextLvlExp(self):
        return self.nextLvlExp

    def resetCurrentExp(self):
        self.currentExp = 0

    def getCurrentLevel(self):
        return self.totalLvlUps

    def getMaxHP(self):
        return self.maxHP

    def getHealthValue(self):
        return self.health
    
    def getAttackValue(self):
        return self.attack

    def getDefenceValue(self):
        return self.defence

    def printAllStats(self):
        print (f"{self.name} stats:\nHP: {self.getHealthValue()}\nAttack: {self.getAttackValue()}\nDefence: {self.getDefenceValue()}")

    def gainExp(self):
        self.addExp(3)

    def checkLvlUp(self):
        if self.getCurrentExp() > self.getNextLvlExp():
            print ("*** LEVEL UP ***")
            print (f"Total XP: {self.getTotalExp()}")
            self.totalLvlUps += 1
            randomNumHealth = random.randint(1,9)
            randomNumAttack = random.randint(1,9)
            randomNumDefence = random.randint(1,9)
            self.healthLevel += 1
            self.maxHP += randomNumHealth
            self.health += randomNumHealth
            self.attack += randomNumAttack
            self.attackLevel += 1
            self.defence += randomNumDefence
            self.defenceLevel += 1
            self.calculateNextLevelForExp()
            print (f"Next lvl up: {self.getNextLvlExp()}")
            self.resetCurrentExp()
            self.printAllStats()
    
    def getHit(self, damageTaken):
        self.health -= damageTaken
        print (f"Ouch! {damageTaken} damage taken!")
        print (f"HP: {self.getHealthValue()}")
        self.totalDamageTaken += damageTaken
        self.numberOfHits += 1

    def getTotalDamageTaken(self):
        return self.totalDamageTaken
    
    def printHealth(self):
        print (f"HP: {self.getHealthValue()}")

    def getNumberOfHits(self):
        return self.numberOfHits
    
    def recoverHealth(self):
        self.health += 1
        self.printHealth()
        
    def checkHP(self):
        if self.getHealthValue() <= 0:
            print (f"{self.getName()} has no more HP. GAME OVER")
            self.playerIsAlive = False

    def getPlayerAliveBool(self):
        return self.playerIsAlive

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return datetime.now().strftime("%d %b %y, %H:%M:%S")
