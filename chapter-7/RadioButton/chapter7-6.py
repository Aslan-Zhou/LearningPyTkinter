from tkinter import *

def printSelection():
    label.config(text=("你选的是："+str(var.get())))

root = Tk()
root.title("ch7-6")
image_Star = PhotoImage(file="star.png")
image_Moon = PhotoImage(file="moon.png")
image_Sun = PhotoImage(file="sun.png")
var = IntVar()
var.set(1)

label = Label(root,text="这是默认值，尚未选择",bg="yellow",
              fg="blue",width=30)
label.pack()

Radiobutton(root,image=image_Star,
            text="星星",compound=RIGHT,
            variable=var,value=1,
            command=printSelection).pack()
Radiobutton(root,image=image_Moon,
            text="月亮",compound=RIGHT,
            variable=var,value=2,
            command=printSelection).pack()
Radiobutton(root,image=image_Sun,
            text="太阳",compound=RIGHT,
            variable=var,value=3,
            command=printSelection).pack()

mainloop(0)
