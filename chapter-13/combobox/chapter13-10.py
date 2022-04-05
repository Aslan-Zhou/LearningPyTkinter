from tkinter import *
from tkinter.ttk import *


def comboSelection(event):
    labelVar.set(var.get())


root = Tk()
root.title("ch13-10")
root.geometry("300x120")

var = StringVar()
cb = Combobox(root, textvariable=var)
cb["values"] = ("Python", "Java", "C#", "C")
cb.current(0)
cb.bind("<<ComboboxSelected>>", comboSelection)
cb.pack(side=LEFT, padx=10, pady=10)

labelVar = StringVar()
Label(root, textvariable=labelVar).pack(side=LEFT)
labelVar.set(var.get())
if __name__ == '__main__':
    mainloop()
