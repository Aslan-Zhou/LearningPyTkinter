from tkinter import *

root = Tk()
root.title("ch19-12")

canvas = Canvas(root, width=640, height=480)
canvas.pack()
canvas.create_text(200, 50, text='Ming-Chi Institute of Technology')
canvas.create_text(200, 80,
                   text='''Ming-Chi Institute of Technology''',
                   fill='blue')
canvas.create_text(300, 120,
                   text='''Ming-Chi  Institute of Technology''',
                   fill="blue", font=('Old English Text MT', 20))
if __name__ == '__main__':
    mainloop()
