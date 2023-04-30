from tkinter import *
from tkinter import messagebox


class AboutPageFrame(Frame):
    def __init__(self, root):
        super().__init__(root, bg='white')
        self.root = root
        Button(self, text="关  于", bg="lightblue", fg='sienna', font='Times 24 bold',
               command=self.buttonMessage).grid(pady=180, padx=200, ipady=24, ipadx=32)

    def buttonMessage(self):
        m = messagebox.askyesno(message='欢迎使用本练习册!', icon='info')
        if m:
            self.toplevel = Toplevel()
            self.frame = Frame(self.toplevel, bg='#FFF5EE')
            Label(self.frame, text='帮助', bg='#FFF5EE',
                  fg='sienna', font='Times 10 bold').pack()
            self.text = Text(self.frame, height=9, width=30)
            self.text.pack()
            self.yscrollbar = Scrollbar(self.toplevel)
            self.yscrollbar.pack(side=RIGHT, fill=Y)
            self.yscrollbar.config(command=self.text.yview)
            self.text.config(yscrollcommand=self.yscrollbar.set)
            self.text.config(state=DISABLED)
            Button(self.frame, text='好   的', font='Times 10 bold', fg='sienna',
                   bg='lightblue', command=self.toplevel.destroy).pack(fill=X)
            self.frame.pack()
