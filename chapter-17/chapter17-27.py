from tkinter import *
from tkinter.filedialog import asksaveasfilename


def Newfile():
    text.delete("1.0", END)
    root.title("Untiled")


def OpenFile():
    global filename
    filename = asksaveasfilename()
    if filename == '':
        return
    with open(filename, "r") as fileObj:
        conter = fileObj.read()
    text.delete("1.0", END)
    text.insert(END, conter)
    root.title(filename)


def SaveAs_file():
    global filename
    textContent = text.get("1.0", END)
    filename = asksaveasfilename(defaultextension=".txt")
    if filename == "":
        return
    with open(filename, "w") as output:
        output.write(textContent)
        root.title(filename)


filename = "Untiled"
root = Tk()
root.title(filename)
root.geometry("300x180")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=Newfile)
filemenu.add_command(label="open File", command=OpenFile)
filemenu.add_command(label="Save As", command=SaveAs_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
root.config(menu=menubar)

text = Text(root, undo=True)
text.pack(fill=BOTH, expand=True)

if __name__ == '__main__':
    mainloop()
