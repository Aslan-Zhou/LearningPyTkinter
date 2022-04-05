from tkinter import *

window = Tk()
window.title("ch3-6")
lable1 = Label(window,text="明志科技大学",
               bg="lightyellow",width=15)
lable2 = Label(window,text="长庚大学",
               bg="lightgreen",width=15)
lable3 = Label(window,text="长庚科技大学",
               bg="lightblue",width=15)
lable1.pack(fill=X)
lable2.pack(pady=10)
lable3.pack(fill=X)

window.mainloop()
