from tkinter import *

root = Tk()
root.title("17-12")

text = Text(root)
text.pack(fill=BOTH, expand=True, pady=2, padx=3)
text.insert(END, "Love You Like A Love Song")
text.insert(1.14, "梦醒时分")

if __name__ == '__main__':
    mainloop()
