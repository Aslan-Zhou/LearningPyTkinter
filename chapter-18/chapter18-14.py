from tkinter import *
from tkinter.ttk import *


def treeview_sortColumn(col):
    global reverseFlag
    lst = [(tree.set(st, col), st)
           for st in tree.get_children("")]
    print(lst)
    lst.sort(reverse=reverseFlag)
    print(lst)
    for index, item in enumerate(lst):
        tree.move(item[1], "", index)
    reverseFlag = not reverseFlag


root = Tk()
root.title("ch18-14")
reverseFlag = False

stateCity = {"Shandong": "Tsingtao", "California": "Los Angeles",
             "Texas": "Houston", "Guangdong": "Kwangchow",
             "Washington": "Houston", "Illinois": "Chicago",
             "Fujian": "Amoy", "Jiangsu": "Nanking",
             "Mississippi": "Oxford", "Kentucky": "Lexington",
             "Florida": "Miami", "Indiana": "West Lafayette",
             }

tree = Treeview(root, columns="states", show="headings")
yscrollbar = Scrollbar(root)
yscrollbar.pack(side=RIGHT, fill=Y)
tree.pack()
yscrollbar.config(command=tree.yview)
tree.configure(yscrollcommand=yscrollbar.set)

tree.heading("states", text="State")
for state in stateCity.keys():
    tree.insert("", index=END, values=(state,))

tree.heading("#1", text="State",
             command=lambda c="states": treeview_sortColumn(c))

if __name__ == '__main__':
    mainloop()
