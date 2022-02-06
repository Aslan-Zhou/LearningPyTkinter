from tkinter import *


root = Tk()
root.title("ch8-10")

toplevel = Toplevel()
toplevel.title("toplevel")
toplevel.geometry("300x180")
Label(toplevel, text="I am a Toplevel").pack()
mainloop()
