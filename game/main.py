import time
import os
import random
import subprocess
# from <file/directory> import <class>
from enemy import EnemyClass
from player import PlayerClass

class StartGame(object):
	'A player object with default fields'
	playerName = input("Before we begin, what is your name? ")
	print(f"Welcome {playerName}, let's begin!")
	print ("Start game!")
	p1 = PlayerClass(playerName, 5, 2, 1)
	e2 = EnemyClass("Baddie")
	p1.printAllStats()
	while p1.getPlayerAliveBool():
		print("Pondering next move ...")
		choice = random.randint(1,3)
		print("Moving on ...")
		if choice == 1:
			print("Nice! Found some XP.")
			p1.gainExp()
		elif choice == 2:
			print("A WILD ENEMY APPEARED!")
			p1.getHit(e2.getAttack())
		elif choice == 3:
			print("Phew nothing here, take a little rest to recover HP.")
			p1.recoverHealth()
		else:
			print ("No options detected, something wrong.")
		p1.checkLvlUp()
		health = str(p1.getMaxHP())
		attack = str(p1.getAttackValue())
		defence = str(p1.getDefenceValue())
		healthLevel = str(p1.healthLevel)
		attackLevel = str(p1.attackLevel)
		defenceLevel = str(p1.defenceLevel)
		file = open(f"./game/gameData.txt", "w")
		file.truncate(0)
		file.write(f"Player: {p1.getName()}\n")
		file.write(f"Max HP: {health}\n")
		file.write(f"Total lvls: {p1.getCurrentLevel()}\n")
		file.write(f"Total XP: {p1.getTotalExp()}\n")
		file.write(f"Total damage taken: {p1.getTotalDamageTaken()}\n")
		file.write(f"Hits taken: {p1.getNumberOfHits()}\n")
		file.write(f"Start time: {p1.getStartTime()}\n")
		file.write(f"End time: {p1.getEndTime()}")
		file.close()
		p1.checkHP()
		time.sleep(3)
