import socket, pyaudio, wave, threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.stream = None
    
    def playa(self, event: threading.Event):
        audio = pyaudio.PyAudio()
        self.musica = wave.open('/home/samuelcds/Músicas/Angelo Boltini-This Town.wav', 'rb')
        self.stream = audio.open(format=audio.get_format_from_width(self.musica.getsampwidth()),
                                 channels=self.musica.getnchannels(),
                                 rate=self.musica.getframerate(),
                                 output=True,
                                 frames_per_buffer=1024)
        arquivo = self.musica.readframes(1024)
        while arquivo:
            self.stream.write(arquivo)
            if not arquivo or event.is_set():
                while True:
                    if not event.is_set():
                        break
            arquivo = self.musica.readframes(1024)
        self.stream.stop_stream()
        self.stream.close()
        audio.terminate()
        self.client.close()
    
    def entrada(self):
        pass
        
    
    def start(self):
        event = threading.Event()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(4)
        print('Servidor iniciado, aguardando conexões...')
        tocarM = threading.Thread(target=self.playa, args=(event,))
        self.client, address_cl = self.server.accept()
        print('Cliente: ', address_cl, 'CONECTADO', self.client)

        while True:
            try:
                cmdMusica = self.client.recv(1024).decode()
            except Exception:
                self.client.close()
            if cmdMusica == "play":
                print("Comando de reprodução recebido.")
                try:
                    tocarM.start()
                except:
                    event.clear()
            elif cmdMusica == "Pause":
                print("comando de pausa recebido.")
                event.set()
            elif cmdMusica == "Restart":
                print("Comando para reiniciar recebido.")

    
                
                
if __name__ == '__main__':
    server = Server('localhost', 12345)
    server.start()
    server.server.close()
