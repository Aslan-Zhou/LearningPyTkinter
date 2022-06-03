from tkinter import *
from tkinter import messagebox


def newFile():
    messagebox.showinfo("New File", "新建文档")


root = Tk()
root.title("ch16-3")
root.geometry("300x180")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Exit", command=root.destroy)

root.config(menu=menubar)
if __name__ == '__main__':
    mainloop()
from tkinter import *
from tkinter import messagebox


def value():
    messagebox.showinfo(" ", " ")


root = Tk()
root.title("ch16-")
root.geometry("300x180")
menubar = Menu(root)
menubar.add_cascade()
filemenu = Menu(menubar)
root.config(menu=menubar)
if __name__ == '__main__':
    mainloop()