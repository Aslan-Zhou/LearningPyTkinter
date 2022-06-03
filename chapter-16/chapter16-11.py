from tkinter import *


root = Tk()
root.title('ch16-11')
root.geometry('300x180')
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.destroy)

toolbar = Frame(root, relief=RAISED, borderwidth=3)
abcGif = PhotoImage(file="cba.png")
Button(toolbar, image=abcGif, command=root.destroy).pack(side=LEFT, pady=3, padx=3)
toolbar.pack(side=TOP, fill=X)

root.config(menu=menubar)
if __name__ == '__main__':
    mainloop()
