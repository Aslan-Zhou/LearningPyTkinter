from tkinter import *

window = Tk()
window.title("ch3-25")
lable1 = Label(window,text="明志科技大学",
               bg="lightyellow",width=15)
lable2 = Label(window,text="长庚大学",
               bg="lightgreen",width=15)
lable3 = Label(window,text="长庚科技大学",
               bg="lightblue",width=15)
lable1.grid(row=0,column=0)
lable2.grid(row=1,column=2)
lable3.grid(row=2,column=1)

window.mainloop()
