from tkinter import *
import time

root = Tk()
root.title("ch19-17")

canvas = Canvas(root)
canvas.pack()
canvas.create_oval(10, 50, 60, 100, fill='yellow', outline='lightgray')

for x in range(0, 80):
    canvas.move(1, 5, 2)
    root.update()
    time.sleep(0.05)
if __name__ == '__main__':
    mainloop()
