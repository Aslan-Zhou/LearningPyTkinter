from tkinter import *


def itemsSorted():
    if var.get():
        revBool = True
    else:
        revBool = False
    listTmp = list(lb.get(0, END))
    sortedList = sorted(listTmp, reverse=revBool)
    lb.delete(0, END)
    for item in sortedList:
        lb.insert(END, item)


fruits = ["Banana", 'Watermelon', 'Pineapple',
          'Orange', "Grapes", 'Mango']
root = Tk()
root.title("ch12-")
lb = Listbox(root)
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack(padx=10, pady=5)

Button(root, text="排序", command=itemsSorted
       ).pack(side=LEFT, padx=10, pady=5)
var = BooleanVar()
Checkbutton(root, text="从大到小排序", variable=var).pack(side=LEFT)
if __name__ == '__main__':
    mainloop()
