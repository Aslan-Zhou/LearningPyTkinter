from tkinter import *

root = Tk()
root.title("ch2_12")
lable = Label(root, text="abcdefghijklmnopqrstuvwxyz",
              fg="blue",bg="lightyellow",
              wraplength=80,
              justify="right")
lable.pack()

root.mainloop()
