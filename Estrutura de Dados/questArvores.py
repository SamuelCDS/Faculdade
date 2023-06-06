class Arvore:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)


class ArvoreBinaria:
    def __init__(self, data):
        node = Arvore(data)
        self.root = node

if __name__ == '__main__':
    tree = ArvoreBinaria(7)
    tree.root.left = Arvore(18)
    tree.root.right = Arvore(14)
    