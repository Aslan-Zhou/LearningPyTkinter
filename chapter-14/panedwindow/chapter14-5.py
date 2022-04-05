from tkinter import *

pw = PanedWindow(orient=HORIZONTAL)
pw.pack(fill=BOTH, expand=True)

entry = Entry(pw, bd=3)
pw.add(entry)

pwin = PanedWindow(pw, orient=VERTICAL)
pw.add(pwin)

scale = Scale(pwin, orient=HORIZONTAL)
pwin.add(scale)
if __name__ == '__main__':
    mainloop()
