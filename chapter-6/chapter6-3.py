from tkinter import *

def callback(*args):
    print("data changed : ",xE.get())

root = Tk()
root.title("ch6-3")

xE = StringVar()
entry = Entry(root,textvariable=xE).pack(
padx=10,pady=5)
xE.trace("w",callback)

mainloop()
