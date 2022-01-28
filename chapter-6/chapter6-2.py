from tkinter import *

def Button_Hit():
    if x.get() == "":
        x.set("I like tkinter")
    else:
        x.set("")

root = Tk()
root.title("ch6-2")


x = StringVar()

Label(root,textvariable=x,fg="blue",bg="lightyellow",
      font="Verdana 16 bold",width=25,height=2).pack()
Button(root,text="Click Me",command=Button_Hit).pack()

mainloop()
