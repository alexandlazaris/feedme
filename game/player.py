from datetime import datetime
from faker import Faker
from enemy import EnemyClass
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
        self.xp_to_next_level = 5
        self.start_time = datetime.now().strftime("%d %b %y, %H:%M:%S")
        self.max_hp = hp
        self.is_alive = True

    def add_xp(self):
        xp_gain = fake.random_int(1,9)
        self.current_xp += xp_gain
        self.total_xp += xp_gain
        if self.current_xp > self.xp_to_next_level:
            self.level_up()
            self.current_xp = 0
            self.print_stats()

    def print_stats(self):
        print(
            f"*** STATS ***\nNAME: {self.name}\nHP: {self.hp}\nATK: {self.attack}\nDEF: {self.defence}\nLEV: {self.level}\nNEXT LEVEL: {self.xp_to_next_level} XP\n*** ^ ^ ^ ***"
        )
    
    def level_up(self):
        print("*** LEVEL UP ***")
        hp_increase = fake.random_digit_not_null()
        self.hp += hp_increase
        self.max_hp = hp_increase
        self.attack += fake.random_digit_not_null()
        self.defence += fake.random_digit_not_null()
        self.xp_to_next_level += 5
        self.level += 1

    def get_hit(self, enemy: EnemyClass):
        scaled_atk = enemy.attack * (1 + 0.05 * enemy.level)
        scaled_def = self.defence * (1 + 0.04 * self.level)
        damage = int(scaled_atk * (scaled_atk / (scaled_atk + scaled_def)))

        self.hp -= damage
        print(f"Ouch! {damage} damage taken! {self.hp} HP remaining.")
        self.total_dmg_taken += damage
        self.total_number_of_hits += 1

    def recover_hp(self):
        hp_recovered= fake.random_int(1, 5)
        self.hp += hp_recovered
        print(f"Recovered {hp_recovered} HP, now at {self.hp}")

    def check_hp(self):
        if self.hp <= 0:
            print(f"{self.name} has no more HP. GAME OVER")
            self.is_alive = False

    def add_turn(self):
        self.turns_taken += 1

    def get_turns(self):
        print(f"You have survived {self.turns_taken}.")

    # TODO: modify this to be time alive for the player in seconds
    def get_end_time(self):
        return datetime.now().strftime("%d %b %y, %H:%M:%S")