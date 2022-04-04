from tkinter import *


root = Tk()
root.title("ch10-2")

var = StringVar()
Message(root, textvariable=var, relief=RAISED).pack(padx=10, pady=10)
var.set("""2016年12月,我一个人订了机票和船票,开始我的南极之旅.""")

if __name__ == '__main__':
    mainloop()
