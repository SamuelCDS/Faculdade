import Implementacao_AES128
class AES_CTR:
    def __init__(self):
        self.aes = Implementacao_AES128.Aes_128()

    def incrementar_contador(self, contador):
        # Incrementando o valor do contador como um inteiro
        return (int.from_bytes(contador, byteorder='big') + 1).to_bytes(len(contador), byteorder='big')

    def ctr_encrypt(self, chave, dado, num_rodadas):
        if isinstance(dado, str):
            dado = dado.encode()

        # Quebrando o dado em blocos de 16 bytes
        blocos = [dado[i:i + 16] for i in range(0, len(dado), 16)]

        dado_encriptado = b''

        # Inicializando o contador com 16 bytes
        contador = b'\x00' * 16

        for bloco in blocos:
            # Cifrando o valor do contador usando AES com o número especificado de rodadas
            keystream = self.aes.encriptar(chave, contador, num_rodadas)
            
            # XOR o bloco de dado com o keystream
            bloco_encriptado = bytes([_a ^ _b for _a, _b in zip(bloco, keystream)])
            dado_encriptado += bloco_encriptado
            
            # Incrementando o contador
            contador = self.incrementar_contador(contador)

        return dado_encriptado

    def ctr_decrypt(self, chave, dado, num_rodadas):
        return self.ctr_encrypt(chave, dado, num_rodadas)
