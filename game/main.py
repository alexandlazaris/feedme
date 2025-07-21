import time
import random
from enemy import EnemyClass
from player import PlayerClass
from file_manager import write_data, generate_graph

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
		write_data(p1)
		generate_graph(p1)
		p1.checkLvlUp()
		p1.checkHP()
		time.sleep(1)
