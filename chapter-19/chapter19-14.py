from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch19-14")
image = Image.open("d.jpg")
d = ImageTk.PhotoImage(image)
canvas = Canvas(root, width=image.size[0] + 40,
                height=image.size[1] + 30)
canvas.create_image(20, 15, anchor=NW, image=d)
canvas.pack(fill=BOTH, expand=True)

if __name__ == '__main__':
    mainloop()
