from tkinter import *

root = Tk()
root.title("ch19-")

canvas = Canvas(root)
canvas.pack()
id = canvas.create_oval(10, 50, 60, 100, fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)
if __name__ == '__main__':
    mainloop()
