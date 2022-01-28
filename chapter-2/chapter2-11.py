from tkinter import *
root = Tk()
root.title("ch2_11")
lable = Label(root, text="abcdefghijklmnopqrstuvwxyz",
              fg="blue",bg="lightyellow",
              wraplength=80,
              justify="center")
lable.pack()

root.mainloop()
