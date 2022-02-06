from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.configure(bg='#8AF681')
# root.iconbitmap("icons8-ok-16.ico")
im = Image.open("icons8-ok-16.ico")
img = ImageTk.PhotoImage(im)
root.tk.call('wm', 'iconphoto', root._w, img)

root.mainloop()
