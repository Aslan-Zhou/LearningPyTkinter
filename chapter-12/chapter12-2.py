from tkinter import *

root = Tk()
root.title("ch12-2")

lb = Listbox(root)
lb.insert(END, "Banana")
lb.insert(END, "Watermelon")
lb.insert(END, "Pineapple")
lb.pack(pady=10)

if __name__ == '__main__':
    mainloop()
