from tkinter import *
import random
import time


def start():
    global timeNum, hintStr, hintVar
    hintStr = "请等待抽奖结果"
    hintVar.set(hintStr)
    label.config(textvariable=hintVar)
    label.grid(row=3, column=1, columnspan=3, pady=20)

    button.config(state=DISABLED)
    # dict1 奖励时间的字典, 用于打印字符串
    dict1 = {0: t1, 1: t2, 2: t3}
    # dict2 奖励时间的标签字典, 用于显示
    dict2 = {0: text1, 1: text2, 2: text3}

    n = random.randint(0, 99999)
    print(n)
    num = timeNum * 10
    while num > 0:
        num -= 1
        n += 1
        n %= 3
        dict2[n].config(bg="green")

        if num % 10 == 0:
            timeNum -= 1
            var.set(timeNum)
        root.update()

        time.sleep(0.1)
        text1.config(bg="gray")
        text2.config(bg="gray")
        text3.config(bg="gray")

    dict2[n].config(bg="green")
    hintStr = "你抽中了" + dict1[n] + "!"
    hintVar.set(hintStr)
    label.config(textvariable=hintVar)
    label.grid(row=3, column=1, columnspan=3, pady=20)
    button.config(state=NORMAL)
    timeNum = 10


root = Tk()
root.title("健身环抽奖")
root.geometry("360x330+780+560")
root.configure(bg="lightgreen")

t1 = "5小时"
t2 = "3小时"
t3 = "2小时"
text1 = Label(root, text=t1, font="Helvetic 20 bold", bg="gray")
text1.grid(row=2, column=1, padx=20, pady=3)
text2 = Label(root, text=t2, font="Helvetic 20 bold", bg="gray")
text2.grid(row=2, column=2, padx=20, pady=3)
text3 = Label(root, text=t3, font="Helvetic 20 bold", bg="gray")
text3.grid(row=2, column=3, padx=20, pady=3)
label2 = Label(root, bg="lightgreen", font="Helvetic 20 bold")
label2.grid(row=3, column=1, columnspan=3)

hintStr = "请开始您的抽奖!"
hintVar = StringVar()
hintVar.set(hintStr)
label = Label(root, textvariable=hintVar, font="Helvetic 20 bold", bg="lightgreen")
label.grid(row=3, column=1, columnspan=3, pady=20)

# num 用于倒计时开始的时间
timeNum = 10
var = IntVar()
var.set(timeNum)
lab = Label(root, textvariable=var, font="Helvetic 50 bold", bg="lightgreen", fg="blue")
lab.grid(row=0, column=2, pady=20)

button = Button(root, text="开始", font="Helvetic 16 bold",
                bg="lightblue", command=start, cursor="boat")
button.grid(row=4, column=2, pady=5, padx=5)

if __name__ == '__main__':
    mainloop()








