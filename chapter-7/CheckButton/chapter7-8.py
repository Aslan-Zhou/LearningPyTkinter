from tkinter import *

def printInto():
    selection = ''
    for i in checkboxes:
        if checkboxes[i].get():
            selection = selection + sports[i] + "\t"
    print(selection)
root = Tk()
root.title("ch7-8")
Label(root,text="请选择喜欢的运动",bg="yellow",
              fg="blue",width=30).grid(row=0)
sports = {0:"美式足球",1:"棒球",2:"篮球",3:"网球"}
checkboxes = {}
for j in range(len(sports)):
    checkboxes[j] = BooleanVar()
    Checkbutton(root,text=sports[j],variable=checkboxes[j]).grid(row=j+1,sticky=W)

Button(root,text="确定",width=10,command=printInto).grid(row=j+1)
mainloop(0)
