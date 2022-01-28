from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")

root = Tk()
root.title("ch4-2")
label = Label(root)
button = Button(root,text="打印",command=msgShow)
label.pack()
button.pack()

mainloop()
