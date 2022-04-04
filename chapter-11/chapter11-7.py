from tkinter import *


def buttonClicked(event):
    print("I like tkinter")


def toggle(onoff):
    if var.get():
        onoff.bind("<Button-1>", buttonClicked)
    else:
        onoff.unbind("<Button-1>")


root = Tk()
root.title("ch11-")
root.geometry("300x180")

btn = Button(root, text="tkinter")
btn.pack(anchor=W, pady=10, padx=10)
var = BooleanVar()
Checkbutton(root, text="bind/unbind", variable=var,
            command=lambda:toggle(btn)).pack(anchor=W,padx=10)
if __name__ == '__main__':
    mainloop()