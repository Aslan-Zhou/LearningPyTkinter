from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("                                      神界日报")
root.iconbitmap("sj.ico")
Title = "<<一个人的极境旅行>>"
Content = """2021年12月17日，赵六（火神）一个人订了机票和船
票，开始他的南极旅行，飞机经过迪拜再往阿根
廷的乌斯怀亚，在此登上游轮开始他的南极之旅。"""
lable1 = Label(root,text=Title,font="Helvetic 22 bold",
               bg="Cornsilk",fg="blue")
lable1.pack(padx=10,pady=10)
sep = Separator(root,orient=HORIZONTAL)
sep.pack(fill=X,padx=10)
lable2 = Label(root,text=Content,font="Helvetic 12 bold",
               bg="#FFDEAD",fg="blue")
lable2.pack(padx=10,pady=10)

root.mainloop()
