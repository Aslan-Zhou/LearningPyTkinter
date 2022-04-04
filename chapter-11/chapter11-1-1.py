from tkinter import *


def python_Clicked():
    if var_Python.get():
        label.config(text="Select Python")
    else:
        label.config(text="Unselect Python")


def java_Clicked():
    if var_Java.get():
        label.config(text="Select Java")
    else:
        label.config(text="Unselect Java")


def button_Clicked(event):
    label.config(text="Button Clicked")


root = Tk()
root.title("ch11-1-1")
root.geometry("300x180")
button = Button(root, text="Click me")
button.pack(anchor=W)
button.bind("<Button-1>", button_Clicked)

var_Python = BooleanVar()
Checkbutton(root, text="Python", variable=var_Python,
            command=python_Clicked).pack(anchor=W)
var_Java = BooleanVar()
Checkbutton(root, text="Java", variable=var_Java,
            command=java_Clicked).pack(anchor=W)
label = Label(root, bg="yellow", fg="blue", height=2,
              width=12, font="Times 16 bold")
label.pack()

mainloop()
