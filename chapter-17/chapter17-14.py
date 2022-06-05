from tkinter import *

root = Tk()
root.title("17-14")
root.geometry("300x180")

text = Text(root)

for i in range(10):
    text.insert(END, str(i+1) + ' Python GUI设计王者归来 \n')

text.mark_set("mark1", "5.0")
text.mark_set("mark2", "8.0")

print(text.get("mark1", "mark2"))
text.pack(fill=BOTH, expand=True)

if __name__ == '__main__':
    mainloop()
