from tkinter import *


def mouseMotion(event):
    x = event.x
    y = event.y
    text_var = "Mouse location = x:{} y:{}".format(x, y)
    var.set(text_var)


root = Tk()
root.title("ch11-3")
root.geometry("300x180")
x1, y2 = 0, 0
var = StringVar()
text = "Mouse location = x:{} y:{}".format(x1, y2)
var.set(text)

Label(root, textvariable=var).pack(
    anchor=S,side=RIGHT, padx=10, pady=10)

root.bind("<Motion>", mouseMotion)

if __name__ == '__main__':
    mainloop()
