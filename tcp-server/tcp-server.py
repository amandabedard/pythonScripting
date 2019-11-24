import socket
import threading

bindIp = "0.0.0.0"
bindPort = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bindIp, bindPort))

server.listen(5)

print "[*] Listening on %s:%d" % (bindIp, bindPort)

def handleClient(clientSocket):
    request = clientSocket.recv(1024)
    print "[*] Recieved: %s" % request

    clientSocket.send("ACK!")
    clientSocket.close()

while True:
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    clientHandler = threading.Thread(target=handleClient,args=(client,))
    clientHandler.start()