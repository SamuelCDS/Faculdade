lista = [0, 1]
def lis(n):
    c = 1
    for i in range(1, n-1):
        lista.append(c)
        c += lista[i]
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        lis(n)
        return lista

	
