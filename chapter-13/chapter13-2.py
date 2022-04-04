from tkinter import *

root = Tk()
root.title("ch13-2")
root.geometry("300x120")

omTuple = ("Python", "Java", "C")
var = StringVar(root)
OptionMenu(root, var, *omTuple).pack()
if __name__ == '__main__':
    mainloop()
