from tkinter import *

fruits = ["Banana", "Watermelon", "Pineapple",
          "Orange", "Grapes", "Mango"]
root = Tk()
root.title("ch12-9")
root.geometry("300x210")

lb = Listbox(root, selectmode=EXTENDED)
for fruit in fruits:
    lb.insert(END, fruit)

lb.pack(pady=10)
lb.selection_set(0, 3)

if __name__ == '__main__':
    mainloop()
