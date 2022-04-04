from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch13-5")
root.geometry("300x120")

var = StringVar()
Combobox(root, textvariable=var,
         values=("Python",
                 "Java", "C#", "C"
                 )).pack(pady=10)
if __name__ == '__main__':
    mainloop()
