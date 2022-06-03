from tkinter import *
from random import *

root = Tk()
root.title("ch19-6")

canvas = Canvas(root, width=640, height=480)
canvas.pack()

for i in range(100):
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2:
        x1, x2, = x2, x1
    if x1 > x2:
        x1, x2, = x2, x1
    canvas.create_rectangle(x1, y1, x2, y2)
if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("ch19-")

canvas = Canvas(root)
canvas.pack()

if __name__ == '__main__':
    mainloop()
