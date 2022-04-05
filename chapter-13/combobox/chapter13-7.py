from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch13-7")
root.geometry("300x120")

var = StringVar()
cb = Combobox(root, textvariable=var)
cb["values"] = ("Python", "Java", "C#", "C")
cb.current(0)
cb.pack(pady=10)

if __name__ == '__main__':
    mainloop()
