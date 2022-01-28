from tkinter import *

window = Tk()
window.title("ch3-33")
label1 = Label(window,text="明志工专",relief="raised")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="明志科技大学",relief="raised")
label4 = Label(window,bg="aqua",width=20)

label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)
window.mainloop()
