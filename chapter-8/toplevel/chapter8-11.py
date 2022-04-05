from tkinter import *
import random

root = Tk()
root.title("ch8-11")
root.geometry("100x100+700+700")
msgYes, msgNo, msgExit = 1, 2, 3


def MessageBox():
    msg_type = random.randint(1, 3)
    if msg_type == msgYes:
        label_text = "Yes"
    elif msg_type == msgNo:
        label_text = "No"
    else:
        label_text = "Exit"
    for i in range(100):
        toplevel = Toplevel()
        toplevel.geometry("100x100")
        toplevel.title("Massage Box")
        Label(toplevel, text=label_text).pack(fill=BOTH, expand=True)


Button(root, text="Click Me", command=MessageBox).pack(fill=BOTH, expand=True)

mainloop()
