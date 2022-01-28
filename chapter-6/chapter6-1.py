from tkinter import *

def Button_Hit():
    global msg_on
    if not msg_on:
        msg_on = True
        x.set("I like tkinter")
    else:
        msg_on = False
        x.set("")

root = Tk()
root.title("ch6-1")

msg_on = False
x = StringVar()

Label(root,textvariable=x,fg="blue",bg="lightyellow",
      font="Verdana 16 bold",width=25,height=2).pack()
Button(root,text="Click Me",command=Button_Hit).pack()

mainloop()
