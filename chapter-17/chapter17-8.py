from tkinter import *
from tkinter.font import Font


def familyChanged(event):
    f=Font(family=familyVar.get())
    text.configure(font=f)


def weightChanged(event):
    f=Font(family=weightVar.get())
    text.configure(font=f)


root = Tk()
root.title("17-8")
root.geometry("300x180")

toolbar = Frame(root, relief=RAISED, borderwidth=1)
toolbar.pack(side=LEFT, pady=1, padx=2, fill=X)

familyVar = StringVar()
familyFamily = ("Arial", "Times", "Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar, familyVar, *familyFamily, command=familyChanged)
family.pack(pady=2)

weightVar = StringVar()
weightFamily = ("normal", "bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar, weightVar, *weightFamily, command=weightChanged)
weight.pack(pady=2)

text = Text(root)
text.pack(fill=BOTH, expand=True, padx=3, pady=2)
text.focus_set()

if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("17-")

text = Text(root)
text.pack()

if __name__ == '__main__':
    mainloop()

