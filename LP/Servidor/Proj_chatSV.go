package main

import (
	"log"
	"net"
)

type Client struct {
	conn    net.Conn
	usuario string
}

func handleClient(client Client, clients map[net.Conn]Client, messages chan<- string) {
	buffer := make([]byte, 1024)

	// Enviar mensagem de boas-vindas
	client.conn.Write([]byte("Bem-vindo ao chat!\nLogado como: "))

	bytesRead, err := client.conn.Read(buffer)
	if err != nil {
		log.Println(err)
		client.conn.Close()
		delete(clients, client.conn)
		return
	}
	client.usuario = string(buffer[:bytesRead])

	msg := client.usuario + " entrou no chat.\n"
	messages <- msg

	for {
		bytesRead, err := client.conn.Read(buffer)
		if err != nil {
			log.Println("Cliente desconectado.")
			client.conn.Close()
			delete(clients, client.conn)
			msg := client.usuario + " saiu do chat.\n"
			messages <- msg
			return
		}
		msg := client.usuario + ": " + string(buffer[:bytesRead])
		messages <- msg
	}
}

func main() {
	clients := make(map[net.Conn]Client)
	messages := make(chan string)

	listener, err := net.Listen("tcp4", "127.0.0.1:1234")
	if err != nil {
		log.Fatal(err)
	}
	defer listener.Close()
	log.Println("Servidor de chat iniciado na porta 1234")

	go func() {
		for {
			conn, err := listener.Accept()
			if err != nil {
				log.Println(err)
				continue
			}
			client := Client{conn: conn}
			clients[conn] = client
			log.Printf("Novo cliente conectado: %v\n", conn.RemoteAddr().String())
			go handleClient(client, clients, messages)
		}
	}()

	for {
		msg := <-messages
		for _, client := range clients {
			client.conn.Write([]byte(msg))
		}
	}
}
