from tkinter import *

def printSelection():
    label.config(text="你是"+var.get())


root = Tk()
root.title("ch7-2")

var = StringVar()
var.set("男生")

label = Label(root,text="这是预设，尚未选择",bg="yellow",width=30)
label.pack()
radiobutton_man = Radiobutton(root,text="男生",
                              variable=var,value="男生",
                              command=printSelection)
radiobutton_man.pack()

radiobutton_woman = Radiobutton(root,text="女生",
                              variable=var,value="女生",
                              command=printSelection)
radiobutton_woman.pack()

mainloop(0)
