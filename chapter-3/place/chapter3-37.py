from tkinter import *

window = Tk()
window.title("ch3-37")
window.geometry("640x480")

SJ = PhotoImage(file="abc.png")
label1 = Label(window,image=SJ)
label1.place(x=20,y=30,width=500,height=120)

wacky_ball = PhotoImage(file="beach_ball.png")
label2 = Label(window,image=wacky_ball)
label2.place(x=200,y=200,width=400,height=240)

window.mainloop()
