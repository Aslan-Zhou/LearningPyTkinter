from tkinter import *


def bubblesort(nums):
    if len(nums) < 2:
        return var.set(nums)
    else:
        for i in range(0, len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] < nums[j - 1]:
                    value = nums[j]
                    nums[j] = nums[j - 1]
                    nums[j - 1] = value

    return var.set(nums)


def selectsort(nums):
    for i in range(0, len(nums)):
        minNum = nums[i]
        minNumIndex = i
        for j in range(i, len(nums)):
            if minNum > nums[j]:
                minNum = nums[j]
                minNumIndex = j

        tmpValue = nums[i]
        nums[i] = nums[minNumIndex]
        nums[minNumIndex] = tmpValue

    return var.set(nums)


def insertionsort(nums):
    for i in range(1, len(nums)):

        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                tmpValue = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = tmpValue
            else:
                break
    return var.set(nums)


def clear():
    label.config(text="")
    entry.delete(0, END)


root = Tk()
root.title("tk")
root.geometry("400x200")
root.configure(bg="#00BFFF")

Label(root, text="      我的排序小程序", bg="#00BFFF").grid(row=0, column=0)
entry = Entry(root, width=30)
entry.grid(row=1, column=1, columnspan=4)
var = StringVar()
label = Label(root, text="排序结果", width=10, bg="#00BFFF")
label.grid(row=2, columnspan=1)
label = Label(root, width=30, textvariable=var)
label.grid(row=3, column=1, columnspan=4, padx=10)

label = Label(root, width=10, bg="#00BFFF")
label.grid(row=4, columnspan=1)
Button(root, text="冒泡排序", bg="#00BFFF", command=lambda: bubblesort(entry.get().split(','))).grid(row=5, column=0)
Button(root, text="插入排序", bg="#00BFFF", command=lambda: insertionsort(entry.get().split(','))).grid(row=5, column=1)
Button(root, text="选择排序", bg="#00BFFF", command=lambda: selectsort(entry.get().split(','))).grid(row=5, column=3)
Button(root, text="清空", bg="#00BFFF", command=clear).grid(row=6, column=0)
Button(root, text="退出", bg="#00BFFF", command=root.destroy).grid(row=6, column=2)
if __name__ == '__main__':
    mainloop()
