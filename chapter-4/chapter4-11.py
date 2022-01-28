from tkinter import *

def msgShow():
    label.config(text="Hello world",bg="lightyellow",
                 fg="blue",font="Helvetic 20 bold")

root = Tk()
root.title("ch4-11")
sun = PhotoImage(file="sun.gif")
label = Label(root)
button = Button(root,image=sun,command=msgShow,
                cursor="star")
label.pack()
button.pack()

mainloop()
