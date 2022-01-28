from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")

root = Tk()
root.title("ch4-8")
sun = PhotoImage(file="sun.gif")
label = Label(root)
button = Button(root,image=sun,command=msgShow,
                text="Click Me",compound=CENTER)
label.pack()
button.pack()

mainloop()
