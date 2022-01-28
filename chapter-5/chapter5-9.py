from tkinter import *

def math():
    out.configure(text="结果 ：" + str(eval(equ.get())))

root = Tk()
root.title("ch5-9")
label = Label(root,text="请输入数学表达式：")
label.pack()
equ = Entry(root)
equ.pack(pady=5)
out = Label(root)
out.pack()
button = Button(root,text="计算",command=math)
button.pack(pady=5)

mainloop()
