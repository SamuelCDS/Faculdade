import socket, sys, tkinter

HOST = 'localhost'
PORT = 1234

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen(4)


class Aplic:
    def __init__(self, master=None):
        file = "/home/samuelcds/Músicas/Angelo Boltini - This Town.mp3"
        self.musica = open(file, "rb")

        self.principal = tkinter.Frame(master)
        self.principal["pady"] = 60
        self.principal["padx"] = 100
        self.principal.pack(side="top")
        self.msg = tkinter.Label(self.principal, text="Stream de Áudio")
        self.msg["font"] = ("Arial", "14", "bold")
        self.msg.pack(side="top")

        self.textout = tkinter.Frame(master)
        self.textout["padx"] = 30
        self.textout.pack()
        self.ms1 = tkinter.Label(self.textout, text="", font="Arial")
        self.ms1.pack(side="top")
        

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

        self.espaco = tkinter.Frame(master)
        self.espaco["pady"] = 10
        self.espaco.pack()
        self.space = tkinter.Label(self.espaco, text="", font=("Arial", "12"))
        self.space.pack()
    
    def Reiniciar(self):
        pass
    
    def Play(self):
        pass

    def Pause(self):
        pass

if __name__ == '__main__':
    root = tkinter.Tk()
    Aplic(root)
    root.mainloop()
