from tkinter import *

counter = 0
def run_counter(digit):
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1,counting)
    counting()
root = Tk()
root.title("ch4-4")
digit = Label(root,bg="lightyellow",fg="blue",
              height=20,width=40,
              font="Helvetic 20 bold")

digit.pack()
run_counter(digit)
Button(root,text="结束",width=25,command=root.destroy).pack(pady=10)

root.mainloop()
