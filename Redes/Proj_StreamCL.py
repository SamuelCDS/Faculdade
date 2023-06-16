import socket, pyaudio, wave, threading, os

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.audio = pyaudio.PyAudio()

    def EachCmdfor(self, clien):
        stream = None
        musica = None
        event = threading.Event()
        tocarM = None
        
        #Envio da lista de músicas:
        clien.sendall('\n'.join(os.listdir("/home/samuelcds/Músicas")).encode())

        #Processamento geral do servidor:
        try:

            def playa(event: threading.Event):
                #Envio da musica:
                while True:
                    if not musica:
                        break
                    arquivo = musica.readframes(1024)
                    stream.write(arquivo)
                    if not arquivo or event.is_set():
                        while True:
                            if not event.is_set():
                                break
            
            #Recebimento da musica desejada:
            selecao_encoded = clien.recv(1024)
            SelecM = selecao_encoded.decode()
            print(f"Música selecionada: {SelecM}")

            #Inicialização do PyAudio:
            direc = os.path.join("/home/samuelcds/Músicas", SelecM)
            musica = wave.open(direc, 'rb')
            stream = self.audio.open(format=self.audio.get_format_from_width(musica.getsampwidth()),
                                    channels=musica.getnchannels(),
                                    rate=musica.getframerate(),
                                    output=True,
                                    output_device_index=self.audio.get_default_output_device_info()['index'])

            #Recebimento de comandos:
            while True:
                try:
                    cmdMusica = clien.recv(1024).decode()
                except ConnectionResetError:
                    print("Conexão perdida.")
                    break
                except Exception as e:
                    stream.stop_stream()
                    stream.close()
                    musica.close()
                    print(f"Erro durante a comunicação com o cliente: {str(e)}")
                    break

                if cmdMusica == "Play":
                    print("Comando de reprodução recebido.")
                    if tocarM is None or not tocarM.is_alive():
                        event.clear()
                        tocarM = threading.Thread(target=playa, args=(event,))
                        tocarM.start()
                    else:
                        event.set()
                        event.clear()

                elif cmdMusica == "Pause":
                    print("comando de pausa recebido.")
                    event.set()

                elif cmdMusica == "Restart":
                    print("Comando para reiniciar recebido.")
                    event.clear()
                    musica.rewind()
                    stream.start_stream()
            
                else:
                    event.set()
                    print(f"Comando para mudar música recebido: {cmdMusica}")
                    stream.stop_stream()
                    if musica:
                        musica.close()
                    direc = os.path.join("/home/samuelcds/Músicas", cmdMusica)
                    musica = wave.open(direc, 'rb')
                    event.clear()
                    stream.start_stream()

        except ConnectionResetError:
            print("Conexão perdida.")
        except Exception as e:
            print(f"Erro durante a comunicação com o cliente: {str(e)}")

        finally:
            if stream:
                stream.stop_stream()
                stream.close()
            if self.audio:
                self.audio.terminate()
            if musica:
                musica.close()
            
    
    def start(self):
        #Iniciando servidor:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(4)
        print('Servidor iniciado, aguardando conexões...')
        
        while True:
            client, address_cl = self.server.accept()
            print('Cliente: ', address_cl, 'CONECTADO')
            eachCon = threading.Thread(target=self.EachCmdfor, args=(client,))
            eachCon.start()
                
if __name__ == '__main__':
    server = Server('localhost', 12345)
    server.start()
    server.server.close()
