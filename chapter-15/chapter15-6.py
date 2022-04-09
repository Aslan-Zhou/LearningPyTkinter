from tkinter import *
from tkinter.ttk import *


def run():
    pb.start()


def stop():
    pb.stop()


root = Tk()
root.title("ch15-6")

pb = Progressbar(root, length=200, mode="indeterminate", orient=HORIZONTAL)
pb.pack(padx=5, pady=10)
pb["maximum"] = 100
pb["value"] = 0

Button(root, text="Run", command=run).pack(side=LEFT, padx=5, pady=10)
Button(root, text="Stop", command=stop).pack(side=LEFT, padx=5, pady=10)

if __name__ == '__main__':
    mainloop()
