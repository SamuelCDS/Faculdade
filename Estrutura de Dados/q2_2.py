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
        self.cont = 0
    def add(self, val):
        self.cont += 1
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > val:
                stop = True
            else:
                previous =  current
                current = current.getNext()
        temp = Node(val)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        def isempty(self):
            return self.head == None
        def size(self):
            return self.cont
        def pop(self):
            current = self.head
            previous = None
            found = False
            last = None
            while not found:
                if current.getData() == None:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return last
