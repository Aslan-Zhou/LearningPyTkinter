from tkinter import *

def callback(name,index,mode):
    xL.set(xE.get())
    print("name = %r, index = %r, mode = %r" % (name,index,mode))

root = Tk()
root.title("ch6-6")

xE = StringVar()
Entry(root,textvariable=xE).pack(
padx=10,pady=5)
xE.trace("w",callback)

xL = StringVar()
Label(root,textvariable=xL).pack(
padx=10,pady=5)
xL.set("同步显示")


mainloop()
