from tkinter import *

root = Tk()
root.title("ch19-2")

canvas = Canvas(root, width=640, height=480)
canvas.pack()

canvas.create_line(100, 100, 500 ,100)
canvas.create_line(100, 125, 500, 125, width=5)
canvas.create_line(100, 150, 500, 150, width=10, fill="blue")
canvas.create_line(100, 175, 500, 175, dash=(10, 2, 2, 2))
if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("ch19-")

canvas = Canvas(root)

canvas.pack()

if __name__ == '__main__':
    mainloop()
