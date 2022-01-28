from tkinter import *

window = Tk()
window.title("ch3-11")
label1 = Label(window,text="明志科技大学",
               bg="lightyellow")
label2 = Label(window,text="长庚大学",
               bg="lightblue")
label3 = Label(window,text="长庚科技大学",
               bg="lightgreen")
label1.pack()
label2.pack(ipadx=10)
label3.pack(ipady=10)

window.mainloop()
