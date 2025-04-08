import Implementacao_AES128

class AES_GCM:
    def __init__(self):
        self.aes = Implementacao_AES128.Aes_128()

    def ghash(self, h, data):
        def galois_mult(a, b):
            p = 0
            for i in range(128):
                if (b & 1) == 1:
                    p ^= a
                hi_bit_set = a & (1 << 127)
                a <<= 1
                if hi_bit_set:
                    a ^= 0xE1  # Polinômio do campo de Galois para AES-GCM
                b >>= 1
            return p

        y = 0
        h = int.from_bytes(h, byteorder='big')  # Converta h para um inteiro
        for bloco in data:
            if isinstance(bloco, bytes):
                y ^= int.from_bytes(bloco, byteorder='big')  # Converte o bloco de bytes em um inteiro
            else:
                raise ValueError("O bloco de dados deve ser um objeto de bytes")
            y = galois_mult(y, h)
            
            # Certificando de que y esteja dentro dos limites de 128 bits
            y &= (1 << 128) - 1

        return y.to_bytes(16, byteorder='big')

    def divide_em_blocos(self, dados):
        return [dados[i:i + 16] for i in range(0, len(dados), 16)]

    def gctr(self, chave, icb, data, rodadas):
        blocks = self.divide_em_blocos(data)
        encrypted_data = b''
        counter = icb

        for bloco in blocks:
            keystream = self.aes.encriptar(chave, counter, rodadas)
            encrypted_block = bytes([_a ^ _b for _a, _b in zip(bloco, keystream)])
            encrypted_data += encrypted_block
            counter = (int.from_bytes(counter, byteorder='big') + 1).to_bytes(16, byteorder='big')

        return encrypted_data

    def encrypt(self, chave, texto, aad, nonce, rodadas):
        h = self.aes.encriptar(chave, b'\x00' * 16, rodadas)
        j0 = nonce + b'\x00\x00\x00\x01'
        textoCifrado = self.gctr(chave, j0, texto, rodadas)

        # Divida os dados em blocos de 16 bytes
        add_blocos = self.divide_em_blocos(aad)
        texto_blocos = self.divide_em_blocos(textoCifrado)
        add_tamanho = len(aad).to_bytes(8, byteorder='big')
        plaintext_length = len(texto).to_bytes(8, byteorder='big')

        s = self.ghash(h, add_blocos + texto_blocos + [add_tamanho] + [plaintext_length])
        tag = self.gctr(chave, j0, s, rodadas)

        return textoCifrado, tag

    def decrypt(self, chave, textoCifrado, tag, aad, nonce, rodadas):
        h = self.aes.encriptar(chave, b'\x00' * 16, rodadas)
        j0 = nonce + b'\x00\x00\x00\x01'
        texto = self.gctr(chave, j0, textoCifrado, rodadas)

        # Dividindo os dados em blocos de 16 bytes
        add_blocos = self.divide_em_blocos(aad)
        texto_blocos = self.divide_em_blocos(textoCifrado)
        add_tamanho = len(aad).to_bytes(8, byteorder='big')
        tamanho_texto = len(textoCifrado).to_bytes(8, byteorder='big')

        s = self.ghash(h, add_blocos + texto_blocos + [add_tamanho] + [tamanho_texto])
        computed_tag = self.gctr(chave, j0, s, rodadas)

        if computed_tag != tag:
            raise ValueError("Autenticação falhou! Tag não corresponde.")

        return texto
