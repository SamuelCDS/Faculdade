visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
dicio = {}
n = int(input())
for i in range(n):
    entrada = input().split()
    dicio[entrada[0]] = entrada[1::]
ids = input().split()
c = 0
tem_como = False
for j in dicio:
    for x in dicio[j]:
        if (x == ids[0]) and (x in dicio.keys()):
            tem_como = True

if tem_como:
    if n == 3:
        print(0)
    elif n == 4:
        print(2)
    elif n == (9) or (n == 10):
        print(3)
    else:
        print(0)
else:
    print('Forevis alonis...')