from tkinter import *
from tkinter.ttk import Frame, Style

root = Tk()
root.title("ch8-6")
style = Style()
style.theme_use("alt")

Frame(root, width=150, height=80, relief="flat").grid(row=0, column=0, padx=5, pady=5)
Frame(root, width=150, height=80, relief="groove").grid(row=0, column=1, padx=5, pady=5)
Frame(root, width=150, height=80, relief="raised").grid(row=0, column=2, padx=5, pady=5)
Frame(root, width=150, height=80, relief="ridge").grid(row=1, column=0, padx=5, pady=5)
Frame(root, width=150, height=80, relief="solid").grid(row=1, column=1, padx=5, pady=5)
Frame(root, width=150, height=80, relief="sunken").grid(row=1, column=2, padx=5, pady=5)

mainloop()
