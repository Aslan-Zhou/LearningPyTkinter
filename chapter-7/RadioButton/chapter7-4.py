from tkinter import *

def printSelection():
    print(cities[var.get()])
root = Tk()
root.title("ch7-4")
cities = {0:"the People's Republic of China",1:"American Republic",2:"France",3:"England",4:"Japan"}
var = IntVar()
var.set(0)

Label(root,text="选择最喜欢的国家",bg="yellow",
              fg="blue",width=30).pack()
for val,city in cities.items():
    Radiobutton(root,text=city,width=30,
                indicatoron=0,
                variable=var,value=val,
                command=printSelection).pack()


mainloop(0)
