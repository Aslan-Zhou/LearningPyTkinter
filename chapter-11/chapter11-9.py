from tkinter import *
from tkinter import messagebox


def callback():
    res = messagebox.askokcancel("OKCANCEL", "结束或取消?")
    if res:
        root.destroy()
    else:
        return


root = Tk()
root.title("ch11-9")
root.geometry("300x180")
root.protocol("WM_DELETE_WINDOW", callback)

if __name__ == '__main__':
    mainloop()
