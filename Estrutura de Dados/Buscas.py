def BuscaLargura(graph, vertex):
    visited, queue = set(), [vertex]
    while queue:
        temp = queue.pop(0)
        if temp  not in visited:
            visited.add(temp)
            queue.extend(graph[temp] - visited)
    return visited

def BuscaProfundidade(graph, vertex):
    visited = set()
    visited.add(vertex)
    noVisit = [vertex]
    while noVisit:
        ver = noVisit.pop()
        for neightbor in graph[ver]:
            if neightbor not in visited:
                visited.add(neightbor)
                noVisit.append(neightbor)
    return visited

if __name__ == "__main__":
    graph = []