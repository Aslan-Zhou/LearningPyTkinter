from tkinter import *
from tkinter import messagebox


def Message():
    messagebox.showinfo("My Message Box", "Python Tkinter 早安")


root = Tk()
root.title("ch10-4")
root.geometry("300x160")
Button(root, text="Good morning", command=Message).pack()

if __name__ == '__main__':
    mainloop()
