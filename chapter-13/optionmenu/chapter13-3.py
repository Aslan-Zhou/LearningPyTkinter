from tkinter import *

root = Tk()
root.title("ch13-3")
root.geometry("300x120")

omTuple = ("Python", "Java", "C")
var = StringVar(root)
var.set("Python")
OptionMenu(root, var, *omTuple).pack()
if __name__ == '__main__':
    mainloop()
