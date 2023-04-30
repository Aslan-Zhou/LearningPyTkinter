from tkinter import *

root = Tk()
root.geometry("500x130+980+520")
root.title("Calculate Expression")
root.config(bg='lightgreen')
var1 = StringVar()
var1.set('请使用"+, -, *, /, (, )"组成表达式:')
Label(root, textvariable=var1, bg='lightgreen',
      fg="blue", font="Helvetic 18 bold"
      ).grid(column=1, row=0, columnspan=4)
entry = Entry(root, width=28, bg='lightgreen', fg="Red")
entry.grid(column=1, row=1, padx=10, columnspan=3)
Button(root, text="清空", bg='lightblue').grid(row=1, column=4)
Label(root, text="         ", bg='lightgreen'
      ).grid(row=2, column=0, padx=10)
Button(root, text="计算", bg='lightblue').grid(row=2, column=1)

var2 = StringVar()
Label(root, textvariable=var2, bg='lightgreen',
      fg="blue", font="Helvetic 18 bold"
      ).grid(column=2, row=2, columnspan=4)

if __name__ == '__main__':
    mainloop()
