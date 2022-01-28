from tkinter import *

counter = 11
def run_counter(digit):
    def counting():
        global counter
        counter *= 11
        digit.config(text=str(counter))
        digit.after(1000,counting)
    counting()
root = Tk()
root.title("ch2-22")
root.geometry("1600x900")
digit = Label(root,bg="lightyellow",fg="blue",
              height=1000,width=500,
              font="Helvetic 20 bold")

digit.pack()
run_counter(digit)

root.mainloop()
