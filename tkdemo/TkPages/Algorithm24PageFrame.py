from tkinter import *


class Algorithm24PageFrame(Frame):
    def __init__(self, root):
        super().__init__(root, bg='white')
        self.label = Label(self, text="该功能暂时\n不支持使用", fg='blue',
                           bg='white', font='Times 28 bold')
        self.label.grid(padx=100, pady=180)
