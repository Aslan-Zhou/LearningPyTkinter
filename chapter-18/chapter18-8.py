from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch18-8")

Style().configure("Treeview", rowheight=35)

info = ["凤凰新闻APP可以获得中国各地最新消息",
        "瑞士国家铁路APP提供全瑞士火车时刻表",
        "可口可乐APP是一个娱乐的软件"]
tree = Treeview(root, columns="说明")
tree.heading("#0", text="APP")
tree.heading("#1", text="功能说明")
tree.column("#1", width=300)

img1 = Image.open("a.jpg")
imgObj1 = ImageTk.PhotoImage(img1)
tree.insert("", index=END, text="凤凰新闻", image=imgObj1, values=info[0])

img2 = Image.open("b.jpg")
imgObj2 = ImageTk.PhotoImage(img2)
tree.insert("", index=END, text="瑞士铁路", image=imgObj2, values=info[1])

img3 = Image.open("c.jpg")
imgObj3 = ImageTk.PhotoImage(img3)
tree.insert("", index=END, text="可口可乐", image=imgObj3, values=info[2])
tree.pack()

if __name__ == '__main__':
    mainloop()
