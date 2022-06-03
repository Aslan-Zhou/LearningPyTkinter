from tkinter import *
from tkinter.ttk import *


def removeItem():
    iids = tree.selection()
    for iid in iids:
        tree.delete(iid)


root = Tk()
root.title("ch18-10")

stateCity = {"山东": "青岛", "加利福尼亚": "洛杉矶", "德州": "休斯顿", "广东": "广州",
             "华盛顿州": "西雅图", "伊利诺": "芝加哥", "福建": "厦门", "江苏": "南京"}

tree = Treeview(root, columns="cities", selectmode=EXTENDED)
tree.heading("#0", text="State")
tree.heading("cities", text="City")
tree.column("cities", anchor=CENTER)


for state in stateCity.keys():
    tree.insert("", index=END, text=state, values=stateCity[state])

tree.pack()

Button(root, text="Remove", command=removeItem).pack(padx=5)
if __name__ == '__main__':
    mainloop()
