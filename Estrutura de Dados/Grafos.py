dicio = {}
entradas = int(input())
for i in range(entradas):
    entrada = input().split()
    if entrada[0] == "IV":
        dicio = {entrada[1] : None}
    elif entrada[0] == "IA":
        if (entrada[1] and entrada[2]) in dicio:
            dicio[entrada[2]] = dicio[entrada[1][0]]
    elif entrada[0] == "RV":
        if entrada[1] in dicio:
            del dicio[entrada[1]]
    elif entrada[0] == "RA":
        if entrada[1] in dicio:
            dicio[entrada[2]] = dicio.pop(entrada[1])

print(dicio)