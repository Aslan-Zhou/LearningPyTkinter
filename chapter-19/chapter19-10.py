from tkinter import *

root = Tk()
root.title("ch19-10")

canvas = Canvas(root, width=640, height=480)
canvas.pack()
canvas.create_oval(10, 10, 110, 110)
canvas.create_oval(150, 10, 300, 160, fill='yellow')

canvas.create_oval(10, 200, 310, 350)
canvas.create_oval(350, 200, 550, 300, fill="aqua", outline='blue', width=5)
if __name__ == '__main__':
    mainloop()
