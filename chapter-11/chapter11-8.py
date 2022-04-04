import time
from tkinter import *


def btnClicked1():
    time.sleep(1)
    print("Command event handler, I like tkinter")


def btnClicked2(event):
    print("bind event handler, I like tkinter")


root = Tk()
root.title("ch11-8")
root.geometry("300x180")

btn = Button(root, text="tkinter", command=btnClicked1)
btn.pack(anchor=W, padx=10, pady=10)
btn.bind("<Button-1>", btnClicked2, add="+")

if __name__ == '__main__':
    mainloop()
