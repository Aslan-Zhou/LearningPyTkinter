from tkinter import *
import time

root = Tk()
root.title("ch19-18")

canvas = Canvas(root, width=500, height=250)
canvas.pack()
id1 = canvas.create_oval(10, 50, 60, 100, fill='yellow', outline='lightgray')
id2 = canvas.create_oval(10, 150, 60, 200, fill='blue', outline='lightgray')

for x in range(0, 80):
    canvas.move(id1, 5, 0)
    canvas.move(id2, 5, 0)
    root.update()
    time.sleep(0.05)
if __name__ == '__main__':
    mainloop()
