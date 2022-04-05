from tkinter import *

root = Tk()
root.title("ch14-2")

pw = PanedWindow(orient=HORIZONTAL)
leftframe = LabelFrame(pw, text="Left Pane", width=120, height=150)
pw.add(leftframe)
middleframe = LabelFrame(pw, text="Middle Pane", width=120, height=150)
pw.add(middleframe)
rightframe = LabelFrame(pw, text="Right Pane", width=120, height=150)
pw.add(rightframe)

pw.pack(fill=BOTH, expand=True, pady=10, padx=10)
if __name__ == '__main__':
    mainloop()
