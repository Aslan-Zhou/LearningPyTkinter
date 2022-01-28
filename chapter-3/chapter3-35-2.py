from tkinter import *

root = Tk()
root.title("ch3-35-2")

root.rowconfigure(1, weight=1)
root.columnconfigure(0,weight=1)

lable1 = Label(root,text="Lable 1",bg="pink")
lable1.grid(row=0,column=0,padx=5,pady=5,sticky=W)

lable2 = Label(root,text="Lable 2",bg="lightblue")
lable2.grid(row=0,column=1,padx=5,pady=5)

lable3 = Label(root,bg="yellow")
lable3.grid(row=1,column=0,columnspan=2,
            padx=5,pady=5,sticky=N+E+W+S)

root.mainloop()
