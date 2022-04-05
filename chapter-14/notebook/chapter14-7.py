from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


def message():
    messagebox.showinfo("Notebook", "欢迎使用Notebook")


root = Tk()
root.title("ch14-6")
root.geometry("300x160")

notebook = Notebook(root)

frame1 = Frame()
frame2 = Frame()
Label(frame1, text="Python").pack(pady=10, padx=10)
Button(frame2, text="Help", command=message).pack(padx=10, pady=10)
notebook.add(frame1, text="页次1")
notebook.add(frame2, text="页次2")

notebook.pack(padx=10, pady=10, fill=BOTH, expand=True)
if __name__ == '__main__':
    mainloop()
