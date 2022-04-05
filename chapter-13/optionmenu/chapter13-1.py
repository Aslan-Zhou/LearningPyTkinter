from tkinter import *

root = Tk()
root.title("ch13-1")
root.geometry("300x120")

var = StringVar(root)
OptionMenu(root, var, "Python",
           "Java", "C").pack()
if __name__ == '__main__':
    mainloop()
