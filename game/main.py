import time
import datetime
import os
import random
from player import PlayerStart as newPlayerStart
import subprocess

class StartGame(object):
	'A player object with default fields'
	newPlayer = newPlayerStart("Alexander", 1, 1, 1)
	startTime = datetime.datetime.now()
	while True:
		newPlayer.lvlup()
		health = str(newPlayer.getHealthValue())
		attack = str(newPlayer.getAttackValue())
		defence = str(newPlayer.getDefenceValue())
		healthLevel = str(newPlayer.healthLevel)
		attackLevel = str(newPlayer.attackLevel)
		defenceLevel = str(newPlayer.defenceLevel)

		file = open(f"./game/gameData-{startTime}.txt", "w")
		file.truncate(0)
		file.write(f"Health,{healthLevel},{health}\n")
		file.write(f"Attack,{attackLevel},{attack}\n")
		file.write(f"Defence,{defenceLevel},{defence}")
		file.close()

		subprocess.call("clear", shell=True)
		subprocess.call("termgraph game/gameData.txt --color {green,yellow}", shell=True)
		print(f"Lvl up has been called {str(newPlayer.totalLvlUps)} times")
		time.sleep(3)
