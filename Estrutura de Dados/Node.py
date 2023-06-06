class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, item):
        self.data = item
    def setNext(self, item):
        self.next = item
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1
    def size(self):
        return f'{self.size}'
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def print(self):
        current = self.head
        while current != None:
            print(current)
            current = current.getNext()
    def pop(self):
        current = self.head
        previous = None
        while current != None:
            previous = current.getData()
            current = current.getNext()
            print(previous)
mylist = Stack()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)


mylist.print()
mylist.pop()
