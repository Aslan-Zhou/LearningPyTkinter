from tkinter import *

window = Tk()
"""window.title("ch3-37")
window.geometry("640x480")
"""
window.rowconfigure(1,weight=1)
window.columnconfigure(0,weight=1)

"""SJ = PhotoImage(file="SJ.gif.gif")"""
lable1 = Label(window,bg="green",width=100)#image=SJ
lable1.grid(row=1,column=0,columnspan=2,
            sticky=N+E+W+S)
"""place(x=20,y=30,width=200,height=120)"""

"""wacky_ball = PhotoImage(file="wacky_ball.gif")
lable2 = Label(window,image=wacky_ball)
lable2.place(x=200,y=200,width=400,height=240)"""


window.mainloop()
