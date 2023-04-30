from tkinter import *
from TkPagesEvent.FractionExpressionPageHandle import *


class FractionExpressionPageFrame(Frame):
    def __init__(self, root):
        super().__init__(root, bg='white')
        self.frame = Frame(self, bg='white')
        Label(self, bg='white', text='分 数 计 算 器',
              font='Helvetic 20 bold', fg='blue'
              ).grid(row=0, column=1, pady=40, columnspan=3)
        self.fraction1()
        self.fraction2()
        self.sign()
        self.return_value()
        self.buttons()
        self.frame.grid(row=1, column=0, columnspan=5)

    def fraction1(self):
        self.entry1 = Entry(self.frame, width=3)
        self.entry1.grid(row=1, column=0, padx=15, pady=10)
        Label(self.frame, bg='white', text='/').grid(row=1, column=1, padx=10)
        self.entry2 = Entry(self.frame, width=3)
        self.entry2.grid(row=1, column=2, padx=15, pady=10)

    def fraction2(self):
        self.entry3 = Entry(self.frame, width=3)
        self.entry3.grid(row=1, column=4, padx=15, pady=10)
        Label(self.frame, text='/', bg='white').grid(row=1, column=5, padx=10)
        self.entry4 = Entry(self.frame, width=3)
        self.entry4.grid(row=1, column=6, padx=15, pady=10)

    def sign(self):
        self.omTuple = ("+", "-", "*", "/")
        self.var1 = StringVar()
        self.var1.set(self.omTuple[0])
        self.option = OptionMenu(self.frame, self.var1, *self.omTuple)
        self.option.grid(row=1, column=3, padx=15, pady=10)

    def buttons(self):
        self.button1 = Button(self, text='计算', bg='lightblue', font='''Times
                    12 bold''', width=3, command=self.cal)
        self.button1.grid(row=2, column=0, columnspan=2, pady=20)

        self.button2 = Button(self, text='清空', width=3, font='''Times
                    12 bold''', command=self.delete, bg='lightblue')
        self.button2.grid(row=2, column=3, columnspan=2, pady=20)

    def return_value(self):
        self.var2 = StringVar()
        self.label1 = Label(self, bg='lightgreen', fg="blue", font='''Times
                    16 bold''', textvariable=self.var2, width=24)
        self.label1.grid(row=3, column=1, columnspan=3, padx=15, pady=25)

    def delete(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.var2.set("")

    def cal(self):
        f1 = Fraction(int(self.entry1.get()), int(self.entry2.get()))
        f2 = Fraction(int(self.entry3.get()), int(self.entry4.get()))
        symbol = self.var1.get()
        if symbol == '+':
            self.var2.set((str(f1) + " " + symbol + ' '
                           + str(f2) + " = " + str(f1 + f2)))
        elif symbol == '-':
            self.var2.set((str(f1) + " " + symbol + ' '
                           + str(f2) + " = " + str(f1 - f2)))
        elif symbol == '*':
            self.var2.set((str(f1) + " " + symbol + ' '
                           + str(f2) + " = " + str(f1 * f2)))
        else:
            self.var2.set((str(f1) + " " + symbol + ' '
                           + str(f2) + " = " + str(f1 / f2)))
