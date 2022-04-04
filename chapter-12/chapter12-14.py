from tkinter import *


def callback():
    indexs = lb.curselection()
    for index in indexs:
        print(lb.get(index))


fruits = ["Banana", "Watermelon", "Pineapple",
          "Orange", "Grapes", "Mango"]
root = Tk()
root.title("ch12-14")
root.geometry("300x210")

lb = Listbox(root)
for fruit in fruits:
    lb.insert(END, fruit)

lb.pack(pady=10)
Button(root, text="Print", command=callback).pack(pady=5)
if __name__ == '__main__':
    mainloop()
