from TkPagesUtils.Queue import Queue


class JosephRingPageHandle:
    def __init__(self, numlist, killnum):
        self.numlist = numlist
        self.killnum = killnum
        self.simqueue = Queue()
        self.kill_list = []

    def josephRingHandle(self):
        for name in self.numlist:
            self.simqueue.enqueue(name)

        while self.simqueue.size() > 1:
            for i in range(self.killnum):
                self.simqueue.enqueue(self.simqueue.dequeue())
            self.kill = self.simqueue.dequeue()
            self.kill_list.append(str(self.kill) + '号出列\t\t剩下的是' + str(self.simqueue.items) + '\n')

        return str(self.simqueue.dequeue()), self.kill_list
