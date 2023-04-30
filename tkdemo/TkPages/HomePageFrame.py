from tkinter import *


class HomePageFrame(Frame):
    def __init__(self, root):
        super().__init__(root, bg='white')
        self.root = root
        self.root.config(bg="white")
        self.label = Label(self, bg='white', text="欢迎回到[我的练习册]!",
                           anchor=CENTER, font="Helvetic 20 bold", fg='blue')
        self.label.pack(pady=180)
