from tkinter import *

window = Tk()
window.title("ch3-39")
window.geometry("640x480")

SJ = PhotoImage(file="beach_ball.png")
label = Label(window,image=SJ)
label.place(relx=0.1,rely=0.1,relheight=0.8)


window.mainloop()
