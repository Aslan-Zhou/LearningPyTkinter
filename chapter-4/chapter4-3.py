from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")

root = Tk()
root.title("ch4-3")
label = Label(root)
button1 = Button(root,text="打印",width=15,command=msgShow)
button2 = Button(root,text="结束",width=15,command=root.destroy)
label.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)

mainloop()
