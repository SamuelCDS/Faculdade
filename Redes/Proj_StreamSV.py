import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address_sv = ('localhost', 12345)
servidor.bind(address_sv)
servidor.listen(4)
print('Servidor iniciado, aguardando conexões...')

while True:
    client, address_cl = servidor.accept()
    print('Cliente: ', address_cl, 'CONECTADO')
    cmdMusica = client.recv(1024).decode()
    musica = open('/home/samuelcds/Músicas/Angelo Boltini - This Town.mp3', 'rb')
    while True:
        arquivo = musica.read(1024)
        if not arquivo:
            break
        client.send(arquivo)
    musica.close()
    client.close()