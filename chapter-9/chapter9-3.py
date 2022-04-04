from tkinter import *


def print_info():
    print("垂直尺度值 = %d, 水平尺度值 = %d" % (SV.get(), SH.get()))


root = Tk()
root.title("ch9-3")
SV = Scale(root, from_=0, to=10,
           label="My Scale")
SV.set(3)
SV.pack()

SH = Scale(root, from_=0, to=10,
           length=300, orient=HORIZONTAL,
           label="My Scale")
SH.set(5)
SH.pack()

Button(root, text="Print", command=print_info).pack()

if __name__ == '__main__':
    mainloop()
