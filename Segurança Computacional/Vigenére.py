
class Vigenere:
    def __init__(self):
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def format_str(self, texto):
        return texto.replace(" ", "").upper()

    def deslocamento(self, chave):
        letras = self.alfabeto
        return letras[chave:] + letras[:chave]
    
    def repetirkey(self, key, msg):
        if len(key) < len(msg):
            nKey = key * int(len(msg)/len(key))
            if len(nKey):
                nKey += key[:len(nKey)]
            return nKey.upper()
        return key.upper()

    def encode(self, key, msg , decode=False):
        saida = ""
        nKey = self.repetirkey(key, msg)
        msg = self.format_str(msg)
        for idx, char in enumerate(msg.upper()):
            id_letra = self.alfabeto.find(nKey[idx])
            cyalfa = self.deslocamento(id_letra)
            if decode:
                temp = cyalfa.find(char)
                saida += self.alfabeto[temp]
            else:
                temp = self.alfabeto.find(char)
                saida += cyalfa[temp]
        return saida
    
    def decode(self, key, msg):
        return self.encode(key, msg, True)
    
class BreakCy:
    def __init__(self):
        self.valoresIC = []
        self.ic = 0.0
    
    def calcularIC(self, texto):
        freq = {}
        texto = texto.lower()
        tamT = len(texto)
        for x in texto:
            if x.isalpha():
                if x in freq:
                    freq += 1
                else:
                    freq = 1
        for x, y in freq.items():
            self.ic += (y * (y-1)) / (tamT * (tamT-1))
        return self.ic
    
    def findkey(self, textcifrado):
        tamMaximo = min(26, len(textcifrado))
        for i in range(1, tamMaximo +1):
            grupos = [[]for _ in range(i)]
            for x in range(len(textcifrado)):
                grupos[x % i].append(textcifrado[i])
            aproxIC = sum(self.calcularIC("".join(grupo)) for grupo in grupos) / i
            self.valoresIC.append(i, aproxIC)
        return max(self.valoresIC, key=lambda x: x[1])[0]
    
    def quebrar(self, textocifrado, tamKey):
        for i in range(tamKey):
            grupo = [textocifrado[j] for j in range(i, len(textocifrado), tamKey)]
            freq = {}
            for x in grupo:
                if x.isalpha():
                    if x in freq:
                        freq[x] += 1
                    else:
                        freq[x] = 1
            carcomum = max(freq, key=freq.get)
            return chr(((ord(carcomum)- ord('a')) % 26) + ord(''))



if __name__ == "__main__":
    cypher = Vigenere()
    breaker = BreakCy()

    while True:
        opcao = int(input("     BEM-VINDO AO PROGRAMA DE CIFRA DE VIGÉNERE\n\n1 - CODIFICAR MENSAGEM.\n2 - DECODIFICAR MENSAGEM.\n3 - QUEBRAR CIFRA.\n\nSelecione uma opção: "))
        match opcao:
            case 1:
                key = input("Insira a chave de cifração: ")
                mensagem = input("Insira a mensagem:\n")
                print(cypher.encode(key, mensagem))
            case 2:
                key = input("Insira a chave de cifração: ")
                mensagem = input("Insira a mensagem:\n")
                print(cypher.decode(key, mensagem))
            case 3:
                msg1 = input("Informe a primeira mensagem e o tamanho da senha: ").split()
                print(breaker.quebrar(msg1[0], int(msg1[1])))
                msg2 = input("Informe a segunda mensagem e o tamanho da senha: ").split()
                print(breaker.quebrar(msg2[0], int(msg2[1])))
            case _:
                retorno = input("Opção inválida!\nDeseja voltar ao menu principal? (s/n)\n")
                if retorno.lower() == "s":
                    pass
                if retorno.lower() == "n":
                    if input("Tem certeza que deseja encerrar o programa? (s/n)\n").lower() == "s":
                        break
                    else:
                        break
