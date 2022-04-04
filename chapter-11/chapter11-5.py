from tkinter import *


def key(event):
    print("按了" + repr(event.char) + " 键")

root = Tk()
root.title("ch11-5")

root.bind("<Key>", key)
if __name__ == '__main__':
    mainloop()
