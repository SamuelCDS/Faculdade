from Implementacao_AES128 import Aes_128 

def teste_arquivo(arquivo_original, arquivo_criptografado, arquivo_descriptografado, chave, num_rodadas):
    aes = Aes_128()

    with open(arquivo_original, 'rb') as f:
        dados = f.read()

    dados_criptografados = aes.encriptar(chave, dados, num_rodadas)
    with open(arquivo_criptografado, 'wb') as f:
        f.write(dados_criptografados)

    with open(arquivo_criptografado, 'rb') as f:
        dados_criptografados = f.read()

    dados_descriptografados = aes.decriptar(chave, dados_criptografados, num_rodadas)
    with open(arquivo_descriptografado, 'wb') as f:
        f.write(dados_descriptografados)

if __name__ == "__main__":
    chave = bytes.fromhex('00112233445566778899aabbccddeeff')  # Exemplo de chave 16 bytes (128 bits)
    num_rodadas = 10

    arquivo_original = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo'
    arquivo_criptografado = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo_1_criptografadoAES.bin'
    arquivo_descriptografado = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo_1-descriptografadoAES'

    teste_arquivo(arquivo_original, arquivo_criptografado, arquivo_descriptografado, chave, num_rodadas)