from tkinter import *

root = Tk()
root.title("ch8-7")

yc_text = "欢迎进入大圆防卫系统终端"
yc_png = PhotoImage(file="yellow_circle.png")
logo = Label(root, image=yc_png, text=yc_text, compound=BOTTOM)
logo.pack()
labelFrame = LabelFrame(root,text="验证")
labelFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)
AccountL = Label(labelFrame, text="Account")
AccountL.grid(row=1)
PasswordL = Label(labelFrame, text="Password")
PasswordL.grid(row=2)

AccountE = Entry(labelFrame)
AccountE.grid(row=1, column=1)
PasswordE = Entry(labelFrame, show="*")
PasswordE.grid(row=2, column=1, pady=10)

root.mainloop()
