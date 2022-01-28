from tkinter import *

def callback(*args):
    xL.set(xE.get())
    print("data changed : ",xE.get())

root = Tk()
root.title("ch6-4")

xE = StringVar()
Entry(root,textvariable=xE).pack(
padx=10,pady=5)
xE.trace("w",callback)

xL = StringVar()
Label(root,textvariable=xL).pack(
padx=10,pady=5)
xL.set("同步显示")


mainloop()
