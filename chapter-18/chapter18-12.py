from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


def doubleClick(event):
    e = event.widget
    iid = e.identify("item", event.x, event.y)
    state = e.item(iid, "text")
    city = e.item(iid, "values")[0]
    str = "{0} : {1}".format(state, city)
    messagebox.showinfo("Double Clicked", str)


stateCity = {"山东": "青岛", "加利福尼亚": "洛杉矶", "德州": "休斯顿", "广东": "广州",
             "华盛顿州": "西雅图", "伊利诺": "芝加哥", "福建": "厦门", "江苏": "南京"}
root = Tk()
root.title("ch18-12")

tree = Treeview(root, columns="cities")
tree.heading("#0", text="State")
tree.heading("cities", text="City")
tree.column("cities", anchor=CENTER)
for state in stateCity.keys():
    tree.insert("", index=END, text=state, values=stateCity[state])
tree.bind("<Double-1>", doubleClick)
tree.pack()

if __name__ == '__main__':
    mainloop()
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18-")

tree = Treeview(root)
tree.heading("", text="")
tree.insert("", index=END, text="", values="")
tree.pack()

if __name__ == '__main__':
    mainloop()
