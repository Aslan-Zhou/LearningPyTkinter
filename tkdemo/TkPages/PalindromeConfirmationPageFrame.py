from tkinter import *
from TkPagesEvent.PalindromeConfirmationPageHandle import *


class PalindromeConfirmationPageFrame(Frame):
    def __init__(self, root):
        super().__init__(root, bg='white')
        self.drawPage()

    def drawPage(self):
        Label(self, bg='white', text='回 文 确 定 器', font='Helvetic 22 bold',
              fg='blue').grid(row=0, column=1, pady=40, columnspan=2)
        self.entry = Entry(self, width=24, font='Helvetic 20 bold')
        self.entry.grid(row=1, column=0, padx=15, pady=10, columnspan=4)
        self.button1 = Button(self, text='判断', width=8, font='Times 14 bold',
                              height=2, command=self.cal, bg='lightblue')
        self.button1.grid(row=2, column=0, columnspan=2, pady=25)

        self.button2 = Button(self, text='清空', width=8, font='Times 14 bold',
                              height=2, command=self.delete, bg='lightblue')
        self.button2.grid(row=2, column=2, columnspan=2, pady=25)
        self.var = StringVar()
        self.label = Label(self, bg='lightgreen', fg="blue", font='''Times
                    22 bold''', textvariable=self.var, width=22)
        self.label.grid(row=3, column=0, columnspan=4, pady=30)

    def delete(self):
        self.entry.delete(0, END)
        self.var.set(" ")

    def cal(self):
        self.var.set(str(PalindromeConfirmationPageHandle(
            self.entry.get()).checkHandle()))
