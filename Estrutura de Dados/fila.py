class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, val):
        self.data = val
    def setNext(self, val):
        self.next = val

class Fila:
    def __init__(self):
        self.head = None
        self.size = 0
    def add(self, val):
        temp = Node(val)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1
