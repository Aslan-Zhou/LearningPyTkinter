from tkinter import *
from tkinter.ttk import *


def load():
    pb["value"] = 0
    pb["maximum"] = maxbytes
    loading()


def loading():
    global bytes
    bytes += 256
    pb["value"] = bytes
    if bytes < maxbytes:
        pb.after(80, loading)


root = Tk()
root.title("ch15-3")
bytes = 0
maxbytes = 1048576

pb = Progressbar(root,  length=200, mode="determinate", orient=HORIZONTAL)
pb.pack(padx=10, pady=10)
pb["value"] = 0

Button(root, text="load", command=load).pack(pady=10)
if __name__ == '__main__':
    mainloop()
