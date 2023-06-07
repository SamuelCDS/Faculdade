import socket, sys, http.client
HOST = "localhost"
PORT = 8888
try:
    MS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = http.client.HTTPConnection(HOST, PORT)
    MS.connect((HOST, PORT))
    MS.send(b'GET /pages/index1.html HTTP/1.0\r\nHost> localhost\r\n\r\n')
    while True:
        data = MS.recv(512)
        if(len(data)<1):
            break
        print(data)
except Exception as e:
    print("Unexpected error: ", e, sys.exc_info()[0])
if MS != None:
    MS.close()