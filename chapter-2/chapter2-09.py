from tkinter import *

root = Tk()
root.title("ch2_9")
lable = Label(root, text= "abcdefghijklmnopqrstuvwxyz",
              fg="blue",bg="lightyellow",
              wraplength = 80)
lable.pack()

root.mainloop()
