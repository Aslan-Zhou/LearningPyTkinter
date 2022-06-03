from tkinter import *
from tkinter import messagebox


def newFile():
    messagebox.showinfo("New File", "新建文档")


def openFile():
    messagebox.showinfo("New File", "打开文档")


def saveFile():
    messagebox.showinfo("New File", "保存文档")


def saveAsFile():
    messagebox.showinfo("New File", "另存为")


def About_Me():
    messagebox.showinfo("about Me", "洪锦魁著")


root = Tk()
root.title("ch16-6")
root.geometry("300x180")
menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu, underline=0)
filemenu.add_command(label="New File", command=newFile, underline=0)
filemenu.add_command(label="Open File", command=openFile, underline=0)
filemenu.add_separator()
filemenu.add_command(label="Save", command=saveFile, underline=0)
filemenu.add_command(label="Save As", command=saveAsFile, underline=5)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.destroy, underline=0)

root.config(menu=menubar)
helpmenu = Menu(menubar)
menubar.add_cascade(label="Help", menu=helpmenu, underline=0)
helpmenu.add_command(label="About Me", command=About_Me, underline=1)
root.config(menu=menubar)
if __name__ == '__main__':
    mainloop()
