from tkinter import *

def show():
    array = []
    array_new = str(AccountE.get()).split(',')
    for i in array_new:
        array.append(int(i))
    result.config(text=bubble_sort(array))

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
    AccountE.delete(0,END)


root = Tk()
root.title("排序")
root.geometry("410x240")
root.configure(bg="aquamarine")
Label(root,text="我的排序小程序",bg="aquamarine").grid(row=0,column=1,columnspan=3)
AccountL = Label(root,text="""          输入要排序的数组，用逗号分隔，最后不用加逗号：""",
                 bg="aquamarine",height=2,anchor="sw")
AccountL.grid(row=1,column=1,columnspan=3)
AccountE = Entry(root,width=30)
AccountE.grid(row=3,column=1,columnspan=3)
resultL = Label(root,text=" 排序结果：",
                bg="aquamarine",height=2,anchor="sw")
resultL.grid(row=5,column=1)
result = Label(root,bg="#C0C0C0",width=30)
result.grid(row=7,column=1,columnspan=3)

sort_button = Button(root,text="排序",command=show,
                     bg="lawngreen",width=5)
sort_button.grid(row=9,column=1,pady=12)
empty_button = Button(root,text="清空",command=clear,
                      bg="lawngreen",width=5)
empty_button.grid(row=9,column=3,padx=15,pady=12)

mainloop()
