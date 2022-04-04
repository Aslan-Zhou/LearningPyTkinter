from tkinter import *


def print_info():
    print(sp.get())


cities = ["新加坡", "上海", "东京"]
root = Tk()
root.title("ch9-10")
sp = Spinbox(root, values=cities, command=print_info)
sp.pack(pady=10, padx=10)

if __name__ == '__main__':
    mainloop()
