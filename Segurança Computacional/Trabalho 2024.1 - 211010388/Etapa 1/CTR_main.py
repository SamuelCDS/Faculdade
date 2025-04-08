from Implementacao_ModoCTR import AES_CTR

def teste_ctr_arquivo(arquivo_original, arquivo_criptografado, arquivo_descriptografado, chave, num_rodadas):
    aes_ctr = AES_CTR()

    with open(arquivo_original, 'rb') as f:
        dados = f.read()

    dados_criptografados = aes_ctr.ctr_encrypt(chave, dados, num_rodadas)
    with open(arquivo_criptografado, 'wb') as f:
        f.write(dados_criptografados)

    with open(arquivo_criptografado, 'rb') as f:
        dados_criptografados = f.read()

    dados_descriptografados = aes_ctr.ctr_decrypt(chave, dados_criptografados, num_rodadas)
    with open(arquivo_descriptografado, 'wb') as f:
        f.write(dados_descriptografados)

if __name__ == "__main__":
    chave = bytes.fromhex('00112233445566778899aabbccddeeff')
    num_rodadas = 16

    arquivo_original = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo'
    arquivo_criptografado = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo_1_criptografadoCTR.bin'
    arquivo_descriptografado = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo_1_descriptografadoCTR'

    teste_ctr_arquivo(arquivo_original, arquivo_criptografado, arquivo_descriptografado, chave, num_rodadas)
