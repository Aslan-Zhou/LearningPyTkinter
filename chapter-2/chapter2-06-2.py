from tkinter import *

root = Tk()
root.title("ch2_4")
lable = Label(root, text= "I like tkinter",
              fg="blue",bg="yellow",
              height = 3,width = 15,
              anchor = SE)
lable.pack()
print(type(lable))
root.mainloop()
