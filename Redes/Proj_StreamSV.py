import socket, pyaudio, wave

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.stream = None
    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(4)
        print('Servidor iniciado, aguardando conexões...')

        while True:
            client, address_cl = self.server.accept()
            print('Cliente: ', address_cl, 'CONECTADO')
            cmdMusica = client.recv(1024).decode()
            if cmdMusica == "play":
                print("Comando de reprodução recebido.")
                audio = pyaudio.PyAudio()
                musica = wave.open('/home/samuelcds/Músicas/Angelo Boltini-This Town.wav', 'rb')
                self.stream = audio.open(format=audio.get_format_from_width(musica.getsampwidth()),
                                         channels=musica.getnchannels(),
                                         rate=musica.getframerate(),
                                         output=True,
                                         frames_per_buffer=1024)
                arquivo = musica.readframes(1024)
                while arquivo:
                    self.stream.write(arquivo)
                    if not arquivo:
                        break
                    arquivo = musica.readframes(1024)
                self.stream.stop_stream()
                self.stream.close()
                audio.terminate()
                
                
if __name__ == '__main__':
    server = Server('localhost', 12345)
    server.start()
