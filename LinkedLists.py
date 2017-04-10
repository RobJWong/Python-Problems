class Node(object):
    def __init__(self, data, pointer = None):
        self.data = data
        self.next = pointer
    def getNext (self):
        return self.next
    def getValue (self):
        return self.data
    def setNext (self, pointer):
        self.next = pointer
    def setData (self, data):
        self.data = data

class LinkedList(object):
    def __init__(self, root = None):
        self.root = root
        self.size = 0
    def getSize (self):
        return self.size
    def addNode(self, value):
        node = Node(value, self.root)
        self.root = node
        self.size += 1

myList = LinkedList()
myList.addNode(5)
myList.addNode(8)
myList.addNode(12)
print("size="+str(myList.getSize()))