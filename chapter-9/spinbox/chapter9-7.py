from tkinter import *

root = Tk()
root.title("ch9-7")
root.geometry("300x100")
Spinbox(root, from_=10, to=30, increment=2).pack(pady=20)

if __name__ == '__main__':
    mainloop()
