import socket, sys, tkinter

lista = []
HOST = 'localhost'
PORT = 1234

CHUNK = 1024
#FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen(4)


class aplic:
    def __init__(self, master=None):
        file = "/home/samuelcds/Músicas/Angelo Boltini - This Town.mp3"
        self.musica = open()

        self.principal = tkinter.Frame(master)
        self.principal["pady"] = 100
        self.principal["padx"] = 450
        self.principal.pack(side="top")
        self.msg = tkinter.Label(self.principal, text="Stream de Áudio")
        self.msg["font"] = ("Arial", "14", "bold")
        self.msg.pack(side="top")

        self.inserir = tkinter.Frame(master)
        self.inserir["padx"] = 1
        self.inserir.pack()
        self.ms1 = tkinter.Label(self.inserir, text="Nome da música: ", font="Arial")
        self.ms1.pack(side="left")
        self.nome = tkinter.Entry(self.inserir)
        self.nome["width"] = 70
        self.nome["font"] = ("Arial", "10")
        self.nome.pack(side="left")

        self.bus = tkinter.Frame(master)
        self.bus["pady"] = -100
        self.bus["padx"] = 50
        self.bus.pack(side="right")
        self.buscar = tkinter.Button(self.bus)
        self.buscar["text"] = "Buscar música"
        self.buscar["font"] = ("Arial", "10")
        self.buscar["width"] = 10
        self.buscar["command"] = self.buscarNome
        self.buscar.pack(side="top")
        self.ms2 = tkinter.Label(self.bus, text="", font=("Arial", "12"))
        self.ms2.pack()

        self.pl = tkinter.Frame(master)
        self.pl["pady"] = -100
        self.pl["padx"] = 50
        self.pl.pack()
        self.play = tkinter.Button(self.pl)
        self.play["text"] = "Play"
        self.play["font"] = ("Arial", "10")
        self.play["width"] = 10
        self.play["command"] = self.Play
        self.play.pack(side="top")
        self.ms3 = tkinter.Label(self.bus, text="", font=("Arial", "12"))
        self.ms3.pack()

        self.ps = tkinter.Frame(master)
        self.ps["pady"] = -100
        self.ps["padx"] = 50
        self.ps.pack()
        self.pause = tkinter.Button(self.ps)
        self.pause["text"] = "Pause"
        self.pause["font"] = ("Arial", "10")
        self.pause["width"] = 10
        self.pause["command"] = self.Pause
        self.pause.pack()
        self.ms4 = tkinter.Label(self.bus, text="", font=("Arial", "12"))
        self.ms4.pack()

    def servidor(self):
        pass

    
    def buscarNome(self):
        musga = self.nome.get()
        if musga not in self.musica:
            self.ms2["text"] = "Música não encontrada"
        else:
            self.ms2["text"] = "Música encontrada"
    
    def Play(self):
        pass

    def Pause(self):
        pass

root = tkinter.Tk()
aplic(root)
root.mainloop()