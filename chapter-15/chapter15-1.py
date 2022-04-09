from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x140")
root.title("ch15-1")

pb1 = Progressbar(root)
pb1.pack(pady=20)
pb1["maximum"] = 100
pb1["value"] = 50

pb2 = Progressbar(root, orient=HORIZONTAL, length=200, mode="determinate")
pb2.pack(pady=20)
pb2["maximum"] = 100
pb2["value"] = 50
if __name__ == '__main__':
    mainloop()
