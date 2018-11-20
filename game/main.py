import os
import random
import player

class StartGame(object):
	'A player object with default fields'

	newPlayer = player.PlayerStart("Alexander", 5, 1, 1)
	print (newPlayer.getAllStats())
	newPlayer.lvlup()	
	print (newPlayer.getAllStats())
