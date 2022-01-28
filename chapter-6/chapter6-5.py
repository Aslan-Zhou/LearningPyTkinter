from tkinter import *

def callbackW(*args):
    xL.set(xE.get())

def callbackR(*args):
    print("Warning:数据被读取！")

def hit():
    print("读取数据: ",xE.get())

root = Tk()
root.title("ch6-5")

xE = StringVar()
Entry(root,textvariable=xE).pack(
padx=10,pady=5)
xE.trace("w",callbackW)
xE.trace("r",callbackR)

xL = StringVar()
Label(root,textvariable=xL).pack(
padx=10,pady=5)
xL.set("同步显示")

Button(root,text="读取",command=hit).pack(pady=5)

mainloop()
