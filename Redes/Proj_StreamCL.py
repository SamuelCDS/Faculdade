import socket, pyaudio, tkinter, threading, queue
from tkinter import ttk

class Aplic:
    def __init__(self, master=None):
        self.event = threading.Event()

        self.principal = tkinter.Frame(master)
        self.principal["pady"] = 50
        self.principal["padx"] = 100
        self.principal.pack(side="top")
        self.msg = tkinter.Label(self.principal, text="Stream de Áudio")
        self.msg["font"] = ("Arial", "14", "bold")
        self.msg.pack(side="top")

        #Lista de musicas:
        self.ls = tkinter.Frame(master)
        self.ls["padx"] = 120
        self.ls.pack()
        self.lsT = tkinter.Label(self.ls, text="Selecione uma musica: ", font=('Arial', '10'))
        self.lsT.pack(side="top")
        self.lista = tkinter.StringVar()
        self.combobox = ttk.Combobox(self.ls,textvariable=self.lista)
        self.combobox["state"] = 'reandoly'
        self.combobox.pack(fill=tkinter.X)
        self.selecL = tkinter.Button(self.ls, text="Selecionar", command=self.selecM)
        self.selecL.pack()

        #Saida de textos:
        self.textout = tkinter.Frame(master)
        self.textout["padx"] = 20
        self.textout.pack()
        self.To = tkinter.Label(self.textout, text="", font="Arial")
        self.To.pack(side="top")

        #Botão para reiniciar a reprodução:
        self.res = tkinter.Frame(master)
        self.res["pady"] = 5
        self.res["padx"] = 50
        self.res.pack()
        self.restart = tkinter.Button(self.res)
        self.restart["text"] = "Restart music"
        self.restart["font"] = ("Arial", "10")
        self.restart["width"] = 13
        self.restart["command"] = self.Reiniciar
        self.restart.pack(side="top")
        self.ms2 = tkinter.Label(self.res, text="", font=("Arial", "12"))
        self.ms2.pack()

        #Botão para iniciar reprodução:
        self.pl = tkinter.Frame(master)
        self.pl["pady"] = 10
        self.pl["padx"] = 50
        self.pl.pack()
        self.play = tkinter.Button(self.pl)
        self.play["text"] = "Play"
        self.play["font"] = ("Arial", "10")
        self.play["width"] = 10
        self.play["command"] = self.Play
        self.play.pack(side="top")
        self.ms3 = tkinter.Label(self.pl, text="", font=("Arial", "12"))
        self.ms3.pack()

        #Botão para pausar a reprodução:
        self.ps = tkinter.Frame(master)
        self.ps["pady"] = 20
        self.ps["padx"] = 50
        self.ps.pack()
        self.pause = tkinter.Button(self.ps)
        self.pause["text"] = "Pause"
        self.pause["font"] = ("Arial", "10")
        self.pause["width"] = 10
        self.pause["command"] = self.Pause
        self.pause.pack()
        self.ms4 = tkinter.Label(self.res, text="", font=("Arial", "12"))
        self.ms4.pack()

        #Pessoas conectadas:
        self.espaco = tkinter.Frame(master)
        self.espaco["pady"] = 10
        self.espaco.pack()
        self.space = tkinter.Label(self.espaco, text="", font=("Arial", "12"))
        self.space.pack()

        #Conexão com o servidor:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addressSV = ('localhost', 1234)
        self.To["text"] = "Conectando..."
        self.client.connect(self.addressSV)
        self.To["text"] = "Conectado."

        #Recebimento da lista de músicas e inserção na box:
        self.LMusicas = self.client.recv(1024).decode().split('\n')
        self.combobox["values"] = self.LMusicas

        #Inicialização do PyAudio:
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=pyaudio.paInt16,
                                   channels=2,
                                   rate=44100,
                                   output=True,
                                   frames_per_buffer=1024)

    def selecM(self):
        if self.lista.get():
            musica = self.lista.get()
            self.client.sendall(musica.encode())
            print(f"Música selecionada: {musica}")  

    def Reiniciar(self):
        self.To["text"] = "Reiniciando música..."
        self.client.sendall('Restart'.encode())

    def Play(self):
        self.rodar = threading.Thread(target=self.Rodar, args=(self.event,))
        self.rodar.start()

    def Rodar(self, event: threading.Event):
        self.client.sendall('Play'.encode())
        self.To["text"] = "Reproduzindo..."
        dataFila = queue.Queue()

        def receive_data():
            while True:
                data = self.client.recv(1024)
                if not data:
                    break
                dataFila.put(data)

        # Inicia a thread para receber dados do servidor
        receive_thread = threading.Thread(target=receive_data)
        receive_thread.start()

        # Reprodução contínua dos dados recebidos
        while True:
            if not dataFila.empty() or event.is_set():
                self.stream.stop_stream()
                break

            try:
                data = dataFila.get(timeout=0.1)  # Aguarda até 0.1 segundos por novos dados
                self.stream.write(data)
                self.stream.start_stream()
            except queue.Empty:
                continue

        # Aguarda a conclusão da thread de recebimento de dados
        receive_thread.join()

    def Pause(self):
        self.client.sendall('Pause'.encode())
        self.To["text"] = "Pause."
        self.stream.stop_stream()

if __name__ == '__main__':
    root = tkinter.Tk()
    Aplic(root)
    root.mainloop()
    Aplic().client.close()
    Aplic().stream.close()
