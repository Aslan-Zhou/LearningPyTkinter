from tkinter import *
from tkinter.ttk import Separator
from PIL import Image, ImageTk

root = Tk()
root.title("神界日报")
# root.iconbitmap("s__j.bmp")
im = Image.open("sj.ico")
img = ImageTk.PhotoImage(im)
root.tk.call('wm', 'iconphoto', root._w, img)

Title = "<<一个人的极境旅行>>"
Content = """2019年7月，赵六一个人订了机票和船票，开
始他的南极之旅.飞机经过迪拜再往阿根廷的
乌斯怀亚，在此登上邮轮开始他的南极之旅。"""
label1 = Label(root, text=Title, font="Helvetic 21 bold",
               bg="Cornsilk", fg="dodgerblue")
label1.pack(padx=10, pady=10)
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=10)
label2 = Label(root, text=Content, font="Helvetic 12 bold",
               bg="#FFDEAD", fg="dodgerblue")
label2.pack(padx=10, pady=10)

root.mainloop()
