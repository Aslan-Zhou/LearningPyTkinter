from tkinter import *


def print_info():
    print(sp.get())


root = Tk()
root.title("ch9-9")

sp = Spinbox(root, values=(10, 38,
                           170, 101), command=print_info)
sp.pack(pady=10, padx=10)

if __name__ == '__main__':
    mainloop()
