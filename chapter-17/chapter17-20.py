from tkinter import *
from tkinter import messagebox


def cutJob():
    text.event_generate("<<Cut>>")


def copyJob():
    text.event_generate("<<Copy>>")


def pasteJob():
    text.event_generate("<<Paste>>")


def showPopupMenu(event):
    popupmenu.post(event.x_root, event.y_root)


def undoJob():
    try:
        text.edit_redo()
    except:
        print("先前没有动作")


def redoJob():
    try:
        text.edit_undo()
    except:
        print("先前没有动作")


root = Tk()
root.title("17-20")
root.geometry("300x180")

popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="Cut", command=cutJob)
popupmenu.add_command(label="copy", command=copyJob)
popupmenu.add_command(label="Paste", command=pasteJob)

root.bind("<Button-3>", showPopupMenu)

toolbar = Frame(root, relief=RAISED, borderwidth=1)
toolbar.pack(side=TOP, fill=X, padx=2, pady=1)

Button(toolbar, text="Undo", command=undoJob).pack(side=LEFT, pady=2)
Button(toolbar, text="Redo", command=redoJob).pack(side=LEFT, pady=2)

text = Text(root, undo=True)
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
