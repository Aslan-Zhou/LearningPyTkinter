from tkinter import *

pw = PanedWindow(orient=VERTICAL)
pw.pack(fill=BOTH, expand=True)

top = Label(pw, text="top Pane")
pw.add(top)

bottom = Label(pw, text="Bottom Pane")
pw.add(bottom)
if __name__ == '__main__':
    mainloop()
