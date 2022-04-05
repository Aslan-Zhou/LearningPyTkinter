from tkinter import *

root = Tk()
root.title("ch8-3")

frameUpper = Frame(root, bg="lightyellow")
frameUpper.pack()
buttonRed = Button(frameUpper, text="Red", fg="red")
buttonRed.pack(side=LEFT, padx=5, pady=5)
buttonGreen = Button(frameUpper, text="Green", fg="green")
buttonGreen.pack(side=LEFT, padx=5, pady=5)
buttonBlue = Button(frameUpper, text="Blue", fg="blue")
buttonBlue.pack(side=LEFT, padx=5, pady=5)

frameLower = Frame(root, bg="lightblue")
frameLower.pack()
buttonPurple = Button(frameLower, text="Purple", fg="purple")
buttonPurple.pack(side=LEFT, padx=5, pady=5)

mainloop()
