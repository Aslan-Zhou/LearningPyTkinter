from tkinter import *

root = Tk()
root.title("ch19-9")

canvas = Canvas(root, width=640, height=480)
canvas.pack()

canvas.create_arc(10, 10, 110, 110, extent=180, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=180, style=CHORD)
canvas.create_arc(410, 10, 510, 110, extent=120, style=PIESLICE, start=30)
if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("ch19-")

canvas = Canvas(root)
canvas.pack()

if __name__ == '__main__':
    mainloop()
