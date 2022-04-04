from tkinter import *


def print_info():
    print(sp.get())


root = Tk()
root.title("ch9-8")
sp = Spinbox(root, from_=0, to=10,
             command=print_info)
sp.pack(pady=10, padx=10)

if __name__ == '__main__':
    mainloop()
