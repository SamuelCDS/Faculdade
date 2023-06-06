class Stack:
    def __init__(self):
        self.lista = []
    def push(self, item):
        self.lista.append(item)
    def pop(self):
        return self.lista.pop()
    def peek(self):
        return self.lista[len(self.lista)-1]
    def isEmpty(self):
        return self.lista == []
    def size(self):
        return len(self.lista)
s = Stack()
numero = int(input())
for i in range(numero):
    expressao = input()
    n_duplicado = True
    for j in expressao:
        if j in '([':
            s.push(j)
        else:
            if not s.isEmpty():
                n_duplicado = False
            else:
                s.pop()
    if n_duplicado and s.isEmpty():
        print('A expressão não possui duplicata.')
    else:
        print('A expressão possui duplicata.')

