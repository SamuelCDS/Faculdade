class Grafo():
    def __init__(self):
        self.lista = []
        self.dict = {}
    def insere_v(self, id, dado):
        self.dict = {id:dado}
    def insere_a(self, id_o, id_d):
        self.dict[id_d] = {id_o}
    def remove_v(self, id):
        if id in self.dict:
            del self.dict[id]
    def remove_a(self, id_o, id_d):
        if id_d in self.dict:
            self.dict[id_d].pop(id_o)
    def grau_saida(self, id):
        if id in self.dict:
            return len(self.dict[id])
        else:
            return 0
    def grau_entrada(self, id):
        if id in self.dict:
            return len(self.dict[id])
        else:
            return 0
    def alcancavel(self, u, v):
        if self.dict[v] in self.dict[u]:
            return True
        else:
            False

grafo = Grafo()
n = int(input())
for i in range(n):
    entrada = input().split()
    if entrada[0] == 'IV':
        grafo.insere_v(entrada[1], entrada[2])
    elif entrada[0] == 'IA':
        grafo.insere_a(entrada[1], entrada[2])
    elif entrada[0] == 'RV':
        grafo.remove_v(entrada[1])
    elif entrada[0] == 'IA':
        grafo.remove_a(entrada[1])