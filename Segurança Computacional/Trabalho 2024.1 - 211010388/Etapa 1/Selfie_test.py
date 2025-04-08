import numpy as np
import matplotlib.pyplot as plt
from Implementacao_ModoCTR import AES_CTR

# Função para carregar a imagem como um array de bytes
def carregar_imagem(filepath):
    # Carrega a imagem como um array de bytes
    img = plt.imread(filepath)
    if img.dtype == np.float32:  # Normalmente para imagens PNG
        img = (img * 255).astype(np.uint8)
    return img.tobytes(), img.shape

# Função para salvar a imagem a partir de um array de bytes
def salvar_imagem(dados, shape, filepath):
    img_array = np.frombuffer(dados, dtype=np.uint8).reshape(shape)
    plt.imsave(filepath, img_array)

# Parâmetros
filepath_original = "/home/samuelcds/Documentos/SegCom/Trabalho 2024.1/Etapa 1/Midia/image"
chave = b'\x00' * 16  # 16 bytes
nonce = b'\x00' * 16 # 16 bytes
num_rodadas = [1, 5, 9, 13]

# Carregar a imagem
dados, shape = carregar_imagem(filepath_original)

# Instância do AES-CTR
aes_ctr = AES_CTR()

# Testar com diferentes números de rodadas
for rodadas in num_rodadas:
    # Criptografar
    dados_criptografados = aes_ctr.ctr_encrypt(chave, dados, rodadas)
    # Salvar a imagem criptografada
    filepath_criptografada = f"selfie_ctr_{rodadas}_rodadas.png"
    salvar_imagem(dados_criptografados, shape, filepath_criptografada)
    print(f"Imagem criptografada com {rodadas} rodadas salva em {filepath_criptografada}")
