class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + 'connectedTo:' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def delVertex(self, key):
        del self.vertList[key]
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __inter__(self):
        return self.vertList.values()
    
G = Graph()
loops = int(input())
peso = 0.0
for i in range(loops):
    entrada = input().split()
    if entrada[0] == 'IV':
        G.addVertex(entrada[1])
    elif entrada[0] == "IA":
        G.addEdge(entrada[1], entrada[2], float(entrada[3]))
        peso += float(entrada[3])
    elif entrada[0] == "RV":
        G.delVertex(entrada[1])
    elif entrada[0] == 'RA':
        if len(G.getVertices()) != 0:
            peso -= float(G.vertList[entrada[2]])
            G.addEdge(entrada[2], None)
            G.delVertex(entrada[1])
    else:
        None
print(G.vertList['B'])
print(f'{len(G.getVertices())} vertice(s), {len(G.vertList.values())} aresta(s) e peso total {peso}.')