def rep(var1, var2):
    return var1.replace(str(var2), '', 1)

n = int(input())
for x in range(n):
    plano = input()
    matu = input()
    vesp = input()
    notu = input()
    tudo = matu+vesp+notu
    morte = False
    for i in tudo:
        if i in plano:
            plano = rep(plano, i)
        else:
            morte = True
    if morte:
        print('You died!')
    elif plano == "":
        print("It's in the box!")
    else:
        print(f"Bora ralar: {''.join(sorted(list(plano), reverse=False))}")
