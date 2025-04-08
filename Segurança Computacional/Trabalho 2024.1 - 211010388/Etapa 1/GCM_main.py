from Implementacao_ModoGCM import AES_GCM

def teste_arquivo_gcm(arquivo_original, arquivo_criptografado, arquivo_tag, chave, nonce, num_rodadas, aad=b''):
    aes_gcm = AES_GCM()

    with open(arquivo_original, 'rb') as f:
        dados = f.read()

    ciphertext, tag = aes_gcm.encrypt(chave, dados, aad, nonce, num_rodadas)
    with open(arquivo_criptografado, 'wb') as f:
        f.write(ciphertext)
    
    with open(arquivo_tag, 'wb') as f:
        f.write(tag)

    with open(arquivo_criptografado, 'rb') as f:
        ciphertext = f.read()
    
    with open(arquivo_tag, 'rb') as f:
        tag = f.read()
    
    decrypted_data = aes_gcm.decrypt(chave, ciphertext, tag, aad, nonce, num_rodadas)
    with open('/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo_descriptografadoGCM', 'wb') as f:
        f.write(decrypted_data)


if __name__ == "__main__":
    chave = b'\x00' * 16  # Chave de 128 bits (16 bytes)
    nonce = b'\x00' * 12  # Nonce de 96 bits (12 bytes)
    num_rodadas = 10  # Número de rodadas do AES

    # Arquivos de teste
    arquivo_original = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo'
    arquivo_criptografado = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo_criptografadoGCM.bin'
    arquivo_tag = '/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/arquivo_tagGCM.bin'

    teste_arquivo_gcm(arquivo_original, arquivo_criptografado, arquivo_tag, chave, nonce, num_rodadas)