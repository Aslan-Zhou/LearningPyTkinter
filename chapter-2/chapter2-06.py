from tkinter import *

root = Tk()
root.title("ch2_4")
lable = Label(root, text= "I like tkinter",
              fg="blue",bg="yellow",
              height = 3,width = 15,
              anchor = "se")
lable.pack()

root.mainloop()
