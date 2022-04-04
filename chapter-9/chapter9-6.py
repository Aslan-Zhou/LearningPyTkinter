from tkinter import *


def bg_Update(source):
    red = RS.get()
    green = GS.get()
    blue = BS.get()
    print("R=%d, G=%d, B=%d" % (red, green, blue))
    color = "#%02x%02x%02x" % (red, green, blue)
    root.config(bg=color)


root = Tk()
root.title("ch9-6")
root.geometry("860x680")
fm = Frame(root)
fm.pack()
RS = Scale(fm, from_=0, to=255, command=bg_Update)
RS.set(0)
RS.grid(row=0, column=0)

GS = Scale(fm, from_=0, to=255, command=bg_Update)
GS.set(255)
GS.grid(row=0, column=1)

BS = Scale(fm, from_=0, to=255, command=bg_Update)
BS.set(0)
BS.grid(row=0, column=3)

if __name__ == '__main__':
    mainloop()
