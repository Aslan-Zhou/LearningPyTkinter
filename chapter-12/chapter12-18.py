from tkinter import *


def itemSelected(event):
    obj = event.widget
    indexs = obj.curselection()
    for index in indexs:
        print(obj.get(index))
    print("----------")


fruits = ["Banana", "Watermelon", "Pineapple",
          "Orange", "Grapes", "Mango"]
root = Tk()
root.title("ch12-18")
root.geometry("300x210")

var = StringVar()
Label(root, text="", textvariable=var).pack(pady=5)
lb = Listbox(root, selectmode=MULTIPLE)
for fruit in fruits:
    lb.insert(END, fruit)

lb.bind("<<ListboxSelect>>", itemSelected)
lb.pack(pady=10)
if __name__ == '__main__':
    mainloop()
