from tkinter import *
import time


class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)
        self.canvas.move(self.id, winW/2, winH/2)

    def ballMove(self):
        self.canvas.move(self.id, 0, step)


winW = 640
winH = 480
step = 3
speed = 0.03
root = Tk()
root.title("Bouncing Ball")
root.wm_attributes('-topmost', 1)

canvas = Canvas(root, width=winW, height=winH)
canvas.pack()
root.update()

ball = Ball(canvas, 'yellow', winW, winH)

if __name__ == '__main__':
    while True:
        ball.ballMove()
        root.update()
        time.sleep(speed)
