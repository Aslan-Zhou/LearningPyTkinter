from tkinter import *

window = Tk()
window.title("ch3-30")
lable1 = Label(window,text="标签1",relief="raised")
lable2 = Label(window,text="标签2",relief="raised")
lable3 = Label(window,text="标签3",relief="raised")
lable4 = Label(window,text="标签4",relief="raised")
lable5 = Label(window,text="标签5",relief="raised")
lable6 = Label(window,text="标签6",relief="raised")
lable7 = Label(window,text="标签7",relief="raised")
lable8 = Label(window,text="标签8",relief="raised")

lable1.grid(row=0,column=0,padx=5,pady=5)
lable2.grid(row=0,column=1,padx=5,pady=5)
lable3.grid(row=0,column=2,padx=5,pady=5)
lable4.grid(row=0,column=3,padx=5,pady=5)
lable5.grid(row=1,column=0,padx=5,pady=5)
lable6.grid(row=1,column=1,padx=5,pady=5)
lable7.grid(row=1,column=2,padx=5,pady=5)
lable8.grid(row=1,column=3,padx=5,pady=5)

window.mainloop()
