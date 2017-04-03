class queueClass(object):
    def __init__(self):
        self.queue = []
    def push (self, value):
        self.queue.append(value)
    def pop (self):
        return(self.queue.pop(0))
    def printQueue(self):
        print("Current items in queue are {}".format(self.queue))


newQueue = queueClass()
newQueue.push(9)
newQueue.push(1)
newQueue.push(10)
newQueue.printQueue()
newQueue.pop()
newQueue.printQueue()
newQueue.push(-4)
newQueue.printQueue()
newQueue.pop()
newQueue.printQueue()