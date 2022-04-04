from tkinter import *


root = Tk()
root.title("ch12-22")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(50):
    lb.insert(END, "Line " + str(i))
lb.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=lb.yview)

if __name__ == '__main__':
    mainloop()
