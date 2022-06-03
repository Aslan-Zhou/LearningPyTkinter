from tkinter import *
from tkinter import messagebox


def hello():
    messagebox.showinfo("Hello", "欢迎使用菜单")


root = Tk()
root.title("ch16-1")
root.geometry("300x180")
menubar = Menu(root)
menubar.add_command(label="Hello", command=hello)
menubar.add_command(label="Exit", command=root.destroy)
root.config(menu=menubar)
if __name__ == '__main__':
    mainloop()
