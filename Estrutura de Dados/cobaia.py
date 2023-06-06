
def entre(frase):
    inicio = 0
    for i in frase:
        inicio = frase.find('[', inicio)
        if inicio == -1:
            break
        fim = frase.find(']', inicio + 1)
        if fim == -1:
            break
        yield frase[inicio + 1: fim]
        inicio = fim + 1
frase = '(llo(he)'
for i in entre(frase):
    print(i)