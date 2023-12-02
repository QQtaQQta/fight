from tkinter import Tk, Canvas
from grid import Grid
import random
from hero import Hero
from sword import Sword
from bow import Bow

root = Tk()
canvas = Canvas(root, width=800, height=600)
canvas.pack()
grid = Grid(canvas)
grid.display()

fs = open('students.txt', 'r', encoding='utf-8')

students = []
for hero in fs:
    s = hero.split(';')
    id = int(s[0])
    name = s[1]
    var = int(s[2])
    group = 'ИП-22'
    gender = (s[4])
    students.append({'id': id, 'full_name': name, 'variant': var,
                     'gender': gender})

fs.close()

   
weapon_type = random.choice(['sword', 'bow'])
if weapon_type == 'sword':
    wp1 = Sword(canvas, weapon_type, 12)
else:
    wp1 = Bow(canvas, weapon_type, 12)

weapon_type = random.choice(['sword', 'bow'])
if weapon_type == 'sword':
    wp2 = Sword(canvas, 'sword', 12)
else:
    wp2 = Bow(canvas, 'bow', 12)


s1 = random.choice(students)
name = f"{s1['full_name'].split()[0]} {s1['full_name'].split()[1][0]} {s1['full_name'].split()[2][0]}"
p1 = Hero(canvas, name, 600, 500, s1['gender'], 100)
p1.setWeapon(wp1)

p1.display()


s2 = random.choice(students)
name = f"{s2['full_name'].split()[0]} {s2['full_name'].split()[1][0]} {s2['full_name'].split()[2][0]}"
p2 = Hero(canvas, name, 100, 500, s2['gender'], 100)
p2.setWeapon(wp2)
p2.display()
print (f"{p1.getName()} экипировал(а) {wp1._name}, {p2.getName()} экипировал(а) {wp2._name}")
while True:
    h1 = p1.attack (p2)
    #print(f"c помощью оружия {sword_name}!")
    print()
    if h1 <= 0:
        print (f"победил {p1.getName()}")
        break
    h2 = p2.attack (p1)
    #print(f"c помощью оружия {bow_name}!")
    print()
    if h2 <= 0:
        print (f"победил {p2.getName()}")
        break
    

    


root.mainloop()
