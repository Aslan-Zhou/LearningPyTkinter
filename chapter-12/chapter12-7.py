from tkinter import *

fruits = ["Banana", "Watermelon", "Pineapple",
          "Orange", "Grapes", "Mango"]
root = Tk()
root.title("ch12-7")
root.geometry("300x210")

lb = Listbox(root, selectmode=EXTENDED)
for fruit in fruits:
    lb.insert(END, fruit)

lb.pack(pady=10)
print("items数字 : ", lb.size())

if __name__ == '__main__':
    mainloop()
