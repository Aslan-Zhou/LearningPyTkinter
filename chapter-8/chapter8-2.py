from tkinter import *

root = Tk()
root.title("ch8-2")

frames = {"red":"cross","green":"clock","blue":"boat"}
for frame in frames:
    Frame(root,bg=frame,cursor=frames[frame],
          height=50,width=200).pack(side=LEFT)

mainloop()
