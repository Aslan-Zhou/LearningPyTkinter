from tkinter import *

root=Tk()
root.title("ch5-3")

sun_text = "欢迎进入阳光防卫系统终端"
sun_gif = PhotoImage(file="sun.gif")
logo = Label(root,image=sun_gif,text=sun_text,compound=BOTTOM)
AccountL = Label(root,text="Name ")
AccountL.grid(row=1)
PasswordL = Label(root,text="Password")
PasswordL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
AccountE = Entry(root)
AccountE.grid(row=1,column=1)
PasswordE = Entry(root,show="*")
PasswordE.grid(row=2,column=1,pady=10)

root.mainloop()
