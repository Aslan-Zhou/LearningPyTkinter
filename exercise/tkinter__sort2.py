from tkinter import *

def show():
    array = []
    array_new = str(entry.get()).split(',')
    for i in array_new:
        array.append(int(i))
    result.config(text=bubble_sort(array))
    readonly()

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                k = array[j]
                array[j] = array[j-1]
                array[j-1] = k

    return array

def clear():
    result.config(text="")
    entry.delete(0,END)

def readonly():
    if var.get():
        entry.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)

root = Tk()
root.title("排序")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 420;h = 250
x = (screenWidth - w) / 2
y = (screenHeight - h) / 2
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.configure(bg="aquamarine")

Label(root,text="我的排序小程序",bg="aquamarine").grid(row=0,column=1,columnspan=3)
Label(root,text="""          输入要排序的数组，用逗号分隔，最后不用加逗号：""",
      bg="aquamarine",height=2,anchor="sw"
      ).grid(row=1,column=1,columnspan=3)

entry = Entry(root,width=30)
entry.grid(row=3,column=1,columnspan=3)
resultL = Label(root,text=" 排序结果：",
                bg="aquamarine",height=2,anchor="sw")
var = BooleanVar()
var.set(True)
readonly()
Checkbutton(root,text="只读",variable=var,command=readonly,relief="raised",
            bg="aquamarine").grid(row=3,column=3,padx=5,pady=5)

resultL.grid(row=5,column=1)
result = Label(root,bg="#C0C0C0",width=30)
result.grid(row=7,column=1,columnspan=3)

sort_button = Button(root,text="排序",command=show,
                     bg="lawngreen",width=5)
sort_button.grid(row=9,column=1,pady=5)
empty_button = Button(root,text="清空",command=clear,
                      bg="lawngreen",width=5)
empty_button.grid(row=9,column=2,padx=5,pady=5)

button_Quit = Button(root,text="结束",command=root.destroy,width=5,
    bg="lawngreen")
button_Quit.grid(row=9,column=3,padx=5,pady=5,sticky=W)

mainloop(0)
