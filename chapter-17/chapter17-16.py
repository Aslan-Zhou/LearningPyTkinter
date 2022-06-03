from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *


def sizeSelected(event):
    f = Font(size=sizeVar.get())
    text.tag_config(SEL, font=f)


root = Tk()
root.title("17-16")
root.geometry("300x180")
toolbar = Frame(root, relief=RAISED, borderwidth=1)
toolbar.pack(side=TOP, fill=X, pady=1, padx=2)

sizeVar = IntVar()
size = Combobox(toolbar, textvariable=sizeVar)
sizeFamily = [x for x in range(8, 30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>", sizeSelected)
size.pack()

text = Text(root)
text.pack(fill=BOTH, expand=True, padx=3, pady=2)
text.insert(END, "Five Hundred Miles\n")
text.insert(END, "If you miss the rain I'm on, \n")
text.insert(END, "You will know that Iam gone.\n")
text.insert(END, "You can hear the whistle blow\n")
text.insert(END, "A Hundred miles, \n")
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
