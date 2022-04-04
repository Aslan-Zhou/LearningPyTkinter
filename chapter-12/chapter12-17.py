from tkinter import *


def itemSelected(event):
    index = lb.curselection()
    var.set(lb.get(index))


fruits = ["Banana", "Watermelon", "Pineapple",
          "Orange", "Grapes", "Mango"]
root = Tk()
root.title("ch12-17")
root.geometry("300x210")

var = StringVar()
Label(root, text="", textvariable=var).pack(pady=5)
lb = Listbox(root)
for fruit in fruits:
    lb.insert(END, fruit)

lb.bind("<Double-Button-1>", itemSelected)
lb.pack(pady=10)
if __name__ == '__main__':
    mainloop()
