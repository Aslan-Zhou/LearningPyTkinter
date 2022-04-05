from tkinter import *

window = Tk()
window.title("ch3-36")
lable1 = Label(window,text="明志科技大学",
               bg="lightyellow",width=15)
lable2 = Label(window,text="长庚大学",
               bg="lightgreen",width=15)
lable3 = Label(window,text="长庚科技大学",
               bg="lightblue",width=15)
lable1.place(x=0,y=0)
lable2.place(x=30,y=50)
lable3.place(x=60,y=100)

window.mainloop()
