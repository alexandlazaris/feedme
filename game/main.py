import time
import random
from enemy import EnemyClass
from player import PlayerClass
from file_manager import write_data, generate_combined_graph

class StartGame(object):
	print(f"Welcome to Feed me, your RPG running in the command line.")
	print(f"The goal is to stay alive and outlive your enemy. Who is your enemy? Well that differs for each run.")
	print(f"Now, in order for your journey to begin, let's start with your name.")
	name_input = input("What is your name? ")
	
	player = PlayerClass(name_input, 10, 2, 2)
	print(f"Welcome {name_input} to your RPG! Before we begin, here are your starting stats.")
	player.print_stats()

	input("OK, let's take a look at your competitor. Press ENTER when you are ready.")
	enemy = EnemyClass(1,1,1)
	print(f"Well, well, well. Today you are facing ... {enemy.name}!")
	enemy.print_stats()
	input(f"Prepare yourself. Your life long battle with {enemy.name} is about to begin. Press ENTER to begin. Good luck.")
	while player.is_alive:
		print("Pondering next move ...")
		choice = random.randint(1,3)
		if choice == 1:
			print("Oooo, you found some XP. Keep collecting XP to level up & improve your stats.")
			player.add_xp()
			enemy.add_xp()
		elif choice == 2:
			print(f"Oh no, {enemy.name} appeared! WHACK!.")
			player.get_hit(enemy)
			player.check_hp()
		elif choice == 3:
			print("Phew nobody around, time to take a little rest & recover HP.")
			player.recover_hp()
			print("Moving on ...")
		else:
			print ("Something went wrong ... skipping turn.")
		write_data(player, enemy)
		player.add_turn()
		generate_combined_graph(player, enemy, file_name="rpg_radar.png")
		time.sleep(1)
