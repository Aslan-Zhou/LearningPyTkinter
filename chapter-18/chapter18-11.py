from tkinter import *
from tkinter.ttk import *


def removeItem():
    ids = tree.selection()
    for id in ids:
        tree.delete(id)


def insertItem():
    state = stateEntry.get()
    city = cityEntry.get()
    if len(state.strip) == 0 or len(city.strip()) == 0:
        return
    tree.insert("", END, text=state, value=city)
    stateEntry.delete(0, END)
    cityEntry.delete(0, END)


root = Tk()
root.title("ch18-11")

stateCity = {"山东": "青岛", "加利福尼亚": "洛杉矶", "德州": "休斯顿", "广东": "广州",
             "华盛顿州": "西雅图", "伊利诺": "芝加哥", "福建": "厦门", "江苏": "南京"}

root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(3, weight=1)

stateLab = Label(root, text="State  = ")
stateLab.grid(row=0, column=0, padx=5, pady=3, sticky=W)
stateEntry = Entry()
stateEntry.grid(row=0, column=1, sticky=W+E, padx=5, pady=3)

cityLab = Label(root, text="City  = ")
cityLab.grid(row=0, column=2, sticky=E)
cityEntry = Entry()
cityEntry.grid(row=0, column=3, sticky=W+E, padx=5, pady=3)

Button(root, text="Insert", command=insertItem).grid(row=0, column=4, pady=3, padx=5)

tree = Treeview(root, columns="cities", selectmode=EXTENDED)
tree.heading("#0", text="State")
tree.heading("cities", text="City")
tree.column("cities", anchor=CENTER)

for state in stateCity.keys():
    tree.insert("", index=END, text=state, values=stateCity[state])

tree.grid(row=1, column=0, columnspan=5, padx=5, sticky=W+E+N+S)

Button(root, text="Remove", command=removeItem).grid(row=2, column=2, padx=5, pady=3, sticky=W)
if __name__ == '__main__':
    mainloop()
