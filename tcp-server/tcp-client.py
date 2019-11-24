import socket

targetHost = "0.0.0.0"
targetPort = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((targetHost, targetPort))
client.send("GET /HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n")
response = client.recv(4096)

print response