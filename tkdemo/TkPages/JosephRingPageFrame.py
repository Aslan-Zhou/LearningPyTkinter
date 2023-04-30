from tkinter import *
from TkPagesEvent.JosephRingPageHandle import *
from tkinter.scrolledtext import ScrolledText


class JosephRingPageFrame(Frame):
    def __init__(self, root):
        super().__init__(root, bg='white')
        self.drawPage()
        self.pack(fill=BOTH, expand=True)

    def drawPage(self):
        Label(self, bg='white').grid()
        Label(self, fg='blue', font="Helvetic 22 bold", text='约瑟夫环',
              bg='white').grid(column=1, row=0, columnspan=6, pady=30)

        self.Label1()
        self.Label2()
        self.Label3()

        Button(self, text="清空", bg="lightblue", fg="Red", font='Helvetic 10 bold',
               command=self.delete).grid(row=2, column=1, columnspan=3, pady=20)
        Button(self, text="计算", bg="lightblue", fg="Red", font='Helvetic 10 bold',
               command=self.expressionValue).grid(row=2, column=4, pady=20, columnspan=43)

        self.var = StringVar()
        self.label = Label(self, textvariable=self.var, bg='lightgreen',
                           font="Helvetic 18 bold", width=26)
        self.label.grid(column=1, row=3, columnspan=6, pady=20)

        self.text = ScrolledText(self, width=50, height=10)
        self.text.grid(row=4, column=1, columnspan=6)

    def Label1(self):
        Label(self, text='起始编号', font="Helvetic 14 bold",
              bg='white').grid(column=1, row=1)
        self.entry1 = Entry(self, width=4, bg='lightblue')
        self.entry1.grid(column=2, row=1, pady=10)

    def Label2(self):
        Label(self, text='终止编号', font="Helvetic 14 bold",
              bg='white').grid(column=3, row=1)
        self.entry2 = Entry(self, width=4, bg='lightblue')
        self.entry2.grid(column=4, row=1, pady=10)

    def Label3(self):
        Label(self, text='出列编号', font="Helvetic 14 bold",
              bg='white').grid(column=5, row=1)
        self.entry3 = Entry(self, width=4, bg='lightblue')
        self.entry3.grid(column=6, row=1, pady=10)

    def delete(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.text.delete(1.0, END)
        self.var.set(" ")

    def expressionValue(self):
        self.text.delete(CURRENT, END)
        if len(self.entry1.get()) <= 3 and len(self.entry2.get()) <= 3 and len(self.entry3.get()) <= 3:
            numlist = list(range(int(self.entry1.get()), (int(self.entry2.get()) + 1)))

            self.last, self.kill_list = JosephRingPageHandle(numlist, int(self.entry3.get()) - 1).josephRingHandle()
            for i in range(len(self.kill_list)):
                self.text.insert(END, self.kill_list[i]+'\n')

            self.var.set('最后的赢家是' + self.last + '号!')
        else:
            self.var.set("数值太大!")
