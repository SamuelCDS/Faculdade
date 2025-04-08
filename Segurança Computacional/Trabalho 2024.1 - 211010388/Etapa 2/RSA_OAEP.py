import hashlib
import random

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def generate_mask(seed, length, hash_func=hashlib.sha256):
    result = b""
    counter = 0
    while len(result) < length:
        C = counter.to_bytes(4, byteorder="big")
        result += hash_func(seed + C).digest()
        counter += 1
    return result[:length]

def oaep_pad(message, bloco, hash_func=hashlib.sha256):
    h_len = hash_func().digest_size
    m_len = len(message)
    ps_len = bloco - m_len - 2 * h_len - 2

    # Padding String (PS) - zeros
    ps = b'\x00' * ps_len
    db = hash_func(b'').digest() + ps + b'\x01' + message
    seed = random.randbytes(h_len)
    db_mask = generate_mask(seed, bloco - h_len - 1, hash_func)
    masked_db = xor_bytes(db, db_mask)
    seed_mask = generate_mask(masked_db, h_len, hash_func)
    masked_seed = xor_bytes(seed, seed_mask)
    return b'\x00' + masked_seed + masked_db

def oaep_unpad(padded_message, bloco, hash_func=hashlib.sha256):
    h_len = hash_func().digest_size
    if len(padded_message) != bloco:
        raise ValueError("Invalid padded message length")

    # Extrair componentes do padded message
    masked_seed = padded_message[1:h_len + 1]
    masked_db = padded_message[h_len + 1:]

    # Gerar máscara para o Seed
    seed_mask = generate_mask(masked_db, h_len, hash_func)
    seed = xor_bytes(masked_seed, seed_mask)

    # Gerar máscara para o DB
    db_mask = generate_mask(seed, bloco - h_len - 1, hash_func)
    db = xor_bytes(masked_db, db_mask)

    # Verificar o hash de L
    l_hash = hash_func(b'').digest()
    if db[:h_len] != l_hash:
        raise ValueError("OAEP hash mismatch error")

    # Encontrar e remover a Padding String (PS) e o separador
    index = db[h_len:].find(b'\x01')
    if index == -1:
        raise ValueError("Invalid padding string")
    
    message = db[h_len + index + 1:]
    return message

# Testes
if __name__ == "__main__":
    bloco = 2048 // 8  # Tamanho do bloco em bytes

    # Mensagem para teste
    message = b"Trabalho tenso ;-;"
    
    # Pad e unpad
    padded_message = oaep_pad(message, bloco)
    print(f"Mensagem Cifrada: {padded_message}")

    decrypted_message = oaep_unpad(padded_message, bloco)
    print(f"Mensagem Decifrada: {decrypted_message}")

    assert message == decrypted_message, "Erro: A mensagem decifrada não corresponde à mensagem original"
