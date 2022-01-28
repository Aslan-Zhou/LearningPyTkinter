from tkinter import *

def printSelection():
    num = var.get()
    if num == 1:
        label.config(text="你是男生")
    else:
        label.config(text="你是女生")

root = Tk()
root.title("ch7-1")

var = IntVar()
var.set(1)

label = Label(root,text="这是预设，尚未选择",bg="yellow",width=30)
label.pack()
radiobutton_man = Radiobutton(root,text="男生",
                              variable=var,value=1,
                              command=printSelection)
radiobutton_man.pack()

radiobutton_woman = Radiobutton(root,text="女生",
                              variable=var,value=2,
                              command=printSelection)
radiobutton_woman.pack()

mainloop(0)
