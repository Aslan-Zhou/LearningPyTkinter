from tkinter import *


def selectedText():
    print("INSERT :", text.index(INSERT))
    print("CURRENT: ", text.index(CURRENT))
    print("END    : ", text.index(END))


root = Tk()
root.title("17-12")

Button(root, text="Print selection", command=selectedText).pack(pady=3)

text = Text(root)
text.pack(fill=BOTH, expand=True, pady=2, padx=3)
text.insert(END, "Love You Like A Love Song")
text.insert(END, "梦醒时分")

if __name__ == '__main__':
    mainloop()
