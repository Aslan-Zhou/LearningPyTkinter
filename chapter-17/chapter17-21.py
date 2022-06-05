from tkinter import *


def mySearch():
    text.tag_remove("found", "1.0", END)
    start = "1.0"
    key = entry.get()

    if len(key.strip()) == 0:
        return
    while True:
        pos = text.search(key, start, END)
        if pos == "":
            break
        text.tag_add("found", pos, "%s+%dc" % (pos, len(key)))
        start = "%s+%dc" % (pos, len(key))


root = Tk()
root.title("17-21")
root.geometry("300x180")
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
entry = Entry()
entry.grid(row=0, column=0, padx=5, sticky=W+E)
Button(root, text="查找", command=mySearch
       ).grid(row=0, column=1, padx=5, pady=5)


text = Text(root, undo=True)
text.grid(row=1, column=0, columnspan=2,
          padx=3, pady=5, sticky=N+S+W+E)
text.insert(END, "Five Hundred Miles\n")
text.insert(END, "If you miss the rain I'm on, \n")
text.insert(END, "You will know that I am gone.\n")
text.insert(END, "You can hear the whistle blow\n")
text.insert(END, "A Hundred miles, \n")
text.tag_configure("found", background="yellow")
if __name__ == '__main__':
    mainloop()
