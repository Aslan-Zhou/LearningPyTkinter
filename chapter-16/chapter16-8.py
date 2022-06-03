from tkinter import *
from tkinter import messagebox


def findNext():
    messagebox.showinfo('Find Next', '查找下一个')


def findPre():
    messagebox.showinfo('Find Pre', '查找下一个')


root = Tk()
root.title('ch16-8')
root.geometry('300x180')
menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu, underline=0)
findmenu = Menu(filemenu, tearoff=False)
findmenu.add_command(label="Find Next", command=findNext)
findmenu.add_command(label="Find Pre", command=findPre)
filemenu.add_cascade(label="Find ", menu=findmenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy, underline=0)
root.config(menu=menubar)
if __name__ == '__main__':
    mainloop()
