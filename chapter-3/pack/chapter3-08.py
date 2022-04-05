from tkinter import *

window = Tk()
window.title("ch3-8")
lable1 = Label(window,text="明志科技大学",
               bg="lightyellow",width=15)
lable2 = Label(window,text="长庚大学",
               bg="lightgreen",width=15)
lable3 = Label(window,text="长庚科技大学",
               bg="lightblue",width=15)
lable1.pack(padx=50)
lable2.pack(padx=50)
lable3.pack(padx=50)

window.mainloop()
