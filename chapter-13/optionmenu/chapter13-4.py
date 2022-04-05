from tkinter import *


def printSelection():
    print("The selection is : ", var.get())


root = Tk()
root.title("ch13-4")
root.geometry("300x120")

omTuple = ("Python", "Java", "C")
var = StringVar(root)
var.set(omTuple[0])
OptionMenu(root, var, *omTuple).pack()

Button(root, text="Print", command=printSelection
       ).pack(pady=10, anchor=S, side=BOTTOM)
if __name__ == '__main__':
    mainloop()
