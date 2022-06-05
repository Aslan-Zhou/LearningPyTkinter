from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *


def familyChanged(event):
    f=Font(family=familyVar.get())
    text.configure(font=f)


def weightChanged(event):
    f=Font(family=weightVar.get())
    text.configure(font=f)


def sizeSelected(event):
    f=Font(size=sizeVar.get())
    text.configure(font=f)


root = Tk()
root.title("17-9")
root.geometry("300x180")

toolbar = Frame(root, relief=RAISED, borderwidth=1)
toolbar.pack(side=TOP, pady=1, padx=2, fill=X)

familyVar = StringVar()
familyFamily = ("Arial", "Arial", "Times", "Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar, familyVar, *familyFamily, command=familyChanged)
family.pack(pady=2, side=LEFT)

weightVar = StringVar()
weightFamily = ("normal", "normal", "bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar, weightVar, *weightFamily, command=weightChanged)
weight.pack(pady=2, side=LEFT)

sizeVar = IntVar()
size = Combobox(toolbar, textvariable=sizeVar)
sizeFamily = [x for x in range(8, 30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>", sizeSelected)
size.pack(side=LEFT)

text = Text(root)
text.pack(fill=BOTH, expand=True, padx=3, pady=2)
text.focus_set()

if __name__ == '__main__':
    mainloop()
