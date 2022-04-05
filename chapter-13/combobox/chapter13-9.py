from tkinter import *
from tkinter.ttk import *


def printSelection():
    print("The selection is : ", var.get())


root = Tk()
root.title("ch13-9")
root.geometry("300x120")

var = StringVar()
cb = Combobox(root, textvariable=var)
cb["values"] = ("Python", "Java", "C#", "C")
cb.current(0)
cb.pack(pady=10)

Button(root, text="Print", command=printSelection
       ).pack(pady=10, anchor=S, side=BOTTOM)
if __name__ == '__main__':
    mainloop()
