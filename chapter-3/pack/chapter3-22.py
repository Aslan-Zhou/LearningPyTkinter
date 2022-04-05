from tkinter import *

root = Tk()
root.title("300x200")

label1 = Label(root, text="Mississippi", bg='red', fg='white',
               font="Times 24 bold").pack(side=LEFT,fill=Y)
label2 = Label(root,text="Kentucky",bg='green',fg='white',
               font="Arial 24 bold italic").pack(side=LEFT,fill=BOTH,expand=True)
label3 = Label(root, text="Purdue", bg='blue', fg='white',
               font="Times 24 bold").pack(side=LEFT,fill=Y)

root.mainloop()
