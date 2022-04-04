from tkinter import *

root = Tk()
root.title("ch12-1")
root.geometry("300x210")

Listbox(root).pack(side=LEFT, padx=5, pady=10)
Listbox(root, height=5, relief="raised").\
    pack(anchor=N, side=LEFT, padx=5, pady=10)

if __name__ == '__main__':
    mainloop()
