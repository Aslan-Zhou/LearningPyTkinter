from tkinter import *

root = Tk()
root.title("ch19-8")

canvas = Canvas(root, width=640, height=480)
canvas.pack()

canvas.create_arc(10, 10, 110, 110, extent=45, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=90, style=ARC)
canvas.create_arc(410, 10, 510, 110, extent=180, fill='yellow')
canvas.create_arc(10, 110, 110, 210, extent=270, style=ARC)
canvas.create_arc(210, 110, 310, 210, extent=359, style=ARC, width=5)

canvas.create_arc(10, 250, 310, 350, extent=90, style=ARC, start=90)
canvas.create_arc(320, 250, 620, 350, extent=180, style=ARC)
canvas.create_arc(10, 360, 310, 460, extent=270, style=ARC, outline='blue')
canvas.create_arc(320, 360, 620, 460, extent=359, style=ARC)

if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("ch19-")

canvas = Canvas(root)
canvas.pack()

if __name__ == '__main__':
    mainloop()
