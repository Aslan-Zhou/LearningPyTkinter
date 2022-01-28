from tkinter import *

def bColor(bgColor):
    root.config(bg=bgColor)


root = Tk()
root.title("ch4-5-1")
root.geometry("300x200")

Yellow_button = Button(root,text="Yellow",command=lambda :bColor("yellow"))
Blue_button = Button(root,text="Blue",command=lambda :bColor("blue"))
Red_button = Button(root,text="Red",command=lambda :bColor("red"))
Green_button = Button(root,text="Green",command=lambda :bColor("green"))
Exit_button=Button(root,text="Exit",command=root.destroy)

Yellow_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)
Blue_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)
Red_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)
Green_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)
Exit_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)


mainloop()
