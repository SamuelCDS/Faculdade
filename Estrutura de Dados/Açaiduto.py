class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
    def adiciona_aresta(self, u, v):
        self.grafo[v-1][v-1] = 1
    def mostra_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])