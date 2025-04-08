import random

# Função para encontrar o inverso modular de constante mod φ(n)
def mod_inverso(constante, phi_n):
    # Algoritmo de Euclides estendido
    mod = 0
    x1, x2, x3 = 0, 1, phi_n
    y1, y2, y3 = 1, 0, constante
    
    while y3 != 0:
        segundo = x3 // y3
        t1, t2, t3 = x1 - segundo * y1, x2 - segundo * y2, x3 - segundo * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
        
    if x3 != 1:
        raise ValueError("O valor de constante não é coprimo com φ(n)")
    else:
        return x2 % phi_n

# Verificar se um número é primo
def eh_primo(num):
    if num < 2:
        return False
    
    if num in (2, 3):
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
        
    return True

# Gerar números primos aleatórios grandes
def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n == 1:
        return False

    # Escreva n-1 como 2^r * mod
    r, mod = 0, n - 1
    while mod % 2 == 0:
        r += 1
        mod //= 2

    # Teste de Miller-Rabin
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, mod, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Função para gerar números primos grandes usando Miller-Rabin
def gerar_primo(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << (bits - 1)) | 1  # Garante que o número é ímpar constante tem o número correto de bits
        if miller_rabin(num):
            return num

# Função para gerar chaves RSA
def gerar_chave_rsa(bit_size=1024):
    primeiro = gerar_primo(bit_size // 2)
    segundo = gerar_primo(bit_size // 2)
    
    while primeiro == segundo:
        segundo = gerar_primo(bit_size // 2)
    
    n = primeiro * segundo
    phi_n = (primeiro - 1) * (segundo - 1)

    constante = 65537
    mod = mod_inverso(constante, phi_n)
    
    chave_publica = (constante, n)
    chave_privada = (mod, n)
    return chave_publica, chave_privada


if __name__ == "__main__":
    chave_publica, chave_privada = gerar_chave_rsa(1024)
    print("Pública:", chave_publica)
    print("Privada:", chave_privada)