from tkinter import *


root = Tk()
root.title("ch10-1")
Text = """2016年12月,我一个人订了机票和船票,开始我的南极之旅."""
Message(root, bg="yellow", text=Text,
        font="times 12 italic").pack(padx=10, pady=10)
if __name__ == '__main__':
    mainloop()
