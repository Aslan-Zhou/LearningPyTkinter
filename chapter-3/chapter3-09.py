from tkinter import *

window = Tk()
window.title("ch3-9")
label1 = Label(window,text="明志科技大学",
               bg="lightyellow",width=15)
label2 = Label(window,text="长庚大学",
               bg="lightblue",width=15)
label3 = Label(window,text="长庚科技大学",
               bg="lightgreen",width=15)
label1.pack(side=LEFT)
label2.pack(side=LEFT,padx=10)
label3.pack(side=LEFT)

window.mainloop()
