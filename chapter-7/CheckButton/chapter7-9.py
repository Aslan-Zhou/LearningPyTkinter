from tkinter import *

def sel_ALL():
    entry.select_range(0,END)
def delete_Sel():
    entry.select_clear()
def clear():
    entry.delete(0,END)
def readonly():
    if var.get():
        entry.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)

root = Tk()
root.title("ch7-9")

entry = Entry(root)
entry.grid(row=0,column=0,columnspan=4,
           padx=5,pady=5,sticky=W)
# row = 1 建立 Button
Button(root,text="选取",command=sel_ALL).grid(
    row=1,column=0,padx=5,pady=5,sticky=W)
Button(root,text="取消选取",command=delete_Sel).grid(
    row=1,column=1,padx=5,pady=5,sticky=W)
Button(root,text="删除",command=clear).grid(
    row=1,column=2,padx=5,pady=5,sticky=W)
Button(root,text="结束",command=root.destroy).grid(
    row=1,column=3,padx=5,pady=5,sticky=W)
# row = 2 建立 CheckBoxes、
var = BooleanVar()
var.set(False)

Checkbutton(root,text="只读",variable=var,
            command=readonly).grid(row=2,column=0)

mainloop(0)
