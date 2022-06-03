from tkinter import *
from tkinter.ttk import *

stateCity = {"Shandong": "Tsingtao", "California": "Los Angeles",
             "Texas": "Houston", "Guangdong": "Kwangchow",
             "Washington": "Houston", "Illinois": "Chicago",
             "Fujian": "Amoy", "Jiangsu": "Nanking",
             "Mississippi": "Oxford", "Kentucky": "Lexington",
             "Florida": "Miami", "Indiana": "West Lafayette",
             }
root = Tk()
root.title("ch18-13")

tree = Treeview(root, columns="cities")
yscrollbar = Scrollbar(root)
yscrollbar.pack(side=RIGHT, fill=Y)
tree.pack()
yscrollbar.config(command=tree.yview)
tree.configure(yscrollcommand=yscrollbar.set)
tree.heading("#0", text="State")
tree.heading("cities", text="City")
tree.column("cities", anchor=CENTER)
for state in stateCity.keys():
    tree.insert("", index=END, text=state, values=stateCity[state])

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
