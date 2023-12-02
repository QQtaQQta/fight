from tkinter import Tk, Canvas
from random import randrange
import random
sword_names = ['Небесная ярость', 'Проклятый меч берсерка', 'Похититель душ']
bow_names = ['Короткий лук Гезена', 'Лук Банши', 'Лук эльфийского двора']

class Weapon():

    def __init__(self, c, weapon_type, d):
        self._canvas = c
        self._baseDamage = d
       
        if weapon_type == 'sword':
            self._name = random.choice(sword_names)
        elif weapon_type == 'bow':
            self._name = random.choice(bow_names)

    def display(self, x, y):
        pass
    
    def GetWname(self):
        return self._name
        
    def hit(self):
        damage = randrange(self._baseDamage-5, self._baseDamage+5)
        return damage
