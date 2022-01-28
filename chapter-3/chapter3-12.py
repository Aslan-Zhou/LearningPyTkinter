from tkinter import *

root = Tk()
root.title("ch3-12")
root.geometry("300x180")
oklabel = Label(root,text="OK",
                font="Times 20 bold",
                fg="white",bg="blue")
oklabel.pack(anchor=S,side=RIGHT,
             padx=10,pady=10)

root.mainloop()
