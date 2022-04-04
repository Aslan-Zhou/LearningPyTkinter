from tkinter import *


def callback(event):
    print("Clicked at ", event.x, event.y)


root = Tk()
root.title("ch11-2")
frame = Frame(root, width=300, height=180)
frame.bind("<Button-1>", callback)
frame.pack()

if __name__ == '__main__':
    mainloop()
