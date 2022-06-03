from tkinter import *


def mySearch():
    textContent = text.get("1.0", END)
    filename = "ch17_23.txt"
    with open(filename, "w") as output:
        output.write(textContent)
        root.title(filename)


root = Tk()
root.title("Untiled")
root.geometry("300x180")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=mySearch)
filemenu.add_command(label="Exit", command=root.destroy)
root.config(menu=menubar)
text = Text(root, undo=True)
text.pack(fill=X, expand=True)
text.insert(END, "Five Hundred Miles\n")
text.insert(END, "If you miss the rain I'm on, \n")
text.insert(END, "You will know that I am gone.\n")
text.insert(END, "You can hear the whistle blow\n")
text.insert(END, "A Hundred miles, \n")
if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("17-")

text = Text(root)
text.pack()

if __name__ == '__main__':
    mainloop()
