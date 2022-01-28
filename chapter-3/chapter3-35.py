from tkinter import *

root = Tk()
root.title("ch3-35")
Colors = ["red","orange","yellow","green","blue","purple"]

n = 0
for color in Colors:
    Label(root,text=color,relief="groove",width=20).grid(row=n,column=0)
    Label(root,bg=color,relief="ridge",width=20).grid(row=n,column=1)
    n += 1

root.mainloop()
