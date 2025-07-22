import random
from datetime import datetime

class PlayerClass(object):
    "Create a player"

    level = 1
    total_xp = 10
    current_xp = 0
    xp_to_next_level = 0
    total_number_of_hits = 0
    max_hp = 0
    start_time = 0
    is_alive = False
    total_dmg_taken = 0

    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.xp_to_next_level += 5
        self.start_time = datetime.now().strftime("%d %b %y, %H:%M:%S")
        self.max_hp = hp
        self.is_alive = True

    def add_xp(self, addAmount):
        print(f"Gained {addAmount} exp")
        self.current_xp += addAmount
        self.total_xp += addAmount

    def print_stats(self):
        print(
            f"*** STATS ***\nNAME: {self.name}\nHP: {self.hp}\nATK: {self.attack}\nDEF: {self.defence}\nLEV: {self.level}\n*** ^ ^ ^ ***"
        )

    def checkLvlUp(self):
        if self.current_xp > self.xp_to_next_level:
            print("*** LEVEL UP ***")
            print(f"Total XP: {self.total_xp}")
            self.level += 1
            random_hp_increase = random.randint(1, 9)
            random_attack_increase = random.randint(1, 9)
            random_defence_increase = random.randint(1, 9)
            self.max_hp += random_hp_increase
            self.hp += random_hp_increase
            self.attack += random_attack_increase
            self.defence += random_defence_increase
            self.xp_to_next_level += 5
            self.current_xp = 0
            self.print_stats()

    def get_hit(self, damage):
        self.hp -= damage
        print(f"ouch! {damage} damage taken!")
        print(f"HP: {self.hp}")
        self.total_dmg_taken += damage
        self.total_number_of_hits += 1

    def print_hp(self):
        print(f"HP: {self.hp}")

    def recover_hp(self):
        self.hp += 1
        self.print_hp()

    def check_hp(self):
        if self.hp <= 0:
            print(f"{self.name} has no more HP. GAME OVER")
            self.is_alive = False

    # modify this to be time alive for the player in seconds
    def get_end_time(self):
        return datetime.now().strftime("%d %b %y, %H:%M:%S")
