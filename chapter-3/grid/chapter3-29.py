from tkinter import *

window = Tk()
window.title("ch3-29")
lable1 = Label(window,text="标签1",relief="raised")
lable2 = Label(window,text="标签2",relief="raised")
lable4 = Label(window,text="标签4",relief="raised")
lable5 = Label(window,text="标签5",relief="raised")
lable8 = Label(window,text="标签8",relief="raised")

lable1.grid(row=0,column=1)
lable2.grid(row=0,column=1,columnspan=2,rowspan=2)
lable4.grid(row=0,column=3)
lable5.grid(row=1,column=0)
lable8.grid(row=1,column=3)

window.mainloop()
