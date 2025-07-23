from datetime import datetime
from faker import Faker
fake = Faker()

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
    turns_taken = 0

    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.xp_to_next_level += 5
        self.start_time = datetime.now().strftime("%d %b %y, %H:%M:%S")
        self.max_hp = hp
        self.is_alive = True

    def add_xp(self):
        xp_gain = fake.random_digit_not_null()
        self.current_xp += xp_gain
        self.total_xp += xp_gain
        if self.current_xp > self.xp_to_next_level:
            print("*** LEVEL UP ***")
            self.level_up()
            self.current_xp = 0
            self.print_stats()

    def print_stats(self):
        print(
            f"*** STATS ***\nNAME: {self.name}\nHP: {self.hp}\nATK: {self.attack}\nDEF: {self.defence}\nLEV: {self.level}\n*** ^ ^ ^ ***"
        )
    
    def level_up(self):
        hp_increase = fake.random_digit_not_null()
        self.hp += hp_increase
        self.max_hp = hp_increase
        self.attack += fake.random_digit_not_null()
        self.defence += fake.random_digit_not_null()
        self.xp_to_next_level = 10
        self.level += 1

    def get_hit(self, enemy_damage):
        hit_damage = int(((enemy_damage / 2) - (self.defence / 2) + 2) * 0.5 + 1)
        self.hp -= hit_damage
        print(f"Ouch! {hit_damage} damage taken! {self.hp} HP remaining.")
        self.total_dmg_taken += hit_damage
        self.total_number_of_hits += 1

    def print_hp(self):
        print(f"Recovered {self.hp} HP")

    def recover_hp(self):
        self.hp += 1
        self.print_hp()

    def check_hp(self):
        if self.hp <= 0:
            print(f"{self.name} has no more HP. GAME OVER")
            self.is_alive = False

    def get_turns(self):
        print(f"You have survived {self.turns_taken}.")

    # TODO: modify this to be time alive for the player in seconds
    def get_end_time(self):
        return datetime.now().strftime("%d %b %y, %H:%M:%S")