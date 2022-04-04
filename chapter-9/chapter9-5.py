from tkinter import *
from tkinter.colorchooser import *


def bg_Update():
    color = askcolor()
    print(type(color), color)
    root.config(bg=color[1])


root = Tk()
root.title("ch9-5")
root.geometry("860x680")
root.config(bg="white")
Button(text="Select Color", command=bg_Update).pack(pady=5)

if __name__ == '__main__':
    mainloop()
