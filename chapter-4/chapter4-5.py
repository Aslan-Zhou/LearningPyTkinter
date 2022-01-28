from tkinter import *

def Yellow():
    root.config(bg="yellow")
def Blue():
    root.config(bg="blue")
def Red():
    root.config(bg="red")
def Green():
    root.config(bg="green")


root = Tk()
root.title("ch4-5")
root.geometry("300x200")

Yellow_button = Button(root,text="Yellow",command=Yellow)
Blue_button = Button(root,text="Blue",command=Blue)
Red_button = Button(root,text="Red",command=Red)
Green_button = Button(root,text="Green",command=Green)
Exit_button=Button(root,text="Exit",command=root.destroy)

Yellow_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)
Blue_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)
Red_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)
Green_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)
Exit_button.pack(anchor=S,side=RIGHT,padx=5,pady=5)


mainloop()
