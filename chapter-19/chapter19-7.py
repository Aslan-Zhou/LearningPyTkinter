from tkinter import *

root = Tk()
root.title("ch19-7")

canvas = Canvas(root, width=640, height=480)
canvas.pack()
canvas.create_rectangle(10, 10, 120, 60, fill='red')
canvas.create_rectangle(130, 10, 200, 80, fill='yellow', outline="blue")
canvas.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')
if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("ch19-")

canvas = Canvas(root)
canvas.pack()

if __name__ == '__main__':
    mainloop()
