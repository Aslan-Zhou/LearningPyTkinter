from tkinter import *

root = Tk()
root.title("ch8-4")

Frame(width=150, height=80, relief=GROOVE, borderwidth=5).pack(side=LEFT, padx=5, pady=10)
Frame(width=150, height=80, relief=RAISED, borderwidth=5).pack(side=LEFT, padx=5, pady=10)
Frame(width=150, height=80, relief=RIDGE, borderwidth=5).pack(side=LEFT, padx=5, pady=10)

mainloop()
