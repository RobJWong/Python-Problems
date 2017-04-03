class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    def find(self,data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    def preorder(self): 
        #displays node value it is on
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
    def postorder(self): 
        #displays node value on the row
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))
    def inorder(self): 
        #displays node value on the row
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.postorder()
        
class Tree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder(self):
        self.root.preorder()
    def postorder(self):
        self.root.postorder()
    def inorder(self):
        self.root.inorder()

bst = Tree()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(15)
bst.insert(21)
bst.insert(9)
bst.insert(3)
#bst.preorder()
#bst.postorder()
bst.inorder()

