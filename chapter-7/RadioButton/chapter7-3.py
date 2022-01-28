from tkinter import *

def printSelection():
    print(cities[var.get()])
root = Tk()
root.title("ch7-3")
cities = {0:"北京",1:"纽约",2:"巴黎",3:"伦敦",4:"东京"}
var = IntVar()
var.set(0)

Label(root,text="选择最喜欢的城市",bg="yellow",
              fg="blue",width=30).pack()
for val,city in cities.items():
    Radiobutton(root,text=city,
    variable=var,value=val,
    command=printSelection).pack()


mainloop(0)
