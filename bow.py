from tkinter import Tk, Canvas
from weapon import Weapon

class Bow(Weapon):

    def __init__(self, c, n, d):
        self._canvas = c
        self._baseDamage = d
        self._name = n

    def display(self, x, y):
        self._canvas.create_arc(x - 60, y - 80, x + 60, y + 80, start=270, extent=180, width=3, outline='green')




        pass
 