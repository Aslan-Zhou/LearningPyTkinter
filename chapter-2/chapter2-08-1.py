from tkinter import *

root = Tk()
root.title("ch2_8")
lable = Label(root, text= "I like tkinter",
              fg="blue",bg="yellow",
              height = 3,width = 15,
              font = ("Helvetic", 20, "bold"))
lable.pack()

root.mainloop()
