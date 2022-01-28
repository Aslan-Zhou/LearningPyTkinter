from tkinter import *

root = Tk()
root.title("ch7-7")
Label(root,text="请选择喜欢的运动",bg="yellow",
              fg="blue",width=30).grid(row=0)
var1 = IntVar()
Checkbutton(root,text="美式足球",variable=var1).grid(row=1,sticky=W)
var2 = IntVar()
Checkbutton(root,text="棒球",variable=var2).grid(row=2,sticky=W)
var3 = IntVar()
Checkbutton(root,text="篮球",variable=var3).grid(row=3,sticky=W)

mainloop(0)
