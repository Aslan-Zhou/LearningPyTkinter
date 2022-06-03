from tkinter import *

root = Tk()
root.title("ch19-5")

canvas = Canvas(root, width=640, height=480)
canvas.pack()

canvas.create_line(30, 30, 500, 30, width=10, stipple="gray25")
canvas.create_line(30, 130, 500, 130, width=40, stipple="questhead")
canvas.create_line(30, 230, 500, 230,width=10, stipple="info")

if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("ch19-")

canvas = Canvas(root)
canvas.pack()

if __name__ == '__main__':
    mainloop()
