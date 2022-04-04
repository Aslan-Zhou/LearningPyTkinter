from tkinter import *


root = Tk()
root.title("ch9-1")

Scale(root, from_=0, to=10).pack()
Scale(root, from_=0, to=10,
      length=150, orient=HORIZONTAL).pack()

if __name__ == '__main__':
    mainloop()
