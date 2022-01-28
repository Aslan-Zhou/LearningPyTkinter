from tkinter import *

root=Tk()
root.title("ch5-2")

AccountL = Label(root,text="Account")
AccountL.grid(row=0)
PasswordL = Label(root,text="Password")
PasswordL.grid(row=1)

AccountE = Entry(root)
AccountE.grid(row=0,column=1)
PasswordE = Entry(root,show="*")
PasswordE.grid(row=1,column=1)

root.mainloop()
