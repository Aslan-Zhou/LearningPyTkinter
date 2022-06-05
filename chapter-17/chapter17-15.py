from tkinter import *

root = Tk()
root.title("17-15")
root.geometry("300x180")

text = Text(root)

for i in range(10):
    text.insert(END, str(i) + ' Python GUI设计王者归来 \n')

text.mark_set("mark1", "5.0")
text.mark_set("mark2", "8.0")

text.tag_add("tag1", "mark1", "mark2")
text.tag_config("tag1", foreground="blue", background="lightgreen")
text.pack(fill=BOTH, expand=True)

if __name__ == '__main__':
    mainloop()
