from tkinter import *

window = Tk()
window.title("ch3-1")
lable1 = Label(window,text="明志科技大学",
               bg="lightyellow")
lable2 = Label(window,text="长庚大学",
               bg="lightgreen")
lable3 = Label(window,text="长庚科技大学",
               bg="lightblue")
lable1.pack()
lable2.pack()
lable3.pack()

window.mainloop()
