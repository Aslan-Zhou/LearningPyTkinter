from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18-1")

tree = Treeview(root, columns=("cities"))
tree.heading("#0", text="State")
tree.heading("#1", text="City")
tree.insert("", index=END, text="伊利诺", value="芝加哥")
tree.insert("", index=END, text="加利福尼亚", value="洛杉矶")
tree.insert("", index=END, text="江苏", value="南京")
tree.pack()

if __name__ == '__main__':
    mainloop()
