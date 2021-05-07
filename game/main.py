import time
import os
import random
from player import PlayerStart as newPlayerStart

class StartGame(object):
	'A player object with default fields'
	newPlayer = newPlayerStart("Alexander", 5, 1, 1)
	while True:
		newPlayer.lvlup()
		print (newPlayer.getAllStats())
		time.sleep(3)
