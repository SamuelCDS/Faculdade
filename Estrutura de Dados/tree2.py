class Node:
    def __init__(self, data=None):
        self.data = data
        self.esq = None
        self.dir = None

class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.esq = None
        self.dir = None

def insere(root, node):
    temp = Node(node)
    if not root:
        return temp
    if temp.data < root.data:
        root.esq = insere(root.esq, node)
    else:
        root.dir = insere(root.dir, node)

def inn(tree):
    if tree:
        inn(tree.esq)
        print(tree.root)
        inn(tree.dir)

def pre(tree):
    if tree:
        print(tree.root)
        pre(tree.esq)
        pre(tree.dir)

def post(tree):
    if tree:
        post(tree.esq)
        post(tree.dir)
        print(tree.root)


if __name__ == "__main__":
    entrada = input()
    raiz = BinaryTree(int(entrada), esq = None, dir=None)
    while entrada != "quack":
        if entrada == "in":
            inn(raiz)
        elif entrada == "pos":
            post(raiz)
        elif entrada == "pre":
            pre(raiz)
        else:
            insere(raiz, int(entrada))
        entrada = input()