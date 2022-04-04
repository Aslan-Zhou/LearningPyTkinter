from tkinter import *
from tkinter import messagebox


def leave(event):
    ret = messagebox.askyesno("ch11-4", "是否离开?")
    if ret:
        root.destroy()
    else:
        return


root = Tk()
root.title("ch11-4")
root.bind("<Escape>", leave)

Label(root, text="测试Esc键", bg="yellow", fg="blue", height=4,
      width=15, font="Times 12 bold").pack(padx=30,pady=30)

if __name__ == '__main__':
    mainloop()
