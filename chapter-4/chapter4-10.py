from tkinter import *

root = Tk()
root.title("ch4-10")
label = Label(root,text="",bg="yellow",width=20)
botton7 = Button(root,text="7",width=3)
botton8 = Button(root,text="8",width=3)
botton9 = Button(root,text="9",width=3)
bottonM = Button(root,text="*",width=3)
botton4 = Button(root,text="4",width=3)
botton5 = Button(root,text="5",width=3)
botton6 = Button(root,text="6",width=3)
bottonS = Button(root,text="-",width=3)
botton1 = Button(root,text="1",width=3)
botton2 = Button(root,text="2",width=3)
botton3 = Button(root,text="3",width=3)
bottonP = Button(root,text="+",width=3)
botton0 = Button(root,text="0",width=8)
bottonD = Button(root,text=".",width=3)
bottonE = Button(root,text="=",width=3)

label.grid(row=0,column=0,columnspan=4)
botton7.grid(row=1,column=0,padx=5)
botton8.grid(row=1,column=1,padx=5)
botton9.grid(row=1,column=2,padx=5)
bottonM.grid(row=1,column=3,padx=5)
botton4.grid(row=2,column=0,padx=5)
botton5.grid(row=2,column=1,padx=5)
botton6.grid(row=2,column=2,padx=5)
bottonS.grid(row=2,column=3,padx=5)
botton1.grid(row=3,column=0,padx=5)
botton2.grid(row=3,column=1,padx=5)
botton3.grid(row=3,column=2,padx=5)
bottonP.grid(row=3,column=3,padx=5)
botton0.grid(row=4,column=0,padx=5,columnspan=2)
bottonD.grid(row=4,column=2,padx=5)
bottonE.grid(row=4,column=3,padx=5)

mainloop()
