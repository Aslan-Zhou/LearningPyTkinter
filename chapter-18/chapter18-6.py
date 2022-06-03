from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18-6")
stateCity = {"山东": "青岛", "加利福尼亚": "洛杉矶", "德州": "休斯顿", "广东": "广州",
             "华盛顿州": "西雅图", "伊利诺": "芝加哥", "福建": "厦门", "江苏": "南京"}
tree = Treeview(root, columns="cities")
tree.heading("#0", text="State")
tree.heading("cities", text="City")
tree.column("cities", anchor=CENTER)
tree.tag_configure("evenColor", background="lightblue")
rowCount = 1
for state in stateCity.keys():
    if rowCount % 2 == 1:
        tree.insert("", index=END, text=state, values=stateCity[state])
    else:
        tree.insert("", index=END, text=state, values=stateCity[state], tags="evenColor")
        rowCount += 1
tree.pack()

if __name__ == '__main__':
    mainloop()
