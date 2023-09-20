
class Vigenere:
    def __init__(self):
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def format_str(self, texto):
        return texto.replace(" ", "").upper()

    def deslocamento(self, chave):
        letras = self.alfabeto
        return letras[chave:] + letras[:chave]

    def encode(self, key, msg):
        return
    
    def decode(self, key, msg):
        return
    

if __name__ == "__main__":
    cypher = Vigenere()

    while True:
        opcao = int(input("     BEM-VINDO AO PROGRAMA DE CIFRA DE VIGÉNERE\n\n1 - CODIFICAR MENSAGEM.\n2 - DECODIFICAR MENSAGEM.\n3 - QUEBRAR CIFRA.\n\nSelecione uma opção: "))
        match opcao:
            case 1:
                key = input("Insira a chave de cifração: ")
                mensagem = input("Insira a mensagem:\n")
                cypher.encode(key, mensagem)
            case 2:
                key = input("Insira a chave de cifração: ")
                mensagem = input("Insira a mensagem:\n")
                cypher.decode(key, mensagem)
            case 3:
                pass
            case _:
                retorno = input("Opção inválida!\nDeseja voltar ao menu principal? (s/n)\n")
                if retorno.lower() == "s":
                    pass
                if retorno.lower() == "n":
                    if input("Tem certeza que deseja encerrar o programa? (s/n)\n").lower() == "s":
                        break
                    else:
                        break