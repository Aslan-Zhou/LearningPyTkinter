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


root = Tk()
root.title("ch16-4")
root.geometry("300x180")
menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="open File", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAsFile)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.destroy)

root.config(menu=menubar)
if __name__ == '__main__':
    mainloop()
