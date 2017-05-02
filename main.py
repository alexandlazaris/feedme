import os
import random

class Player(object):
	'A player object with default fields'

	def __init__(self, name, health, attack, defence):
		self.name = name
		self.health = health
		self.attack = attack
		self.defence = defence
		print("life created")
		#hunger = 0
		#hungry = False

	def displayStats(self):
		print ("~~~~~~~~~~")
		print ("name:", self.name)
		print ("health:", self.health)
		print ("attack:", self.attack)
		print ("defence:",self.defence)
		print ("~~~~~~~~~~")
		Player.prompt(self)

	def prompt(self):
		choice = input("what to do ")
		if int(choice) == 1:
			Player.lvlup(self)
		else:
			print("nothing to do")

	def lvlup(self):
		print("***LEVEL UP***")
		randomNumHealth = random.randint(1,9)
		randomNumAttack = random.randint(1,9)
		randomNumDefence = random.randint(1,9)
		if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumHealth):
			print("health++")
			self.health += randomNumHealth
		if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumAttack):
			print("attack++")
			self.attack += randomNumAttack
		if (max(randomNumHealth, randomNumAttack, randomNumDefence) == randomNumDefence):
			print("defence++")
			self.defence += randomNumDefence
		Player.displayStats(self)




player1 = Player("Alexander", 10, 4, 6)
player1.displayStats()