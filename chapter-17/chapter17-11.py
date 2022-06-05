from tkinter import *


def selectedText():
    try:
        selText = text.get(SEL_FIRST, SEL_LAST)
        print("选取文字", selText)
        print("selectionstart: ", text.index(SEL_FIRST))
        print("selectionend: ", text.index(SEL_LAST))
    except TclError:
        print("没有选取文字")


root = Tk()
root.title("17-11")

Button(root, text="Print selection", command=selectedText).pack(pady=3)

text = Text(root)
text.pack(fill=BOTH, expand=True, pady=2, padx=3)
text.insert(END, "Love You Like A Love Song")

if __name__ == '__main__':
    mainloop()
