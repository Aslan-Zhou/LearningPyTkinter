from tkinter import *
from tkinter import messagebox


def Message1():
    ret = messagebox.askretrycancel(
        "Message Box", "安装失败,再试一次?")
    print("安装失败", ret)


def Message2():
    ret = messagebox.askyesnocancel(
        "Message Box", "编辑完成,是或否或取消?")
    print("编辑完成", ret)


root = Tk()
root.title("ch10-5")
Button(root, text="安装失败", command=Message1).pack()
Button(root, text="编辑完成", command=Message2).pack()

if __name__ == '__main__':
    mainloop()
