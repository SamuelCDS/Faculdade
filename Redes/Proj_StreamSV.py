import socket, pyaudio, wave, threading, os

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.stream = None
        self.musica = None
    
    def playa(self, event: threading.Event):
        #Envio da musica:
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
        self.audio.terminate()
        self.client.close()

    def initMusic(self):
        #recebimento da musica desejada:
        self.selecao_encoded = self.client.recv(1024)
        self.SelecM = self.selecao_encoded.decode()
        print("Música selecionada.")

        #Inicialização do PyAudio:
        self.audio = pyaudio.PyAudio()
        direc = os.path.join("/home/samuelcds/Músicas", self.SelecM)
        self.musica = wave.open(direc, 'rb')
        self.stream = self.audio.open(format=self.audio.get_format_from_width(self.musica.getsampwidth()),
                                 channels=self.musica.getnchannels(),
                                 rate=self.musica.getframerate(),
                                 output=True,
                                 frames_per_buffer=1024)
    
    def start(self):
        #Iniciando servidor:
        event = threading.Event()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(4)
        print('Servidor iniciado, aguardando conexões...')
        tocarM = threading.Thread(target=self.playa, args=(event,))
        self.client, address_cl = self.server.accept()
        print('Cliente: ', address_cl, 'CONECTADO')

        #Envio da lista de músicas:
        self.client.sendall('\n'.join(os.listdir("/home/samuelcds/Músicas")).encode())

        #Primeira inicialização do PyAudio:
        self.initMusic()

        #Recebimento de comandos:
        while True:
            try:
                cmdMusica = self.client.recv(1024).decode()
            except Exception:
                self.stream.stop_stream()
                self.stream.close()
                self.audio.terminate()
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
            else:
                self.initMusic()

                
if __name__ == '__main__':
    server = Server('localhost', 1234)
    server.start()
    server.server.close()
