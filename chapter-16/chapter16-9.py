from tkinter import *
from tkinter import messagebox


def minimizeIcon():
    root.iconify()


def showPopupMenu(event):
    popupmenu.post(event.x_root, event.y_root)


root = Tk()
root.title('ch16-9')
root.geometry('300x180')
popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="Minimize", command=minimizeIcon)
popupmenu.add_command(label="Exit", command=root.destroy)
root.bind("<Button-3>", showPopupMenu)
if __name__ == '__main__':
    mainloop()
