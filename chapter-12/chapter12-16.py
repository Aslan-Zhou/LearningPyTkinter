from tkinter import *


def itemSelected(event):
    obj = event.widget
    index = obj.curselection()
    var.set(obj.get(index))


fruits = ["Banana", "Watermelon", "Pineapple",
          "Orange", "Grapes", "Mango"]
root = Tk()
root.title("ch12-16")
root.geometry("300x210")

var = StringVar()
Label(root, text="", textvariable=var).pack(pady=5)
lb = Listbox(root)
for fruit in fruits:
    lb.insert(END, fruit)

lb.bind("<<ListboxSelect>>", itemSelected)
lb.pack(pady=10)
if __name__ == '__main__':
    mainloop()
