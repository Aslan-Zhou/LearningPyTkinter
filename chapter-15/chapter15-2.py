from tkinter import *
from tkinter.ttk import *
import time


def running():
    for i in range(100):
        pb["value"] = i+1
        root.update()
        time.sleep(0.05)


root = Tk()
root.title("ch15-2")

pb = Progressbar(root, length=200, mode="determinate")
pb.pack(padx=10, pady=10)
pb["maximum"] = 100
pb["value"] = 0

Button(root, text="running", command=running).pack(pady=10)
if __name__ == '__main__':
    mainloop()
