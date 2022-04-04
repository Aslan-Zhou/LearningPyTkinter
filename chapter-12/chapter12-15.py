from tkinter import *


def callback():
    print(lb.selection_includes(3))


fruits = ["Banana", "Watermelon", "Pineapple"
          "Orange", "Grapes", "Mango"]
root = Tk()
root.title("ch12-16")
root.geometry("300x250")

lb = Listbox(root, selectmode=MULTIPLE)
for fruit in fruits:
    lb.insert(END, fruit)

lb.pack(pady=10)
Button(root, text="Check", command=callback).pack(pady=5)
if __name__ == '__main__':
    mainloop()
