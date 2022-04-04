from tkinter import *

fruits = ["Banana", "Watermelon", "Pineapple"]
root = Tk()
root.title("ch12-4")
root.geometry("300x210")

lb = Listbox(root, selectmode=EXTENDED)
for fruit in fruits:
    lb.insert(END, fruit)
lb.insert(ACTIVE, "Orange", "Grapes", "Mango")
lb.pack(pady=10)
if __name__ == '__main__':
    mainloop()
