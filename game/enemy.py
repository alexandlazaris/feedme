import os
import random


class EnemyClass(object):
    'Enemy object'

    def __init__(self, name): 
        self.name = name
        self.health = random.randint(1,9)
        self.attack = random.randint(1,9)
        self.defence = random.randint(1,9)

    def getAttack(self):
        return self.attack


    def getName(self):
        return self.name
