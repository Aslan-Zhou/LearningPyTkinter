from tkinter import *
from tkinter.font import Font
from TkPagesEvent.AlgorithmExpressionPageHandle import *


class AlgorithmExpressionPageFrame(Frame):
    def __init__(self, root):
        super().__init__(root, bg='white')
        self.drawPage()
        self.pack(fill=BOTH, expand=True)

    def drawPage(self):
        Label(self, text='请使用"+, -, *, /, (, )"组成表达式:', bg='white',
              font="Helvetic 18 bold").grid(columnspan=4, pady=50)

        font = Font(size=20, family='Helvetic')
        self.entry = Entry(self, width=24, font=font, bg='lightblue')
        self.entry.grid(row=1, pady=10, columnspan=4)

        Button(self, text="清空", bg="lightblue", fg="Red", font='Helvetic 10 bold',
               command=self.delete).grid(row=2, column=3, pady=20)
        Label(self, text="").grid(row=2, column=0, padx=10)
        Button(self, text="计算", bg="lightblue", fg="Red", font='Helvetic 10 bold',
               command=self.expressionValue).grid(row=2, column=0, pady=20)

        self.var = StringVar()
        self.label = Label(self, textvariable=self.var, font="Helvetic 18 bold",
                           width=26, bg='lightgreen')
        self.label.grid(column=0, row=3, columnspan=4, pady=30)

    def delete(self):
        self.entry.delete(0, END)
        self.var.set(" ")

    def expressionValue(self):
        self.v = self.entry.get()
        algorithmExp = AlgorithmExpressionPageHandle(
            self.splitExpression())
        self.var.set(algorithmExp.postfixEval2())

    def splitExpression(self):
        self.v += ' '
        items = []
        i = 0
        while i < len(self.v):

            if self.v[i].isdigit():
                j = i + 1
                while self.v[i:j].isdigit() and j < len(self.v):
                    j += 1
                items.append(self.v[i:j - 1])
                i = j - 1

            elif self.v[i] in '+-*/()':
                items.append(self.v[i])
                i += 1
            elif self.v[i] == ' ':
                i += 1
            else:
                self.var.set('非法字符!')
                break
        return items
