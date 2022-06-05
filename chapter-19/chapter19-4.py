from tkinter import *

root = Tk()
root.title("ch19-4")

canvas = Canvas(root, width=640, height=480)
canvas.pack()

canvas.create_line(30, 30, 500, 30, width=10, capstyle=ROUND)
canvas.create_line(30, 130, 500, 130, width=10, capstyle=BUTT)
canvas.create_line(30, 230, 500, 230, width=10, capstyle=PROJECTING)

canvas.create_line(30, 20, 30, 240)
canvas.create_line(500, 20, 500, 250)
if __name__ == '__main__':
    mainloop()
