from tkinter import *

root = Tk()
root.title("ch8-5")
fm = Frame(width=150, height=80, relief=RAISED, borderwidth=5)
Label(fm, text="请复选常用的编程语言", bg="yellow",
      fg="blue", width=30).pack()

Checkbutton(fm, text="Python").pack(anchor=W)
Checkbutton(fm, text="Java").pack(anchor=W)
Checkbutton(fm, text="Ruby").pack(anchor=W)
fm.pack(padx=10,pady=10)

mainloop()
