from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("17-29")
root.geometry("1000x800")
img = Image.open("apple.jpg")
myphoto = ImageTk.PhotoImage(img)

text = Text(root)
text.image_create(END, image=myphoto)
text.insert(END, "\n")
text.insert(END, "洪锦魁年轻时留学美国拍摄于Chicago")
text.pack(fill=BOTH, expand=True)
if __name__ == '__main__':
    mainloop()
from tkinter import *

root = Tk()
root.title("17-")

text = Text(root)
text.pack()

if __name__ == '__main__':
    mainloop()
