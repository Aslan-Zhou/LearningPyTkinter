from tkinter import *


def paint(event):
    x1, y1 = event.x, event.y
    x2, y2 = event.x, event.y
    canvas.create_oval(x1, y1, x2, y2, fill='blue')


def cls():
    canvas.delete('all')


root = Tk()
root.title("ch19-15")
Label(root, text="拖拽鼠标可以绘图").pack()
canvas = Canvas(root, width=640, height=300)
canvas.pack()
Button(root, text='清除', command=cls).pack(pady=5)
canvas.bind("<B1-Motion>", paint)
if __name__ == '__main__':
    mainloop()
