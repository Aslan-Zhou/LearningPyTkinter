from tkinter import *

root = Tk()
root.title("ch2_10")
lable = Label(root, text= "abcdefghijklmnopqrstuvwxyz",
              fg="blue",bg="lightyellow",
              wraplength=80,
              justify = "left")
lable.pack()

root.mainloop()
