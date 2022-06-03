from tkinter import *



def status():
    if demoStatus.get():
        statusLabel.pack(side=BOTTOM, fill=X)
    else:
        statusLabel.pack_forget()


root = Tk()
root.title('ch16-10')
root.geometry('300x180')

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit" ,command=root.destroy)

viewmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="View", menu=viewmenu)
demoStatus = BooleanVar()
demoStatus.set(True)
viewmenu.add_checkbutton(label="Status", command=status,
                         variable=demoStatus)
root.config(menu=menubar)

statusVar = StringVar()
statusVar.set("显示")
statusLabel = Label(root, textvariable=statusVar, relief="raised")
statusLabel.pack(side=BOTTOM, fill=X)
if __name__ == '__main__':
    mainloop()
