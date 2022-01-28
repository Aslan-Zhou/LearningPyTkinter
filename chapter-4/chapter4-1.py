from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"

root = Tk()
root.title("ch4-1")
root.geometry("200x200")
label = Label(root)
button = Button(root,text="打印",command=msgShow)
label.place(x=55,y=40)
button.place(x=80,y=120)

mainloop()
