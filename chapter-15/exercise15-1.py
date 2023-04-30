from tkinter import *
from tkinter.ttk import *


def load():
    pb1.start()
    pb2["value"] = 0
    pb2["maximum"] = maxbytes
    loading()


def loading():
    global bytes
    bytes += 512
    bt.config(state=DISABLED)
    pb2["value"] = bytes
    if bytes < maxbytes:
        pb2.after(25, loading)
    else:
        pb1.stop()

root = Tk()
root.title("ex15-1")
bytes = 0
maxbytes = 67108864

pb1 = Progressbar(root, length=200, mode="indeterminate", orient=HORIZONTAL)
pb1.pack(padx=10, pady=10)
pb1["value"] = 0
pb2 = Progressbar(root, length=200, mode="determinate", orient=HORIZONTAL)
pb2.pack(padx=5, pady=10)
pb2["maximum"] = 100
pb2["value"] = 0

bt = Button(root, text="load", command=load)
bt.pack(padx=10, pady=10)


if __name__ == '__main__':
    mainloop()