package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"os"
)

func receiveMessages(conn net.Conn) {
	reader := bufio.NewReader(conn)
	for {
		msg, err := reader.ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}
		fmt.Print(msg)
	}
}

func main() {
	conn, err := net.Dial("tcp", "localhost:1234")
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()
	go receiveMessages(conn)

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		var msg string
		msg = scanner.Text()
		conn.Write([]byte(msg + "\n"))

	}
}
