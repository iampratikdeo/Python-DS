class Queue:
    def __init__(self):
        self.queue = list()

    def add(self, data):
        self.queue.insert(0, data)

    def size(self):
        return len(self.queue)

    def remove(self):
        if(len(self.queue) > 0):
            return self.queue.pop()
        return ("No element in Queue")


TheQueue = Queue()
TheQueue.add("Mon")
TheQueue.add("Tue")
TheQueue.add("Wed")
print(TheQueue.size())
print(TheQueue.remove())
print(TheQueue.size())
