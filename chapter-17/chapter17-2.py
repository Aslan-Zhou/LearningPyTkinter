from tkinter import *

root = Tk()
root.title("17-2")

text = Text(root, height=2, width=30)
text.pack()
text.insert(END, "hello\nworld\n")
text.insert(INSERT, "Python")

if __name__ == '__main__':
    mainloop()
