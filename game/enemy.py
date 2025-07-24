from faker import Faker
fake = Faker()

class EnemyClass(object):
    'Enemy object'
    hp = 0
    max_hp = 0
    attack = 0
    defence = 0
    current_xp = 0
    xp_to_next_level = 0
    total_xp = 0
    level = 1
    specialty = fake.catch_phrase()

    def __init__(self, hp, attack, defence): 
        self.name = fake.name()
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.xp_to_next_level = 5

    def print_stuff(self):
        print (fake.random_digit_above_two())
    
    def level_up(self):
        hp_increase = fake.random_digit_not_null()
        self.hp += hp_increase
        self.max_hp = hp_increase
        self.attack += fake.random_digit_not_null()
        self.defence += fake.random_digit_not_null()
        self.xp_to_next_level += 5
        self.level += 1
        
    def add_xp(self):
        xp_gain = fake.random_int(1,9)
        self.current_xp += xp_gain
        self.total_xp += xp_gain
        if self.current_xp > self.xp_to_next_level:
            print("*** ENEMY LEVEL UP ***")
            self.level_up()
            self.current_xp = 0
            self.print_stats()

    def print_stats(self):
        print(
            f"*** STATS ***\nNAME: {self.name}\nHP: {self.hp}\nATK: {self.attack}\nDEF: {self.defence}\nLEV: {self.level}\nNEXT LEVEL: {self.xp_to_next_level} XP\n*** ^ ^ ^ ***"
        )