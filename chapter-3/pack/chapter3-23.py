from tkinter import *

root = Tk()
root.title("ch3-13")
root.geometry("300x180")
print("执行前",root.pack_slaves())
ok_label = Label(root,text="OK",
                font="Times 20 bold",
                fg="white",bg="blue")
ok_label.pack(anchor=S,side=RIGHT,
             padx=10,pady=10)
no_label = Label(root,text="NO",
                font="Times 20 bold",
                fg="white",bg="red")
no_label.pack(anchor=S,side=RIGHT,
             pady=10)
print("执行后",root.pack_slaves())

root.mainloop()
