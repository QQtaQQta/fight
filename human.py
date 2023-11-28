from tkinter import Tk, Canvas, Frame, BOTH, W

class Human:
    def __init__(self, canvas, name, x, y, gender):
        self.canvas = canvas
        self._name = name
        self.x = x
        self.y = y
        self.gender = gender

    def getName(self):
        return self._name
    
    def display(self):
        self._DrawName()
        self._DrawHead()
        self._DrawBody()
        self._DrawLeggs()
        self._DrawHands()
        self._DrawFace()
        self._DrawName()
        self._DrawName()

        if self.gender == "ж":
            self._DrawPigtails()
        elif self.gender == "м":
            self._DrawHair()


    def _DrawName(self):
        self.canvas.create_text(self.x + 1.5, self.y - 270, text=self._name, font="Times 18", anchor=W, fill="black")

    def _DrawHead(self):
        self.canvas.create_oval(self.x+20, self.y-200, self.x+80, self.y-140, width=2) 
        
    def _DrawBody(self):
        self.canvas.create_line(self.x+50,self.y-50,self.x+50,self.y-140,width=2)
        
    def _DrawLeggs(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width=2)
        
    def _DrawHands(self):
        self.canvas.create_line(self.x, self.y-140, self.x+50, self.y-100,self.x+100, self.y-140, width=2)
        
    def _DrawFace(self):
        self.canvas.create_oval(self.x+35, self.y-185, self.x+45, self.y-175, width=5, outline="light green", fill="black")
        self.canvas.create_oval(self.x+55, self.y-185, self.x+65, self.y-175, width=5, outline="light green", fill="black")
        self.canvas.create_arc(self.x+30, self.y-190, self.x+70, self.y-150, start=0, extent=-180, outline="red", width=2)

    def _DrawHair(self):
        self.canvas.create_line(self.x + 35, self.y - 205, self.x + 35, self.y - 195, width=2)
        self.canvas.create_line(self.x + 50, self.y - 210, self.x + 50, self.y - 200, width=2)
        self.canvas.create_line(self.x + 65, self.y - 205, self.x + 65, self.y - 195, width=2)

    def _DrawPigtails(self):
        self.canvas.create_line(self.x, self.y - 100, self.x + 20, self.y - 175, width=2, fill='brown')
        self.canvas.create_line(self.x + 100, self.y - 100, self.x + 80, self.y - 175, width=2, fill='brown')
        self.canvas.create_line(self.x + 33, self.y - 100, self.x + 40, self.y - 142, width=2, fill='brown')
        self.canvas.create_line(self.x + 64, self.y - 100, self.x + 58, self.y - 142, width=2, fill='brown')
