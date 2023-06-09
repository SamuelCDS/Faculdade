import socket, pyaudio, tkinter

class Aplic:
    def __init__(self, master=None):
        self.principal = tkinter.Frame(master)
        self.principal["pady"] = 60
        self.principal["padx"] = 100
        self.principal.pack(side="top")
        self.msg = tkinter.Label(self.principal, text="Stream de Áudio")
        self.msg["font"] = ("Arial", "14", "bold")
        self.msg.pack(side="top")
        
        #Saida de textos:
        self.textout = tkinter.Frame(master)
        self.textout["padx"] = 30
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
        self.ps["pady"] = -100
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
        self.addressSV = ('localhost', 12345)
        self.To["text"] = "Conectando..."
        self.client.connect(self.addressSV)

    def SaidaTexto(self,texto):
        self.ms1["text"] = texto
    
    def Reiniciar(self):
        pass
    
    def Play(self):
        self.client.send(1024)
        self.pa = pyaudio.PyAudio()
        self.stream = pyaudio.open(format=pyaudio.paInt16,
                                   channels=2,
                                   rate=44100
                                   output=True)
        while True:
            self.data = self.client.recv(1024)
            if not data:
                break
            self.stream.write(self.data)

    def Pause(self):
        self.stream.stop_stream()
        self.stream.close()

if __name__ == '__main__':
    root = tkinter.Tk()
    Aplic(root)
    root.mainloop()
