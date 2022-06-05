from tkinter import *
from tkinter import messagebox


def spellingCheck():
    text.tag_remove("spellErr", "1.0", END)
    textwords = text.get("1.0", END).split()
    print("字典内容\n", textwords)
    startChar = "("
    endChar = (".", ",", ":", ";", "?", "!", ")")
    start = "1.0"
    for word in textwords:
        if word[0] in startChar:
            word = word[1:]
        if word[-1] in endChar:
            word = word[:1]
        if word not in dicts and word.lower() not in dicts:
            print("error", word)
            pos = text.search(word, start, END)
            text.tag_add("found", pos, "%s+%dc" % (pos, len(word)))
            start = "%s+%dc" % (pos, len(word))


def clearText():
    text.tag_remove("spellErr", "1.0", END)


root = Tk()
root.title("17-22")
root.geometry("300x180")
toolbar = Frame(root, relief=RAISED, borderwidth=1)
toolbar.pack(side=TOP, fill=X, padx=2, pady=1)

Button(toolbar, text="检查", command=spellingCheck
       ).pack(side=LEFT, padx=5, pady=5)
Button(toolbar, text="清理", command=clearText
       ).pack(side=LEFT, padx=5, pady=5)

text = Text(root, undo=True)
text.pack(fill=BOTH, expand=True)
text.insert(END, "Five Hundred Miles\n")
text.insert(END, "If you miss the rain I'm on, \n")
text.insert(END, "You will now that I am gone.\n")
text.insert(END, "You can hear the while bow\n")
text.insert(END, "A Hund red miles, \n")
text.tag_configure("spellErr", foreground="red")
with open("myDict.txt", "r") as dictObj:
    dicts = dictObj.read().split("\n")
if __name__ == '__main__':
    mainloop()
