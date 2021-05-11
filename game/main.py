import time
import os
import random
from player import PlayerStart as newPlayerStart
import subprocess

class StartGame(object):
	'A player object with default fields'
	newPlayer = newPlayerStart("Alexander", 1, 1, 1)
	while True:
		newPlayer.lvlup()
		file = open("./game/player.dat", "w")
		file.truncate(0)
		file.write("@ Health,Attack,Defence\n")
		health = str(newPlayer.getHealthValue())
		attack = str(newPlayer.getAttackValue())
		defence = str(newPlayer.getDefenceValue())
		file.write(f"Stats,{health},{attack},{defence}")
		file.close()
		subprocess.call("clear", shell=True)
		subprocess.call("termgraph game/player.dat --color {blue,red,green} --title 'Let the games begin'", shell=True)
		time.sleep(3)
