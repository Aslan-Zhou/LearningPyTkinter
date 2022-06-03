from tkinter import *
from tkinter.ttk import *


def load():
    pb1.start()
    pb2["value"] = 0
    pb2["maximum"] = maxbytes
    loading()


def loading():
    global bytes
    bytes += 256
    pb2["value"] = bytes
    if bytes < maxbytes:
        pb2.after(25, loading)
    else:
        pb1.stop()


root = Tk()
root.title("tk15-1")
bytes = 0
maxbytes = 1048576

pb1 = Progressbar(root, length=200, mode="indeterminate", orient=HORIZONTAL)
pb1.pack(padx=10, pady=10)
pb1["value"] = 0
pb2 = Progressbar(root, length=200, mode="determinate", orient=HORIZONTAL)
pb2.pack(padx=5, pady=10)
pb2["maximum"] = 100
pb2["value"] = 0

Button(root, text="load", command=load).pack(padx=10, pady=10)


if __name__ == '__main__':
    mainloop()
