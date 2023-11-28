from human import Human
from tkinter import Tk, Canvas, Frame, BOTH, W
import random


class Student(Human):
    def __init__(self, canvas, name, x, y, gender, gr, var):
        super().__init__(canvas, name, x, y, gender)
        self.group = gr
        self.variant = var

    def _DrawName(self):
        self.canvas.create_text(self.x + 15.5, self.y - 220,
        text=f'{self._name}, {self.group}, №{self.variant}',
        font="Arial", anchor=W, fill="black")









