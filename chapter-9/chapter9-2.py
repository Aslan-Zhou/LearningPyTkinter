from tkinter import *


root = Tk()
root.title("ch9-2")
Scale(root, from_=0, to=10,
      troughcolor="green",
      width=30, length=300,
      tickinterval=2, bg="green",
      orient=HORIZONTAL,
      label="My Scale").pack()

if __name__ == '__main__':
    mainloop()
