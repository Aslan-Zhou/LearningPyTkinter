from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18-7")
asia = {"中国": "北京", "日本": "东京", "泰国": "曼谷", "韩国": "首尔"}
euro = {"英国": "伦敦", "法国": "巴黎", "德国": "柏林", "挪威": "奥斯陆"}
tree = Treeview(root, columns="capital")
tree.heading("#0", text="国家")
tree.heading("#1", text="首都")
idAsia = tree.insert("", index=END, text="Asia")
idEuro = tree.insert("", index=END, text="Europe")
for country in asia.keys():
    tree.insert(idAsia, index=END, text=country, values=asia[country])
for country in euro.keys():
    tree.insert(idEuro, index=END, text=country, values=asia[country])
tree.pack()

if __name__ == '__main__':
    mainloop()
