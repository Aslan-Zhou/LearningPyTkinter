from tkinter import *
from tkinter import messagebox


def cutJob():
    copyJob()
    text.delete(SEL_FIRST, SEL_LAST)


def copyJob():
    try:
        text.clipboard_clear()
        copyText = text.get(SEL_FIRST, SEL_LAST)
        text.clipboard_append(copyText)
    except TclError:
        print("没有选取")


def pasteJob():
    try:
        copyText = text.selection_get(selection="CLIPBOARD")
        text.insert(INSERT, copyText)
    except TclError:
        print("剪贴板没有数据")


def showPopupMenu(event):
    popupmenu.post(event.x_root, event.y_root)


root = Tk()
root.title("17-18")
root.geometry("300x180")

popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="Cut", command=cutJob)
popupmenu.add_command(label="copy", command=copyJob)
popupmenu.add_command(label="Paste", command=pasteJob)

root.bind("<Button-3>", showPopupMenu)

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
