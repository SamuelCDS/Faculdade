
class Deque:
    def __init__(self):
        self.lista = []
    def isEmpty(self):
        return self.lista == []
    def addFront(self, item):
        self.lista.append(item)
    def addRear(self, item):
        self.lista.insert(0,item)
    def addPos(self, prioridade, item):
        self.lista.insert(prioridade, item)
    def removeFront(self):
        return self.lista.pop()
    def removeRear(self):
        return self.lista.pop(0)
    def size(self):
        return len(self.lista)

def checar_let(lista):
    eh_letra = False
    for i in lista:
        if not(isinstance(i, int)):
            eh_letra = True
        else:
            None
    return eh_letra

def ordenar_list(lista):
    loops = lista[0]
    lista = lista[1::]
    strin = ""
    for i in range(loops):
        A = lista.pop(0)
        B = lista.pop(0)
        if A < B:
            lista.append(A)
            lista.insert(0, B)
        else:
            lista.insert(0, A)
            lista.append(B)
            
    for j in lista:
        strin += str(j)
    lista = []
    return strin

def ehparen(c):
    return ((c == '(') or (c == ')'))

def ehparvalid(texto):
    c = 0
    for i in range(len(texto)):
        if texto[i] == '(':
            c +=1
        elif texto[i] == ')':
            c -= 1
        if c < 0:
            return False
        return c == 0

def limparstrin(strin):
    lista = []
    tex = ''
    if len(strin) == 0:
        return
    
    verificado = set()
    
    fila = []
    temp = 0
    nivel = 0
    
    fila.append(strin)
    verificado.add(strin)
    while (len(fila)):
        strg = fila[0]
        fila.pop()
        if ehparvalid(strin):
            lista.append(strin)
            nivel = True
        if nivel:
            continue
        for i in range(len(strin)):
            if not(ehparen(strin[i])):
                continue
            
            temp = strin[0:i] + strin[i + 1:]
            if temp not in verificado:
                fila.append(temp)
                verificado.add(temp)
    for i in lista:
        for j in i:
            tex += j
        
    return tex

def seclist(frase):
    inicio = 0
    fim = 0
    c = 0
    while True:
        c += 1
        inicio = frase.find('(', c)
        if inicio == -1:
            break
        fim = frase.find(')', inicio + 1)
        if fim == -1:
            break
        yield frase[inicio+1: fim]
        inicio = fim

d = Deque()
Lista_G = []
funcao = input().split()
while funcao[0] != 'stop':
    numeros = []
    if funcao[0] == 'enqueue':
        for i in range(int(funcao[1])):
            solicitacao = input().split()
            
            if solicitacao[1] == 'scramble':
                if int(solicitacao[0]) == 0:
                    inan = []
                    d.addRear(solicitacao[2])
                    inan = d.removeRear()
                    d.addPos(int(solicitacao[0]), inan)
                elif int(solicitacao[0]) <= d.size():
                    d.addFront(solicitacao[2])
                else:
                    d.addPos(int(solicitacao[0]), solicitacao[2])
            else:
                for nu in solicitacao[2::]:
                    numeros.append(int(nu))
                if int(solicitacao[0]) == 0:
                    inan = []
                    d.addRear(list(map(int, solicitacao[2::])))
                    inan = d.removeRear()
                    d.addPos(int(solicitacao[0]), inan)
                elif int(solicitacao[0]) >= d.size():
                    d.addFront(list(map(int, solicitacao[2::])))
                else:
                    d.addRear(list(map(int, solicitacao[2::])))
    elif funcao[0] == 'go':
        try:
            temp = d.removeRear()
        except:
            None
        if checar_let(temp):
            fraseLimpa = temp
            
            semsujeira = limparstrin(temp)
            if (")" or "(") in fraseLimpa:
                fraseLimpa = fraseLimpa.replace("(", " ")
                fraseLimpa = fraseLimpa.replace(")", " ")
            
            listaPrimaria = fraseLimpa.split()
            
            if listaPrimaria == []:
                None
            else:
                frasef = ''
                listaf = []
                listaSecundaria = []
                for interno in seclist(temp):
                    listaSecundaria.append(interno)

                for j in listaPrimaria:
                    if j in listaSecundaria:
                        print(j)
                        listaf.insert(0, j)
                    else:
                        listaf.append(j)
                for k in listaf:
                    frasef += k
                print(frasef)
            temp = []

        else:
            print(ordenar_list(temp))
            temp = []
    else:
        None

    funcao = input().split()
print(f'{d.size()} processo(s) órfão(s).')