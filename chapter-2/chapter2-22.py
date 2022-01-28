from tkinter import *
root = Tk()
root.title("ch2-22")
sseText = """SSE全名是Silicon Stone Education，这家公司在美国，
这是国际专业证照公司，产品多元与丰富。"""
sse_gif = PhotoImage(file="tree.png")
lable = Label(root,text=sseText,image=sse_gif,
            bg="lightyellow",compound="center")

lable.pack()
root.mainloop()
