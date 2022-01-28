from tkinter import *

root = Tk()
root.title("ch8-1")

for frame in ["red","green","blue"]:
    Frame(root,bg=frame,height=50,width=250).pack()

mainloop()
