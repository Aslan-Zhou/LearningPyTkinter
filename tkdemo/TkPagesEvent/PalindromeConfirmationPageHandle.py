from TkPagesUtils.Deque import Deque


class PalindromeConfirmationPageHandle:
    def __init__(self, string):
        self.str = string.split(' ')
        self.returns = self.checkstring()
        self.deque = Deque()

    def checkstring(self):
        self.string = ''
        while '' in self.str:
            self.str.remove('')
        if len(self.str) > 0:
            for i in range(len(self.str)):
                self.string += self.str[i]
        else:
            return '字符串输入有误!'

    def checkHandle(self):
        if self.returns == '字符串输入有误!':
            return '字符串输入有误!'
        self.bool = True
        for item in self.string:
            self.deque.addFront(item)

        while self.deque.size() > 1 and self.bool:
            self.front = self.deque.removeFront()
            self.rear = self.deque.removeRear()
            if self.front != self.rear:
                self.bool = False

        return self.bool
