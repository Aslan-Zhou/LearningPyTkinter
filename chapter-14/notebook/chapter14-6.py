from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch14-6")
root.geometry("300x160")

notebook = Notebook(root)

frame1 = Frame()
frame2 = Frame()
notebook.add(frame1, text="选项卡1")
notebook.add(frame2, text="选项卡2")
notebook.pack(padx=10, pady=10, fill=BOTH, expand=True)
if __name__ == '__main__':
    mainloop()
