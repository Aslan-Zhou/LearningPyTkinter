from tkinter import *

def print_Into():
    print("Account: %s\nPassword:%s" % (AccountE.get(),PasswordE.get()))
    AccountE.delete(0,END)
    PasswordE.delete(0,END)

root = Tk()
root.title("ch5-7")

sun_text = "欢迎进入阳光防卫系统终端"
sun_gif = PhotoImage(file="sun.gif")#
logo = Label(root,image=sun_gif,text=sun_text,compound=BOTTOM)
AccountL = Label(root,text="Name ")
AccountL.grid(row=1)
PasswordL = Label(root,text="Password")
PasswordL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
AccountE = Entry(root)
AccountE.insert(0,"Kevin")
AccountE.grid(row=1,column=1)
PasswordE = Entry(root,show="*")
PasswordE.insert(0,"Password")
PasswordE.grid(row=2,column=1,pady=10)
login_button = Button(root,text="Login",command=print_Into)
login_button.grid(row=3,column=1,sticky=W,pady=5)
quit_button = Button(root,text="quit",command=root.quit)
quit_button.grid(row=3,column=0,sticky=W,pady=5)
mainloop()
