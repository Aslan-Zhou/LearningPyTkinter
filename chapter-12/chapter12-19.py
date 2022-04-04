from tkinter import *


def itemAdded():
    varAdd = entry.get()
    if len(varAdd.strip()) == 0:
        return
    lb.insert(END, varAdd)
    entry.delete(0, END)


def itemDeleted():
    index = lb.curselection()
    if len(index) == 0:
        return
    lb.delete(index)


root = Tk()
root.title("ch12-19")
entry = Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)

Button(root, text="增加", width=10,
       command=itemAdded).grid(row=0, column=1, padx=5, pady=5)

lb = Listbox(root)
lb.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=W)

Button(root, text="删除", width=10,
       command= itemDeleted).grid(row=2, column=0,
                                  padx=5, pady=5, sticky=W)
if __name__ == '__main__':
    mainloop()
