class Node:
    def __init__(self, data):
        self.data = data
        self.dir = self.esq = None
    def __str__(self):
        return str(self.data)
    

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.data = None
    
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.esq:
            self.simetric_traversal(node.esq)
        print(node, end=" ")
        if node.dir:
            self.simetric_traversal(node.dir)
    
    def posorder_traversal(self, node=None):
        if node is None:
            node = self.root
        #print(node, end=" ")
        if node.esq:
            self.posorder_traversal(node.esq)
        if node.dir:
            self.posorder_traversal(node.dir)
        print(node, end=" ")
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hEsq = 0
        hDir = 0
        if node.esq:
            hEsq = self.height(node.esq)

        if node.dir:
            hDir = self.height(node.dir)
        if hDir > hEsq:
            return hDir+1
        return hEsq+1

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while x:
            parent = x
            if value > x.data:
                x = x.esq
            else:
                x = x.dir
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.esq = Node(value)
        else:
            parent.dir = Node(value)
    
    def search(self, value, node=0):
        if not(node):
            node = self.root
        if node is None or node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.esq)
        return self.search(value, node.dir)
    
    def search1(self,value, node):
        if node is None or node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self .search1(value, node.esq)
        return self.search1(value, node.dir)

if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.esq = Node(14)
    tree.root.dir = Node(18)

    tree.posorder_traversal()
    print(f'Altura: {tree.height()}')