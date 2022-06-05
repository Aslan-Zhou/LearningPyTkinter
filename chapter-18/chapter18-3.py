from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18-3")

tree = Treeview(root, columns=("cities", "populations"))
tree.heading("#0", text="State")
tree.heading("#1", text="City")
tree.heading("#2", text="Populations")
tree.insert("", index=END, text="伊利诺", values=("芝加哥", "800"))
tree.insert("", index=END, text="加利福尼亚", values=("洛杉矶", "1000"))
tree.insert("", index=END, text="江苏", values=("南京", "900"))
tree.pack()

if __name__ == '__main__':
    mainloop()
