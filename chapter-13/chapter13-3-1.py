from tkinter import *

root = Tk()
root.title("ch13-3-1")
root.geometry("300x120")

omTuple = ("Python", "Java", "C")
var = StringVar(root)
var.set(omTuple[0])
OptionMenu(root, var, *omTuple).pack()
if __name__ == '__main__':
    mainloop()
