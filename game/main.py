import time
import random
from enemy import EnemyClass
from player import PlayerClass
from file_manager import write_data, generate_graph_type_one, generate_radar_graph_player, generate_radar_graph_enemy

class StartGame(object):
	'A player object with default fields'
	name_input = input("Before we begin, what is your name? ")
	print(f"Welcome {name_input} to your RPG!")
	player = PlayerClass(name_input, 10, 2, 1)
	enemy = EnemyClass(1,1,1)
	player.print_stats()
	while player.is_alive:
		print("Pondering next move ...")
		choice = random.randint(1,3)
		if choice == 1:
			print("Nice, I found some XP. I'll keep collecting these to level up.")
			player.add_xp(3)
			enemy.add_xp()
		elif choice == 2:
			print("A WILD ENEMY APPEARED! Hope it doesn't kill me.")
			player.get_hit(enemy.attack)
		elif choice == 3:
			print("Phew time for a little rest to recover HP.")
			player.recover_hp()
			print("Moving on ...")
		else:
			print ("Something went wrong ... skipping turn.")
		write_data(player)
		generate_graph_type_one(player)
		generate_radar_graph_player(player)
		generate_radar_graph_enemy(enemy)
		player.checkLvlUp()
		player.check_hp()
		time.sleep(1)
