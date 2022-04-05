from tkinter import *


def print_Into():
    selection = ''
    for i in checkboxes:
        if checkboxes[i].get():
            selection = selection + sports[i] + "\t"
    print(selection)


root = Tk()
root.title("ch8-8")
root.geometry("400x240")
labelFrame = LabelFrame(root, text="请选择喜欢的运动")

sports = {0: "美式足球", 1: "棒球", 2: "篮球", 3: "网球"}
checkboxes = {}
for j in range(len(sports)):
    checkboxes[j] = BooleanVar()
    Checkbutton(labelFrame, text=sports[j], variable=checkboxes[j]).grid(row=j + 1, sticky=W)
labelFrame.pack(ipadx=5, ipady=5, pady=10)
Button(root, text="确定", width=10, command=print_Into).pack()
mainloop(0)
